import logging, coloredlogs

logger = logging.getLogger(__name__)
coloredlogs.install(level="DEBUG", logger=logger)
logger.debug("Hola keepcoders")

def add_one(number):
    return number + 1

# def add_two(number):
#     return number + 2

print(add_one(3))
# print(add_two(3))