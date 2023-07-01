from pydantic import BaseSettings


class Settings(BaseSettings):
    # ツイート済み日時を書き込むファイル名
    tweeted_file: str = 'tweeted'
    # ログ出力の設定ファイル
    logging_config_file: str = 'logging_config.json'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
