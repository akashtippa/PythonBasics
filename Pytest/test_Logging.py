import logging


def test_logging():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logsfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)  # file handler object

    logger.setLevel(logging.DEBUG)

    logger.debug("A Debug statement executed")
    logger.info("Information statement")
    logger.warning("something is in warning mode")
    logger.error("A Major error has happend")
    logger.critical("Critical Issue")
