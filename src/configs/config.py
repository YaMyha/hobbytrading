import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env-render")


class AppSettings:
    @property
    def DB_HOST(self):
        return os.environ.get("DB_HOST")

    @property
    def DB_PORT(self):
        return os.environ.get("DB_PORT")

    @property
    def DB_NAME(self):
        return os.environ.get("DB_NAME")

    @property
    def DB_USER(self):
        return os.environ.get("DB_USER")

    @property
    def DB_PASS(self):
        return os.environ.get("DB_PASS")

    @property
    def REDIS_HOST(self):
        return os.environ.get("REDIS_HOST")

    @property
    def REDIS_PORT(self):
        return os.environ.get("REDIS_PORT")

    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def REDIS_URL(self):
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"


settings = AppSettings()

# from dotenv import find_dotenv, load_dotenv
# from pydantic_settings import BaseSettings, SettingsConfigDict
# import os
#
# DOTENV = os.path.join(os.path.dirname(__file__), ".env-prod")
#
#
# class AppSettings(BaseSettings):
#     DB_HOST: str
#     DB_PORT: int
#     DB_USER: str
#     DB_PASS: str
#     DB_NAME: str
#
#     REDIS_HOST: str
#     REDIS_PORT: int
#
#     model_config = SettingsConfigDict(env_file=DOTENV, env_file_encoding="utf-8", extra='ignore')
#
#     @property
#     def DATABASE_URL_asyncpg(self):
#         return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
#
#     @property
#     def REDIS_URL(self):
#         return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"
#
#
# settings = AppSettings()
