import logging, coloredlogs

# Instance for logging y que incluya el nombre del servidor
logger=logging.getLogger(__name__)

# Install of colored logs
coloredlogs.install(level='DEBUG', logger=logger)

logger.debug("Hi Keepcoders")

# Funcion que recibe un parámetro que es number (<> tipo number)
def add_one(number):
    return number+1

print(add_one(3))