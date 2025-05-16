from supabase import create_client
from .config import settings
from supa_mcp.tools import mcp

supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_SERVICE_ROLE_KEY)

def insert_user(user_name: str):
    """
    向 users 表插入一条记录。
    Args:
        user_name (str): 用户名
    Returns:
        dict: 插入结果
    """
    data = {"user_name": user_name}
    result = supabase.table("users").insert(data).execute()
    return result.data