from fastapi import FastAPI
from app.api.routers import api_router

app = FastAPI(
    title="EasyAdmin",
    version="1.0",
    description="基于FastAPI的后台管理系统"
)

# 注册API路由
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
