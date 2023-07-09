from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    # ツイート済み日時が保存されていない場合にツイートする最大数
    untweeted_max_num: int = 3

    # ツイート済み日時を書き込むファイル名
    tweeted_file: str = 'tweeted'
    # ログ出力の設定ファイル
    logging_config_file: str = 'logging_config.json'


settings = Settings()
