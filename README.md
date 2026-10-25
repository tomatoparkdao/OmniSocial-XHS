<h1 align="center">OmniSocial XHS 小红书自动运营平台</h1>

<p align="center">
  <b>面向小红书运营的内容采集、智能创作、账号管理与自动发布平台 —— 先沉淀内容，再规模化运营</b><br>
  搜索采集 ＋ 内容库 ＋ AI 改写 ＋ 图片优化 ＋ 多账号管理 ＋ 定时发布 ＋ 数据洞察<br>
  发现素材 → 内容整理 → AI 创作 → 素材优化 → 发布校验 → 自动运营 → 数据复盘<br>
  所有发布与自动化动作均需由使用者确认账号授权、平台规则与内容合规边界
</p>

<p align="center">
  <a href="https://github.com/tomatoparkdao/OmniSocial-XHS"><img src="https://img.shields.io/badge/%E4%BB%93%E5%BA%93-OmniSocial--XHS-1f6feb?style=flat-square" alt="仓库 OmniSocial-XHS"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/%E8%AE%B8%E5%8F%AF-MIT-2ea043?style=flat-square" alt="许可 MIT"></a>
  <a href="https://tomatoparkdao.github.io/OmniSocial-XHS/"><img src="https://img.shields.io/badge/%E6%BC%94%E7%A4%BA-OmniSocial--XHS-8957e5?style=flat-square" alt="演示 OmniSocial-XHS"></a>
  <a href="https://discord.gg/vdgTEpXMh3"><img src="https://img.shields.io/badge/%E7%A4%BE%E5%8C%BA-Discord-5865f2?style=flat-square" alt="开源社区 Discord"></a>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776ab?style=flat-square" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/React-19-61dafb?style=flat-square" alt="React 19">
  <img src="https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=flat-square" alt="FastAPI">
</p>

<p align="center">
  <b>简体中文</b>　｜　<a href="https://tomatoparkdao.github.io/OmniSocial-XHS/">在线演示</a>
</p>

> © OmniSocial XHS ｜ 开发者：Mochiball ｜ OmniSocial XHS 小红书自动运营平台 — 未经授权禁止复制、传播或二次分发。

它不是单一的爬虫，也不是单一的发布器——**第一步是把账号、素材、内容和运营目标放进同一条工作流**：先搜索与采集，再进入内容库沉淀；随后通过 AI 完成标题、正文和标签改写，按需优化图片，最后经过发布校验进入立即发布、定时发布或自动运营任务。每一阶段都保留可追踪的任务状态与结果。

<table width="100%" style="width:100%; min-width:100%; table-layout:auto;">
<thead><tr><th align="left">项目</th><th align="left">值</th><th align="left">说明</th></tr></thead>
<tbody>
<tr><td>产品名称</td><td>OmniSocial XHS 小红书自动运营平台</td><td>面向小红书运营的内容与账号工作台</td></tr>
<tr><td>核心能力</td><td>采集、内容库、AI 创作、图片优化、发布、自动运营</td><td>从素材发现到数据复盘的完整链路</td></tr>
<tr><td>技术栈</td><td>Python / FastAPI / React / TypeScript</td><td>支持本地开发与 Docker 部署</td></tr>
<tr><td>版本</td><td>v0.1.0</td><td>前后端统一的初始版本</td></tr>
<tr><td>运行方式</td><td>本地服务 / Docker / GitHub Pages 演示</td><td>Pages 仅展示前端，不承载后端业务</td></tr>
<tr><td>许可</td><td>MIT（见 <a href="LICENSE">LICENSE</a>）</td><td>第三方依赖按各自许可证执行</td></tr>
<tr><td>仓库</td><td><a href="https://github.com/tomatoparkdao/OmniSocial-XHS">tomatoparkdao/OmniSocial-XHS</a></td><td>项目源码与部署配置</td></tr>
<tr><td>演示页面</td><td><a href="https://tomatoparkdao.github.io/OmniSocial-XHS/">OmniSocial-XHS</a></td><td>静态前端演示</td></tr>
<tr><td>开源社区</td><td><a href="https://discord.gg/vdgTEpXMh3">Discord 开源社区</a></td><td>使用交流、问题反馈与协作讨论</td></tr>
</tbody>
</table>

## 项目定位

同一条内容从发现、整理到发布，往往要在搜索工具、表格、图片工具、AI 平台和创作者平台之间反复切换。OmniSocial XHS 将这些步骤收进一个工作台：

- 账号矩阵：绑定多个 PC / Creator 账号，统一管理 Cookie 与健康状态。
- 内容发现：关键词搜索、URL 直查、评论抓取和素材下载。
- 内容库：保存、标签、筛选、批量操作和 JSON / CSV 导出。
- 草稿工坊：AI 改写正文、润色标题、生成标签和整理图片素材。
- 发布中心：立即发布、定时发布、校验、状态跟踪、重试与取消。
- 自动运营：按关键词和频率执行搜索、改写、上传与发布流程。
- 数据洞察：互动趋势、热门话题、评论分析和运营报告。

