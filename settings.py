from pydantic import BaseSettings


class Settings(BaseSettings):
    # RSSフィードのURL
    feed_url: str
    # Twitter API Key
    twitter_api_key: str
    # Twitter API Secret Key
    twitter_api_secret_key: str
    # Twitter Access Token
    twitter_access_token: str
    # Twitter Access Token Secret
    twitter_access_token_secret: str

    # ツイート済みエントリーの日時を書き込むファイル名
    tweeted_filename: str = 'appstate'
    # ツイート済みエントリーの日時が保存されていない場合にツイートする最大数
    untweeted_max_num: int = 3
    # URLを除いたツイートの最大文字数
    max_tweet_char: int = 128


settings = Settings()
