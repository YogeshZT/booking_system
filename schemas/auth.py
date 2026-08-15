from pydantic import BaseModel


class LoginRequest(BaseModel):
    email : str
    password : str


class RegisterRequest(BaseModel):
    name : str
    email : str
    password : str


class VerifyEmailRequest(BaseModel):
    verification_token : str


class ResendVerificationRequest(BaseModel):
    email : str


class ForgotPasswordRequest(BaseModel):
    email : str


class ResetPasswordRequest(BaseModel):
    reset_token : str
    new_password: str