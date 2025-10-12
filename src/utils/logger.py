import logging
import sys

def get_logger(name=__name__, log_file=None):
    
    """
    Escoger dónde se van a guardar mis logs (un archivo de extensión .log)
        Ejemplo: a un archivo
            file_handler = logging.FileHandler("my_program.log")
            logger.addHandler(file_handler)
        Ejemplo: a un archivo y a la consola
            logger.debug("Starting Division!")
            file_handler = logging.FileHandler("calculator.log")
            logger.addHandler(file_handler)
            stream_handler = logging.StreamHandler(sys.stdout)
    Tambien hay que escoger cuáles logs se muestran en la consola y cuáles se guardan.
    Formatear los logs
        Ejemplo de formatting:
            formatter = logging.Formatter("[%(asctime)s] %(levelname)s:%(name)s:%(lineno)d:%(message)s")
            stream_handler.setFormatter(formatter)
            logger.addHandler(stream_handler)
            logger.warning("This is a warning!")
                Salida:
                    [2021-11-04 02:58:51,847] WARNING:script:This is a warning!
    Definir el nivel de los logs
    NOTA: log level for development -> DEBUG
            Log level after deploying -> WARNING
    """
    logger = logging.getLogger(name)

    if logger.hasHandlers():
        logger.handlers.clear()


    stream_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(stream_handler)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    stream_handler.setFormatter(formatter)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    stream_handler.setLevel(logging.WARNING)
    file_handler.setLevel(logging.DEBUG)


    return logger
