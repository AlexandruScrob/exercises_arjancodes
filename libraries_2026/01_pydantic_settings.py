from pathlib import Path

from pydantic import BaseModel, SecretStr, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseModel):
    host: str = "localhost"
    port: int = 5432
    user: str = "postgres"
    password: SecretStr
    database: str

    @computed_field
    @property
    def url(self) -> str:
        return (
            f"postgresql://{self.user}:"
            f"{self.password.get_secret_value()}@"
            f"{self.host}:{self.port}/{self.database}"
        )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="example.env",
        env_prefix="APP_",
        env_nested_delimiter="__",
        extra="ignore",
    )

    debug: bool = False
    app_name: str = "My Application"
    log_level: str = "INFO"
    data_dir: Path = Path("./data")

    database: DatabaseSettings


def main() -> None:
    settings = Settings()
    print(settings.dict())


if __name__ == "__main__":
    main()
