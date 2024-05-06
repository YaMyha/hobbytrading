from typing import Type, Callable, cast

import pytest
from fastapi_users.authentication import Transport, CookieTransport, AuthenticationBackend, Strategy
from httpx import Response

from src.auth.auth import get_jwt_strategy, auth_backend
from tests.conftest import client, MockTransport, UserModel


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

    def test_login(self):
        user_data = {
            "username": "string",
            "password": "string"
        }
        response = client.post("/auth/jwt/login", data=user_data)

        assert isinstance(response, Response)
        assert response.status_code == 200 or 204, f"Ошибка авторизации: {response.text}"

        cookie: str = response.headers["set-cookie"].split(";")[0]
        assert "fastapiusersauth" in cookie

