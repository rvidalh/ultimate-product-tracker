from typing import Union

import uvicorn
from fastapi import FastAPI

from app.core.config import get_settings

app = FastAPI()
settings = get_settings()


@app.get("/health", response_model=dict[str, Union[str, bool]])
async def health_check():
    return {
        "app_name": settings.app_name,
        "status": "ok",
        "debug": settings.debug,
    }


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        log_level="info",
    )
