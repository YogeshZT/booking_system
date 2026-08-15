from fastapi  import APIRouter, Depends, Cookie

from dependencies import get_auth_service, get_current_user
from schemas.auth import LoginRequest, RegisterRequest, VerifyEmailRequest, ResendVerificationRequest, \
    ResetPasswordRequest, ForgotPasswordRequest
from services.auth_service import AuthService

router = APIRouter(
    prefix="/api/v1/auth"
)

@router.post("/login")
async def login(
    payload : LoginRequest,
    auth_service : AuthService = Depends(get_auth_service)
):
    return await auth_service.login(payload)


@router.post("/logout")
async def logout(
    user_id = Depends(get_current_user),
    session_id = Cookie(default = None),
    auth_service : AuthService = Depends(get_auth_service),
):
    return auth_service.logout(session_id)


@router.post("/register")
async def register(
    payload : RegisterRequest,
    auth_service : AuthService = Depends(get_auth_service)
):
    return auth_service.register(payload)


@router.post("/verify-email")
async def verify_email(
    payload : VerifyEmailRequest,
    auth_service : AuthService = Depends(get_auth_service)
):
    return auth_service.verify_email(payload)


@router.post("/resend-verification")
async def resend_verification(
    payload : ResendVerificationRequest,
    auth_service : AuthService = Depends(get_auth_service)
):
    return auth_service.resend_verification(payload)


@router.post("/forgot-password")
async def forgot_password(
    payload : ForgotPasswordRequest,
    auth_service : AuthService = Depends(get_auth_service)
):
    return auth_service.forgot_password(payload)


@router.post("/reset-password")
async def reset_password(
    payload : ResetPasswordRequest,
    auth_service : AuthService = Depends(get_auth_service)
):
    return auth_service.reset_password(payload)
