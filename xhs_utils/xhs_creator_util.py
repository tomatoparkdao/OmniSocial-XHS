import json
import os

import execjs

from xhs_utils.xhs_creator.auth import XHSCreatorAuth
from xhs_utils.xhs_creator.params import (
    generate_request_params,
    generate_xsc as _generate_xsc,
)
_STATIC_DIR = os.path.join(os.path.dirname(__file__), 'xhs_creator', 'js')


def _compile_static_js(filename):
    with open(os.path.join(_STATIC_DIR, filename), 'r', encoding='utf-8') as f:
        return execjs.compile(f.read())


_JS_CACHE = {}


def _get_static_js(filename):
    if filename not in _JS_CACHE:
        _JS_CACHE[filename] = _compile_static_js(filename)
    return _JS_CACHE[filename]


class LazyStaticJS:
    def __init__(self, filename):
        self.filename = filename

    def call(self, *args):
        return _get_static_js(self.filename).call(*args)

    def eval(self, *args):
        return _get_static_js(self.filename).eval(*args)


signature_js = LazyStaticJS('xhs_creator_signature.js')
sign_js = LazyStaticJS('xhs_creator_sign.js')

_CREATOR_RAP_TPL_PATH = os.path.join(
    _STATIC_DIR, 'rap_fingerprint_creator.json',
)
_ALPHABET36 = '0123456789abcdefghijklmnopqrstuvwxyz'


def load_creator_rap_fingerprint_hex() -> str:
    """加载 Creator 发布接口的 rap 指纹模板（Uuid 每次随机化）。

    模板来自浏览器 Creator post_note x-rap-param 信封的 AES 解密
    （build 1.19.3，436B）。03ea 段的 16 字符会话 Uuid 每次重新随机，
    避免静态指纹聚类；03eb 槽位由生成侧按 url+body 现算覆写。
    """
    import random
    with open(os.path.abspath(_CREATOR_RAP_TPL_PATH), encoding='utf-8') as fh:
        tpl = json.load(fh)
    raw = bytearray.fromhex(tpl['bodyUnmaskedHex'])
    if raw[:6].hex() != '03ea00000010':
        raise RuntimeError('creator rap fingerprint template 03ea Uuid section not found')
    raw[6:22] = ''.join(random.choice(_ALPHABET36) for _ in range(16)).encode('ascii')
    return raw.hex()

def _require_auth(auth):
    if not isinstance(auth, XHSCreatorAuth):
        raise TypeError(
            'Creator signing now requires XHSCreatorAuth; create it with '
            'from_cookie(), from_qrcode_login(), or from_phone_login()'
        )
    return auth


def generate_xs(auth, api, data=''):
    headers, _, body = generate_request_params(_require_auth(auth), api, data)
    return headers['x-s'], headers['x-t'], body


def generate_xs_xs_common(auth, api, data=''):
    headers, _, _ = generate_request_params(_require_auth(auth), api, data)
    return headers['x-s'], headers['x-t'], headers['x-s-common']


def generate_xsc(auth, api, data=''):
    return _generate_xsc(_require_auth(auth), api, data)

# scene: image/video
def get_fileIds_params(scene):
    return {
        "biz_name": "spectrum",
        "scene": scene,
        "file_count": "1",
        "version": "1",
        "source": "web"
    }

def get_upload_media_headers(message, signature, token, *, user_agent, upload_host=''):
    # 2026-07-25 浏览器实抓（ros-upload-d4 PUT）：accept-encoding 含 zstd、
    # accept-language 为长列表、无 pragma 头；sec-fetch-site 随上传域与
    # creator.xiaohongshu.com 的站点关系变化（xhscdn.com -> cross-site）。
    sec_fetch_site = (
        'cross-site' if 'xhscdn.com' in str(upload_host) else 'same-site'
    )
    return {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
        "authorization": f"q-sign-algorithm=sha1&q-ak=null&q-sign-time={message}&q-key-time={message}&q-header-list=content-length;host&q-url-param-list=&q-signature={signature}",
        "cache-control": "",
        "content-type": "",
        "origin": "https://creator.xiaohongshu.com",
        "referer": "https://creator.xiaohongshu.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": sec_fetch_site,
        "user-agent": user_agent,
        "x-cos-security-token": token,
    }

def get_post_note_image_data(title, desc, postTime, post_loc, privacy_type, fileInfos):
    if postTime is None:
