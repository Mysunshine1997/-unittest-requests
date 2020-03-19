# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 14:19
# @Author  : Mysunshine
# @File    : test.py
import os
import logging
from logging.handlers import TimedRotatingFileHandler

path = os.path.dirname(os.path.dirname(__file__))
log_path = path.join(path, 'result')


class Logger(object):
    def __init__(self, logger_name='logs...'):
        self.logger = logging.getLogger(logger_name)
        # 设置日志等级
        logging.root.setLevel(logging.NOTSET)
        # 日志的文件名称
        self.log_file_name = 'test.log'
        # 最多存放日志个数
        self.backup_count = 5
        # 日志输出级别
        self.console_output_level = 'WARNING'
        self.file_output_level = 'DEBUG'
        # 日志输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def get_logger(self):
        """在logger中添加句柄并返回，如果logger已有句柄，则直接返回"""
        # 避免重复句柄
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(log_path, self.log_file_name), when ='D',
                                                    interval=1, backupCount=self.backup_count, delay=True,
                                                    encoding='utf-8')
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger


logger = Logger().get_logger()
