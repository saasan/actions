import logging
import os
import time
from settings import settings


def setup_logger(name):
    """loggerを設定"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # 標準エラー出力のハンドラをINFOレベルで作成
    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)
    sh_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', '%Y-%m-%d %H:%M:%S')
    sh.setFormatter(sh_formatter)
    logger.addHandler(sh)

    # 上位ロガーには送らない
    logger.propagate = False

    return logger


def main():
    # loggerを設定
    logger = setup_logger(__name__)

    logger.info('feed_url: ' + settings.feed_url)
    logger.info('twitter_api_key: ' + settings.twitter_api_key)
    logger.info('twitter_api_secret_key: ' + settings.twitter_api_secret_key)
    logger.info('tweeted_filename: ' + settings.tweeted_filename)

    dir = os.path.dirname(os.path.abspath(__file__))
    logger.info('dir: ' + dir)

    with open(os.path.join(dir, settings.tweeted_filename)) as f:
        logger.info('appstate: ' + f.read())

    unixtime = str(int(time.time()))
    logger.info('new appstate: ' + unixtime)

    with open(settings.tweeted_filename, mode='w') as f:
        f.write(unixtime)


if __name__ == '__main__':
    main()
