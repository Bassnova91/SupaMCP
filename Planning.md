# Supabase MCP Server Project Plan

## Overview
This project aims to create a **Supabase MCP server** using Python. The server will follow the **Model Context Protocol (MCP)**, a standard that allows Large Language Models (LLMs) and AI tools to interact with platforms like Supabase. Supabase is an open-source Firebase alternative offering tools such as a PostgreSQL database, authentication, and real-time subscriptions. The MCP server will enable AI clients (e.g., Cursor or Claude) to perform tasks like managing Supabase projects, querying databases, and fetching configurations.

### Scope
The initial scope includes:
- Building an MCP-compliant server that integrates with Supabase APIs.
- Implementing core MCP tools, such as:
  - Listing Supabase projects (`list_projects`)
  - Executing SQL queries (`execute_sql`)
  - Applying database migrations (`apply_migration`)
  - Fetching project configurations (`fetch_config`)
- Ensuring secure authentication and authorization for AI clients.

Future enhancements (out of initial scope):
- Support for Supabase Edge Functions.
- Integration with Supabase Storage.

### Technologies
- **Programming Language**: Python 3.10+
- **Web Framework**: FastAPI (chosen for its asynchronous capabilities and API-friendly design)
- **Supabase Integration**: Supabase Python client (`supabase-py`)
- **Authentication**: Supabase Personal Access Tokens (PAT) for server authentication; OAuth 2.0 as a future option for clients
- **Deployment**: Cloud platform (e.g., Heroku, AWS, or Google Cloud)
- **Testing**: Pytest for unit and integration testing
- **Documentation**: Markdown files and inline code comments

### Architecture
- The server will expose HTTP endpoints following the MCP specification.
- AI clients will send requests in the MCP message format, which the server will process and translate into Supabase API calls.
- Responses will be formatted according to MCP standards and returned to the client.
- The server will use the Supabase Management API and Database API to interact with Supabase resources.

### Security Considerations
- **Authentication**: Use Supabase PATs to authenticate the server with Supabase.
- **Authorization**: Plan for OAuth 2.0 to authorize AI clients (future scope).
- **Data Safety**: Implement read-only modes for database queries where applicable.
- **Rate Limiting**: Add limits to prevent abuse from AI clients.

### Deployment
- The server will be containerized with Docker for portability.
- It will be deployed to a cloud platform (e.g., Heroku) with environment variables for sensitive data like PATs.

## SupaMCP 服务器（MCP + Supabase）

### 架构与目标
- 采用 MCP Python SDK（低层 stdio_server 实现）
- 通过 Stdio 协议与 LLM 客户端（如 Claude Desktop）集成
- 通过 Supabase Python SDK 连接 Supabase Postgres 数据库
- 所有数据库连接参数通过环境变量配置（SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY）

### 功能与模块
- 工具（Tools）：
  - 查询表记录（支持条件、分页）
  - 插入单条/多条记录
  - 更新单条/多条记录
  - 删除单条/多条记录
- 每个工具均有详细描述，便于 LLM 理解其用途和参数
- 工具参数和返回值均使用 Pydantic 校验
- 代码结构：
  - 入口：supa_mcp/server.py
  - 工具定义：supa_mcp/tools.py
  - Supabase 适配：supa_mcp/supabase_client.py
  - 配置与环境变量：supa_mcp/config.py
  - 单元测试：tests/supa_mcp/

### 风格与约束
- 遵循 PEP8，类型注解，black 格式化
- 结构清晰，分层解耦，便于扩展
- 工具描述和参数注释详尽，适配 LLM 理解
- 所有数据库操作均通过 Supabase 官方 Python SDK
- 环境变量安全管理，不在代码中硬编码密钥

### 未来扩展
- 支持更多 Supabase 功能（如存储、认证等）
- 增加资源（Resources）和提示（Prompts）能力
- 支持多租户/多项目配置

---

## Development Phases
1. **Phase 1**: Set up the server and implement basic MCP tools (e.g., `list_projects`).
2. **Phase 2**: Add authentication and security features.
3. **Phase 3**: Expand with additional tools (e.g., `execute_sql`, `apply_migration`).
4. **Phase 4**: Test and document the server.
5. **Phase 5**: Deploy to a cloud platform.

---

## Risks and Mitigations
- **Risk**: Changes in the MCP specification.
  - **Mitigation**: Stay updated with MCP documentation and adapt as needed.
- **Risk**: Security flaws in request handling.
  - **Mitigation**: Validate inputs and enforce rate limits.
- **Risk**: Supabase API limits.
  - **Mitigation**: Optimize API calls and cache responses where possible.

---

## Success Criteria
- The server handles MCP requests from AI clients correctly.
- Core tools (`list_projects`, `execute_sql`) work as expected.
- The server passes all tests.
- Documentation is clear for setup and usage.