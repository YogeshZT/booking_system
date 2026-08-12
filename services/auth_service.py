class AuthService:
    def __init__(self, user_repository, redis):
        self.user_repository = user_repository
        self.redis = redis