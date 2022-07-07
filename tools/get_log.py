import logging.handlers
import os

from config import BASE_PATH


class GetLog:
    __log = None

    @classmethod
    def get_log(cls):
        if cls.__log is None:
            # 获取日志器
            cls.__log = logging.getLogger()
            # 修改默认级别
            cls.__log.setLevel(logging.INFO)
            log_path = BASE_PATH + os.sep + "log" + os.sep + "tt.log"
            # 获取处理器
            th = logging.handlers.TimedRotatingFileHandler(filename=log_path, when="midnight", interval=1,
                                                           backupCount=3, encoding="utf-8")
            # 获取格式器
            fmt = " %(asctime)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器中
            th.setFormatter(fm)
            #             将处理器添加到日志器中
            cls.__log.addHandler(th)
        # 返回日志器
        return cls.__log


# if __name__ == '__main__':
#     log=GetLog().get_log()
#     log.info('测试信息级别')
#     log.error("测试错误级别")
