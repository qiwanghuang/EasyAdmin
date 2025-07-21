from fastapi import APIRouter
from .controllers import users

# 创建API路由器
api_router = APIRouter()

# 注册用户相关路由
api_router.include_router(users.router, prefix="/api/v1", tags=["用户管理"])