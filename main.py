import json
import logging
import logging.config
import time
from settings import settings


def setup_logger(name: str) -> logging.Logger:
    """ログ出力の設定"""
    with open(settings.logging_config_file, encoding='utf-8') as f:
        logging_config = json.load(f)
    logging.config.dictConfig(logging_config)
    logger = logging.getLogger(name)

    return logger


def main():
    # ログ出力の設定
    logger = setup_logger(__name__)

    logger.info('feed_url: ' + settings.feed_url)
    logger.info('twitter_api_key: ' + settings.twitter_api_key)
    logger.info('twitter_api_secret_key: ' + settings.twitter_api_secret_key)
    logger.info('tweeted_filename: ' + settings.tweeted_filename)

    with open(settings.tweeted_filename) as f:
        logger.info('appstate: ' + f.read())

    unixtime = str(int(time.time()))
    logger.info('new appstate: ' + unixtime)

    with open(settings.tweeted_filename, mode='w') as f:
        f.write(unixtime)


if __name__ == '__main__':
    main()
