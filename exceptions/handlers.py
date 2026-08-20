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
            "status":False,
            "message":exception.message,
            "data":{}
        }
    )

async def generic_exception_handler(
    request : Request,
    exception : Exception
):
    return JSONResponse(
        status_code=500,
        content={
            "status":False,
            "message":"Internal server error",
            "data":{}
        }
    )