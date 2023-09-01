from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport
from fastapi_users.authentication import JWTStrategy
from fastapi_users.authentication import AuthenticationBackend

from auth.manager import get_user_manager
from auth.models import User

from config import JWT_SECRET

cookie_transport = CookieTransport(cookie_name="netgraph",cookie_max_age=3600)

SECRET = JWT_SECRET

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
current_user = fastapi_users.current_user()
active_user = fastapi_users.current_user(active=True)