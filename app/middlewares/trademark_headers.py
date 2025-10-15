from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class TrademarkMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers['X-Powered-By'] = 'FastAPI'
        return response
