import logging
import inspect
import os


def logger(func, *, level=logging.DEBUG):
    def wrapper(*args, **kwargs):
        another_func = args[0]
        format = "%(asctime)s LEVEL: %(levelname)s MSG: %(message)s"
        logging.basicConfig(format=format, level=level)
        logger = logging.getLogger(__name__)
        current_path = os.path.dirname(__file__)
        file_name = f"{current_path}\logger_file.txt"
        file_handler = logging.FileHandler(file_name)
        logger.addHandler(file_handler)
        func_name = another_func.__name__
        signature = inspect.signature(another_func)
        params = list(signature.parameters.keys())
        logger.log(level=level,
                   msg=f"function {func_name}, with parameters: {params}", )
        # Call the original function with the given arguments
        return func(*args, **kwargs)

    return wrapper

