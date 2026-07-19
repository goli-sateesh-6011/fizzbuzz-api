from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "FizzBuzz API"
    APP_VERSION: str = "1.0.0"
    LOG_LEVEL: str = "INFO"
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()