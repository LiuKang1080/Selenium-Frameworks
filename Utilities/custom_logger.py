import logging
import inspect


def custom_logger(log_level, log_name=None):
    """
    Create a custom logger with custom.log file.
    :param log_level: Default log level for specific log.
    :param log_name: Specific name of the log. (Default = automation.log)
    :return:
    """

    # Gets the name of the class / method from where this method is called from
    logger_name = inspect.stack()[1][3]

    if log_name is None:
        logger = logging.getLogger(logger_name)
    else:
        logger = logging.getLogger(log_name)

    logger.setLevel(logging.DEBUG)

    if log_name is None:
        file_handler = logging.FileHandler('Automation.log', mode='a')
    else:
        file_handler = logging.FileHandler('{0}.log'.format(log_name))

    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S.%p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
