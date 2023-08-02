import logging
import inspect

def extract_info(another_func, *, level=logging.DEBUG):
    def decorator(func):
        def wrapper(*args, **kwargs):
            format = "%(asctime)s LEVEL: %(levelname)s MSG: %(message)s"
            logging.basicConfig(format=format, level=level)
            logger = logging.getLogger(__name__)

            file_name = "logger.txt"
            file_handler = logging.FileHandler(file_name)
            logger.addHandler(file_handler)
            func_name = another_func.__name__
            signature = inspect.signature(another_func)
            params = list(signature.parameters.keys())
            logger.log(level=level, msg=f"Name of another_func: {func_name}, with parameters of another_func: {params}",)
            # Call the original function with the given arguments
            return func(*args, **kwargs)

        return wrapper

    return decorator


