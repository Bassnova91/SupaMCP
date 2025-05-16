

## 2024-06-10
- [x] 初始实现 SupaMCP 服务器：
  - [x] 基于 MCP Python SDK，采用 stdio 协议
  - [x] 工具：查询、插入、更新、删除 Supabase 表记录
  - [x] 环境变量配置 Supabase URL 和服务密钥
  - [x] 工具参数和返回值均用 Pydantic 校验
  - [x] 每个工具有详细描述，便于 LLM 理解

2024-06-11
- [ ] 为 MCP 工具编写单元测试（tests/supa_mcp/test_tools.py）：
  - [ ] read_table_rows：常规、边界、异常用例
  - [ ] create_table_records：常规、边界、异常用例
  - [ ] update_table_records：常规、边界、异常用例
  - [ ] delete_table_records：常规、边界、异常用例
- [ ] 测试覆盖：
  - [ ] 每个工具至少 1 个正常用例、1 个边界用例、1 个失败用例
  - [ ] 使用 Pytest，必要时 mock Supabase client
- [ ] 完善/修正 tools.py（如需与 server.py 工具保持一致，或仅做 re-export）
- [ ] 文档与注释：确保所有测试和工具函数有清晰注释和 docstring
- [ ] 发现新问题及时补充到 Task.md “Discovered During Work”