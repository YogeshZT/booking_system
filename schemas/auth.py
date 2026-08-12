from pydantic import BaseModel


class Login(BaseModel):
    email : str
    password : str

class Register(BaseModel):
    name : str
    email : str
    password : str

class VerifyEmail(BaseModel):
    verification_token : str

class ResendVerification(BaseModel):
    verification_token : str

class ForgotPassword(BaseModel):
    email : str

class ResetPassword(BaseModel):
    reset_token : str
    new_password: str