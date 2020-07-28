import logging  # python字典
from hoopytestapiproject.tools import project_path
from hoopytestapiproject.tools.get_data import GetData


class MyLog:

    def my_log(self, msg, level):
        Info = GetData().get_info_for_log()
        my_logger = logging.getLogger(Info)
        my_logger.setLevel('DEBUG')

        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')
        ch.setFormatter(formatter)
        fh = logging.FileHandler(project_path.log_path, encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)

        my_logger.addHandler(ch)
        my_logger.addHandler(fh)
        # 收集日志
        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)

        # 关闭渠道
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log(msg, 'DEBUG')

    def info(self, msg):
        self.my_log(msg, 'INFO')

    def error(self, msg):
        self.my_log(msg, 'ERROR')

    def critical(self, msg):
        self.my_log(msg, "CRITICAL")

    def warning(self, msg):
        self.my_log(msg, "WARNING")
