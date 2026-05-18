import logging


def get_logger(name: str = "paleo_futura") -> logging.Logger:
    """Return a basic configured logger."""
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
    return logging.getLogger(name)
