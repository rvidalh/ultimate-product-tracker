from typing import Union

import uvicorn
from fastapi import FastAPI

from app.core.config import settings

app = FastAPI()


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
