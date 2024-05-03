from typing import Type, Callable, cast

import pytest
from fastapi_users.authentication import Transport, CookieTransport, AuthenticationBackend, Strategy
from starlette.responses import Response

from src.auth.auth import get_jwt_strategy
from tests.conftest import client, MockTransport, UserModel


@pytest.fixture(params=[MockTransport])
def transport(request) -> Transport:
    transport_class: Type[CookieTransport] = request.param
    return transport_class(cookie_max_age=3600)


@pytest.fixture
def user() -> UserModel:
    return UserModel(
        username="string",
        hashed_password="string",
    )


@pytest.fixture()
def get_strategy() -> Callable[..., Strategy]:
    strategy_class = get_jwt_strategy
    return lambda: strategy_class()


@pytest.fixture
def backend(
        transport: Transport, get_strategy: Callable[..., Strategy]
) -> AuthenticationBackend:
    return AuthenticationBackend(
        name="mock", transport=transport, get_strategy=get_strategy
    )


class TestAuth:
    def test_register(self):
        response = client.post("/auth/register", json={
            "username": "string",
            "email": "string",
            "password": "string",
            "is_active": True,
            "is_superuser": False,
            "is_verified": False,
        })

        assert response.status_code == 201

# Check cookie header as well
    @pytest.mark.authentication
    async def test_login(self, backend: AuthenticationBackend, user: UserModel):
        strategy = cast(Strategy, backend.get_strategy())
        result = await backend.login(strategy, user)
        assert isinstance(result, Response)

