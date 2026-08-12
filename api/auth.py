from fastapi  import APIRouter
from fastapi.params import Depends

from dependencies import get_auth_service
from schemas.auth import LoginRequest, RegisterRequest, VerifyEmailRequest, ResendVerificationRequest, \
    ResetPasswordRequest, ForgotPasswordRequest

router = APIRouter(
    prefix="/api/v1/auth"
)

@router.post("/login")
def login(
    payload : LoginRequest,
    auth_service = Depends(get_auth_service)
):
    return auth_service.login(payload)

@router.post("/logout")
def logout(
    auth_service = Depends(get_auth_service)
):
    return auth_service.logout()

@router.post("/register")
def register(
    payload : RegisterRequest,
    auth_service = Depends(get_auth_service)
):
    return auth_service.register(payload)

@router.post("/verify-email")
def verify_email(
    payload : VerifyEmailRequest,
    auth_service = Depends(get_auth_service)
):
    return auth_service.verify_email(payload)

@router.post("/resend-verification")
def resend_verification(
    payload : ResendVerificationRequest,
    auth_service = Depends(get_auth_service)
):
    return auth_service.resend_verification(payload)

@router.post("/reset-password")
def reset_password(
    payload : ResetPasswordRequest,
    auth_service = Depends(get_auth_service)
):
    return auth_service.reset_password(payload)

@router.post("/forgot-password")
def forgot_pasword(
    payload : ForgotPasswordRequest,
    auth_service = Depends(get_auth_service)
):
    return auth_service.forgot_password()