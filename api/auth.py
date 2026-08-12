from fastapi  import APIRouter

router = APIRouter(
    prefix="/api/v1/auth"
)
@router.post("/login")
def login():
    pass

@router.post("/logout")
def logout():
    return 

@router.post("/signup")
def signup():
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