## 能力一览

<table width="100%" style="width:100%; min-width:100%; table-layout:auto;">
<thead><tr><th align="left">层面</th><th align="left">具体能力</th></tr></thead>
<tbody>
<tr><td>账号与登录</td><td>PC 端 / 创作者平台登录，多账号绑定，Cookie 加密，健康巡检</td></tr>
<tr><td>内容采集</td><td>关键词搜索、笔记详情、用户内容、评论、批量 URL 抓取</td></tr>
<tr><td>内容资产</td><td>内容库、标签、卡片 / 列表视图、JSON / CSV 导出、媒体本地化</td></tr>
<tr><td>AI 创作</td><td>标题、正文、标签改写；支持 OpenAI 兼容 API</td></tr>
<tr><td>图片工坊</td><td>AI 图片生成、参考图、图片描述与原位替换</td></tr>
<tr><td>发布管理</td><td>图集 / 视频发布、可见性控制、立即 / 定时发布</td></tr>
<tr><td>自动运营</td><td>每日、每周或自定义间隔的任务调度与执行审计</td></tr>
<tr><td>数据分析</td><td>仪表盘、互动趋势、Top 内容、话题与评论分析</td></tr>
<tr><td>平台适配</td><td>小红书 PC、创作者、蒲公英、千帆相关能力</td></tr>
</tbody>
</table>

## 快速开始

### 环境要求

- Python 3.10+
- Node.js 20+

### 安装

```bash
git clone https://github.com/tomatoparkdao/OmniSocial-XHS.git
cd OmniSocial-XHS

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

npm install
cd frontend && npm install && cd ..
```

### 启动

```bash
python main.py --with-frontend
```

访问：

- Web 界面：http://localhost:5173
- API 文档：http://localhost:8000/docs
- GitHub Pages 演示：[OmniSocial-XHS](https://tomatoparkdao.github.io/OmniSocial-XHS/)

首次启动会创建数据库，注册账号后即可配置模型和平台账号。

### Docker

```bash
docker compose up -d
```

## 全流程总览

```text
① 账号准备   绑定账号 / 导入 Cookie / 健康检查
      │
      ▼
② 内容发现   关键词搜索 / URL 查询 / 评论与素材采集
      │
      ▼
③ 内容沉淀   内容库 / 标签 / 筛选 / 导出
      │
      ▼
④ 智能创作   标题正文改写 / 标签生成 / 图片优化
      │
      ▼
⑤ 发布运营   立即发布 / 定时发布 / 自动运营任务
      │
      ▼
⑥ 数据复盘   互动趋势 / 热门话题 / 评论分析 / 任务审计
```

## 项目结构

```text
OmniSocial XHS/
├── main.py                         # 统一启动入口
├── config/                         # 分层配置
├── apis/                           # 小红书平台 API 适配
├── xhs_utils/                      # 签名与请求工具
├── backend/app/
│   ├── main.py                     # FastAPI 应用
│   ├── api/                        # API 路由
│   ├── adapters/xhs/               # 平台适配层
│   ├── core/                       # 配置、数据库、安全与任务运行
│   ├── models/                     # 数据模型
│   ├── services/                   # 业务服务与调度
│   └── storage/                    # 媒体与导出文件
├── frontend/src/                   # React 前端
├── tests/                          # 后端测试
├── Dockerfile
└── docker-compose.yml
```

## 配置与安全

配置优先级为 `config/default.yaml` < `CONFIG_FILE` < `.env` < 环境变量。

```yaml
database:
  type: sqlite
security:
  secret_key: change-me
scheduler:
  enabled: false
```

常用环境变量：`SECRET_KEY`、`DATABASE_TYPE`、`DATABASE_URL`、`SCHEDULER_ENABLED`。

Cookie、API Key 和账号信息属于敏感数据。生产环境请使用独立密钥、持久化数据库和受控的部署环境。

## 开发与验证

```bash
npm run build --prefix frontend
.venv/bin/python -m pytest tests/backend/test_root_main.py tests/backend/test_api.py -q
```

当前核心后端测试通过，前端构建通过。

## 使用边界

请遵守小红书及相关服务的用户协议、隐私政策和适用法律法规。使用账号、Cookie、内容与接口时，应确保拥有相应授权，并自行承担运营风险。自动化发布前请确认账号授权、内容版权和平台规则。

## 开源社区

加入 [Discord 开源社区](https://discord.gg/vdgTEpXMh3)，可进行使用交流、问题反馈和协作讨论。

## 许可证与署名

本项目采用 MIT License，详见 [LICENSE](LICENSE)。项目中保留的第三方组件、原始依赖及其许可证信息仍按各自条款执行。

---

> © OmniSocial XHS ｜ 开发者：Mochiball ｜ OmniSocial XHS 小红书自动运营平台 — 未经授权禁止复制、传播或二次分发。

