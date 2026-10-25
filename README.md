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

| 项目 | 值 | 说明 |
|---|---|---|
| 产品名称 | OmniSocial XHS 小红书自动运营平台 | 面向小红书运营的内容与账号工作台，覆盖发现、创作、发布和复盘 |
| 核心能力 | 采集、内容库、AI 创作、图片优化、发布、自动运营 | 从素材发现到数据复盘的完整链路，适合个人与团队运营流程 |
| 技术栈 | Python / FastAPI / React / TypeScript | 支持本地开发、Docker 部署与 GitHub Pages 前端演示 |
| 版本 | v0.1.0 | 前后端统一的初始版本 |
| 运行方式 | 本地服务 / Docker / GitHub Pages 演示 | Pages 仅展示前端，不承载后端业务 |
| 许可 | MIT（见 [LICENSE](LICENSE)） | 第三方依赖按各自许可证执行 |
| 仓库 | [tomatoparkdao/OmniSocial-XHS](https://github.com/tomatoparkdao/OmniSocial-XHS) | 项目源码与部署配置 |
| 演示页面 | [OmniSocial-XHS](https://tomatoparkdao.github.io/OmniSocial-XHS/) | 静态前端演示 |
| 开源社区 | [Discord 开源社区](https://discord.gg/vdgTEpXMh3) | 使用交流、问题反馈与协作讨论 |

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

| 层面 | 具体能力 | 说明 |
|---|---|---|
| 账号与登录 | PC 端 / 创作者平台登录，多账号绑定，Cookie 加密，健康巡检；支持二维码、验证码与 Cookie 导入 | 统一维护账号状态、登录凭证与授权有效期，减少重复切换平台，并在凭证失效时提供明确的状态反馈 |
| 内容采集 | 关键词搜索、笔记详情、用户内容、评论、批量 URL 抓取；支持排序、类型与时间筛选 | 支持从搜索结果和指定链接沉淀内容，并保存图片、视频、作者信息、互动数据与评论上下文 |
| 内容资产 | 内容库、标签、卡片 / 列表视图、JSON / CSV 导出、媒体本地化；支持批量操作与原文查看 | 将采集素材统一归档，支持筛选、标签管理、批量处理、结构化导出和来源追踪，形成可复用的内容资产 |
| AI 创作 | 标题、正文、标签改写；支持 OpenAI 兼容 API、模型配置与多轮编辑 | 在草稿编辑流程中完成结构化改写，并保留人工确认、继续编辑、版本切换与结果回退能力 |
| 图片工坊 | AI 图片生成、参考图、图片描述与原位替换；支持普通图片资产管理 | 对草稿素材进行描述、生成和优化，便于快速形成统一的内容资产，并在原图与结果之间进行对比确认 |
| 发布管理 | 图集 / 视频发布、可见性控制、立即 / 定时发布；支持发布校验、状态追踪、重试与取消 | 发布前进行内容、账号和素材校验，记录完整任务状态，支持失败重试、定时任务管理与异常结果追踪 |
| 自动运营 | 每日、每周或自定义间隔的任务调度与执行审计；支持关键词、账号与发布参数配置 | 按关键词和频率串联搜索、内容改写、素材上传与发布步骤，并保留每次自动执行的输入、输出和结果 |
| 数据分析 | 仪表盘、互动趋势、Top 内容、话题与评论分析；支持运营报告和历史数据查看 | 汇总内容表现、互动变化、热门话题和评论信息，辅助判断选题效果、账号表现与下一阶段运营方向 |
| 平台适配 | 小红书 PC、创作者、蒲公英、千帆相关能力；通过统一适配层组织平台接口 | 通过适配层隔离不同平台接口，便于在统一工作台中调用，并为后续扩展其他内容平台保留结构空间 |

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

### 演示账号

GitHub Pages 演示和本地前端均支持使用以下独立演示账号直接进入工作台：

| 项目 | 值 |
|---|---|
| 演示账号 | `demo` |
| 演示密码 | `Xhs2026` |

演示账号仅用于查看前端工作台，不影响原有注册、登录和真实账号数据。

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

