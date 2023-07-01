import json
import logging
import logging.config
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
    # ログ出力の設定
    logger = setup_logger(__name__)

    try:
        with open(settings.tweeted_file, 'r') as f:
            logger.info('old tweeted: ' + f.read())
    except FileNotFoundError:
        logger.info('old tweeted: File Not Found')

    unixtime = str(int(time.time()))
    logger.info('new tweeted: ' + unixtime)

    with open(settings.tweeted_file, mode='w') as f:
        f.write(unixtime)


if __name__ == '__main__':
    main()
