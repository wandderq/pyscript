import logging as lg
import colorlog as clg
import sys

def setup_logger(name: str) -> lg.Logger:
    """Setups logger and returns it"""
    logger = lg.getLogger(name)
    
    if logger.handlers:
        logger.handlers.clear()
    
    logger.setLevel(lg.INFO)
    
    stream_handler = lg.StreamHandler(stream=sys.stdout)
    stream_formatter = clg.ColoredFormatter(
        fmt="{log_color}[{name} - {levelname}]: {message}",
        style='{',
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        },
        secondary_log_colors={}
    )
    stream_handler.setFormatter(stream_formatter)
    logger.addHandler(stream_handler)
    
    return logger


def printf(text: str) -> None:
    sys.stdout.write(text + '\n')
    sys.stdout.flush()