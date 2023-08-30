import logging
import time
import random
import notify

message_list = []  # 存储消息数据


def init_logger():
    """
    初始化日志系统

    :return:
    """
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    log_format = logging.Formatter(
        '%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s: %(message)s'
    )

    # Console
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(log_format)
    log.addHandler(ch)


def random_delay():
    """
    生成10秒到10分钟之间的随机延迟时间

    :return:
    """
    delay = random.uniform(10, 600)
    time.sleep(delay)


def info_message(message_content):
    """
    成功日志输出

    :param message_content:
    :return:
    """
    logging.info(f"🎈{message_content}")
    message(f"🎈{message_content}")


def error_message(message_content):
    """
    失败日志输出

    :param message_content:
    :return:
    """
    logging.error(f"😢{message_content}")
    message(f"😢{message_content}")


def message(message_content):
    """
    日志和消息放在一起

    :param message_content:
    :return:
    """
    message_list.append(message_content)


def send_notify(title):
    """
    发送通知

    :param title:
    :return:
    """
    msg = '\n'.join(message_list)
    notify.send(title, msg)


def init():
    """
    延迟时间和日志初始化

    :return:
    """
    # 随机延迟
    random_delay()
    # 初始化日志
    init_logger()
