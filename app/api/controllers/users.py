from fastapi import APIRouter
from typing import Dict, Any

router = APIRouter()

# 模拟用户数据
MOCK_USERS = [
    {
        "id": 1,
        "username": "admin",
        "email": "admin@example.com",
        "full_name": "管理员",
        "role": "admin",
        "status": "active",
        "created_at": "2024-01-01T00:00:00",
        "last_login": "2024-01-15T10:30:00"
    },
    {
        "id": 2,
        "username": "user001",
        "email": "user001@example.com",
        "full_name": "张三",
        "role": "user",
        "status": "active",
        "created_at": "2024-01-02T00:00:00",
        "last_login": "2024-01-14T15:20:00"
    },
    {
        "id": 3,
        "username": "user002",
        "email": "user002@example.com",
        "full_name": "李四",
        "role": "user",
        "status": "inactive",
        "created_at": "2024-01-03T00:00:00",
        "last_login": "2024-01-10T09:15:00"
    }
]


@router.get("/users", summary="获取用户列表")
async def get_users() -> Dict[str, Any]:
    """
    获取所有用户列表
    
    Returns:
        Dict: 包含用户列表和统计信息的响应
    """
    return {
        "code": 200,
        "message": "获取用户列表成功",
        "data": {
            "users": MOCK_USERS,
            "total": len(MOCK_USERS),
            "active_count": len([u for u in MOCK_USERS if u["status"] == "active"]),
            "inactive_count": len([u for u in MOCK_USERS if u["status"] == "inactive"])
        }
    }


@router.get("/users/{user_id}", summary="获取用户详情")
async def get_user_by_id(user_id: int) -> Dict[str, Any]:
    """
    根据用户ID获取用户详细信息
    
    Args:
        user_id (int): 用户ID
        
    Returns:
        Dict: 用户详细信息
    """
    user = next((u for u in MOCK_USERS if u["id"] == user_id), None)
    
    if not user:
        return {
            "code": 404,
            "message": "用户不存在",
            "data": None
        }
    
    return {
        "code": 200,
        "message": "获取用户信息成功",
        "data": user
    }