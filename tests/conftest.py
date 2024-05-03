import asyncio
import dataclasses
import uuid
from datetime import datetime
from typing import AsyncGenerator, Any, Optional

import pytest
from fastapi.openapi.models import Response
from fastapi.testclient import TestClient
from fastapi_users import models
from fastapi_users.authentication import CookieTransport, BearerTransport, Strategy
from fastapi_users.openapi import OpenAPIResponseType
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from api import app
from db.database import get_async_session
from db.modelsORM import metadata

from src.db.modelsORM import User
from tests.configs.config import TestSettings

settings = TestSettings()
engine_test = create_async_engine(url=settings.DATABASE_URL_asyncpg_test, poolclass=NullPool)
async_session_maker = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)
metadata.bind = engine_test


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[get_async_session] = override_get_async_session


@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.drop_all)


@pytest.fixture(scope='session')
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


client = TestClient(app)


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


class MockTransport(CookieTransport):
    def __init__(self, cookie_max_age: int):
        super().__init__(cookie_max_age=cookie_max_age)

def generate_id() -> int:
    return hash(uuid.uuid4())


@dataclasses.dataclass
class UserModel(models.UserProtocol[int]):
    username: str
    hashed_password: str
    id: int = dataclasses.field(default_factory=generate_id)
