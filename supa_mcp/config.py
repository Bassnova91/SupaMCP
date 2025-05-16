from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    配置类，从环境变量读取 Supabase 连接信息。
    Args:
        SUPABASE_URL (str): Supabase 项目 URL。
        SUPABASE_SERVICE_ROLE_KEY (str): Supabase 服务角色密钥。
    """
    SUPABASE_URL: str
    SUPABASE_SERVICE_ROLE_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()


