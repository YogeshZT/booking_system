from fastapi  import APIRouter

router = APIRouter(
    prefix="/api/v1/auth"
)
@router.post("/login")
def login(
    login_payload :
):
    pass

@router.post("/logout")
def logout():
    return 

@router.post("/register")
def register():
    pass

@router.post("/verify-email")
def verify_email():
    pass

@router.post("/resend-verification")
def resend_verification():
    pass

@router.post("/reset-password")
def reset_password():
    pass

@router.post("/forgot-password")
def forgot_pasword():
    pass