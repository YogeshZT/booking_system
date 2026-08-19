from fastapi import Request
from fastapi.responses import JSONResponse

from exceptions.exceptions import AppException

async def app_exception_handler(
    request : Request,
    exception : AppException
):
    return JSONResponse(
        status_code=exception.status_code,
        content={
            "error":exception.message
        }
    )

async def generic_exception_handler(
    request : Request,
    exception : Exception
):
    return JSONResponse(
        status_code=500,
        content={
            "error":"Internal server error"
        }
    )