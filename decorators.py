import functools
import logging

logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

def any_error(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        try:
            print("asidşlasidlaisşl")
            func(*args,**kwargs)
            logger.info(f"{func.__name__}  : f{error}")

        except Exception as error:
            logger.error(f"{func.__name__}  : f{error}")

    return wrapper