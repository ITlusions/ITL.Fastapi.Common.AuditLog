import uuid
import os
import socket
import time
import logging
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("audit")

class AuditLogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        # Generate request ID for each request and correlation ID for each client session
        request_id = str(uuid.uuid4())
        correlation_id = request.headers.get("X-Correlation-ID", str(uuid.uuid4()))

        # Get server hostname and version from env
        hostname = socket.gethostname()
        version = os.getenv("APP_VERSION", "unknown")

        # Log request details from client
        logger.info(f"Request: {request.method} {request.url} | Request ID: {request_id} | Correlation ID: {correlation_id}")

        # Process request
        response = await call_next(request)

        # Compute request duration for performance monitoring
        duration = time.time() - start_time

        # Add headers to response for monitoring, traceabilty and debugging
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Correlation-ID"] = correlation_id
        response.headers["X-Server-Hostname"] = hostname
        response.headers["X-App-Version"] = version

        # Log response details
        logger.info(f"Response: {response.status_code} | Request ID: {request_id} | Correlation ID: {correlation_id} | Duration: {duration:.2f}s")

        return response
