# OmniSocial XHS

> 小红书一站式智能运营平台：采集、分析、AI 创作、素材处理、发布与运营任务统一管理。

> © OmniSocial XHS ｜ 开发者：Mochiball ｜ 项目仓库：[OmniSocial XHS](https://github.com/tomatoparkdao/OmniSocial-XHS)

## 项目概览

| 项目 | 内容 |
|---|---|
| 产品名称 | OmniSocial XHS |
| 产品定位 | 面向小红书运营的内容与账号工作台 |
| 版本 | 0.1.0 |
| 技术栈 | Python、FastAPI、React、TypeScript、SQLite/MySQL |
| 运行方式 | 本地开发、Docker |
| 许可 | MIT，详见 [LICENSE](LICENSE) |
| 开源仓库 | https://github.com/tomatoparkdao/OmniSocial-XHS |

## 一句话

OmniSocial XHS 把小红书运营中分散的搜索、采集、内容管理、AI 改写、图片处理、账号管理、发布和定时任务串成一条可追踪的工作流。

## 能力一览

### 账号与平台能力

- PC 端与创作者平台登录
- 多账号绑定、Cookie 加密存储与健康巡检
- 笔记、用户、评论、作品和互动数据获取
- 图集与视频素材上传
- 小红书、蒲公英、千帆相关接口适配

### 内容运营能力

- 关键词搜索、URL 查询与批量抓取
- 内容库、标签、卡片/列表视图和 JSON/CSV 导出
- 草稿编辑、标题/正文/标签 AI 改写
- 图片生成、图片描述与参考图优化
- 立即发布、定时发布、状态跟踪、重试与取消
- 自动运营任务、竞品监控、数据洞察和通知中心
- OpenAI 兼容模型配置

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

启动后访问：

- Web 界面：http://localhost:5173
- API 文档：http://localhost:8000/docs

首次启动会创建数据库，随后可注册账号并配置模型与平台账号。

### Docker

```bash
docker compose up -d
```

## 工作流

1. 在账号矩阵中绑定并验证平台账号。
2. 通过笔记发现或批量抓取将素材保存到内容库。
3. 在草稿工坊中编辑内容，按需调用 AI 改写和图片优化。
4. 在发布中心完成校验，选择立即发布或定时发布。
5. 在任务中心、通知中心和数据洞察中跟踪执行结果。

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
├── tests/                          # 自动化测试
├── Dockerfile
└── docker-compose.yml
```

## 配置

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

AI 功能需要在模型配置页面设置 OpenAI 兼容 API 端点及密钥。生产环境请使用独立密钥和持久化数据库，并妥善保护 Cookie、API Key 等敏感数据。

## 开发与验证

```bash
npm run build --prefix frontend
.venv/bin/python -m pytest tests/backend/test_root_main.py tests/backend/test_api.py -q
```

修改底层平台接口时，请优先通过 `backend/app/adapters/` 调用，避免业务层直接耦合签名实现。

## 使用边界

请遵守小红书及相关服务的用户协议、隐私政策和适用法律法规。使用账号、Cookie、内容与接口时，应确保拥有相应授权，并自行承担运营风险。

## 许可证与署名

本项目采用 MIT License，详见 [LICENSE](LICENSE)。项目中保留的第三方组件、原始依赖及其许可证信息仍按各自条款执行。

---

> © OmniSocial XHS ｜ 开发者：Mochiball ｜ OmniSocial XHS — 未经授权禁止复制、传播或二次分发。

