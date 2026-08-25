from fastapi  import APIRouter, Depends, Cookie, Response, Query

from dependencies import get_auth_service, get_current_user
from schemas.auth import LoginRequest, RegisterRequest, ResendVerificationRequest, ResetPasswordRequest, ForgotPasswordRequest
from services.auth_service import AuthService
from constants import SESSION_EXPIRY_SECONDS
from responses.common import SuccessResponse
from responses.auth_messages import *

router = APIRouter(
    prefix="/api/v1/auth"
)

@router.post("/login")
async def login(
    payload : LoginRequest,
    response: Response,
    auth_service : AuthService = Depends(get_auth_service)
):
    session_id = await auth_service.login(payload)
    response.set_cookie(
        key="session_id",
        value=session_id,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=SESSION_EXPIRY_SECONDS,
    )


@router.post("/logout")
async def logout(
    response: Response,
    user_id = Depends(get_current_user),
    session_id = Cookie(default = None),
    auth_service : AuthService = Depends(get_auth_service),
):
    await auth_service.logout(session_id)
    response.delete_cookie(
        key="session_id",
        httponly=True,
        secure=True,
        samesite="lax",
    )


@router.post("/register")
async def register(
    payload : RegisterRequest,
    auth_service : AuthService = Depends(get_auth_service)
):
    await auth_service.register(payload)
    return SuccessResponse(
        status=201,
        message=REGISTER_USER_SUCCESS_MESSAGE,
        data={}
    )


@router.get("/verify-email")
async def verify_email(
    token = Query(...),
    auth_service : AuthService = Depends(get_auth_service)
):
    await auth_service.verify_email(token)
    return SuccessResponse(
        status=200,
        message=EMAIL_VERIFIED_MESSAGE,
        data={}
    )


@router.post("/resend-verification")
async def resend_verification(
    payload : ResendVerificationRequest,
    auth_service : AuthService = Depends(get_auth_service)
):
    await auth_service.resend_verification(payload)
    return SuccessResponse(
        status=200,
        message=RESEND_VERIFY_EMAIL_SENT_MESSAGE,
        data={}
    )


@router.post("/forgot-password")
async def forgot_password(
    payload : ForgotPasswordRequest,
    auth_service : AuthService = Depends(get_auth_service)
):
    await auth_service.forgot_password(payload)
    return SuccessResponse(
        status=200,
        message=FORGOT_PASSWORD_SUCCESS_MESSAGE,
        data={}
    )


@router.get("/reset-password")
async def reset_password(
    payload : ResetPasswordRequest,
    auth_service : AuthService = Depends(get_auth_service)
):
    await auth_service.reset_password(payload)
    return SuccessResponse(
        status=200,
        message=RESET_PASSWORD_SUCCESS_RESPONSE,
        data={}
    )
