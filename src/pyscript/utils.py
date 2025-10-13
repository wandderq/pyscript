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

# def setup_logger(name: str) -> lg.Logger:
#     """Setups logger and returns it"""
#     logger = lg.getLogger(name)
#     logger.setLevel(lg.DEBUG)
    
#     stream_handler = lg.StreamHandler(stream=sys.stdout)
#     stream_formatter = clg.ColoredFormatter(
#         fmt="{log_color}[{name} - {levelname}]: {message}{reset}",
#         style='{',
#         log_colors={
#             'debug': 'white',
#             'info': 'green',
#             'warning': 'yellow',
#             'error': 'red',
#             'critical': 'red',
            
#         }
#     )
#     stream_handler.setFormatter(stream_formatter)
#     logger.addHandler(stream_handler)
    
#     return logger
    # filename = os.path.join(.EXEC_DIR, f'logs/{}.log')
    # os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # file_handler = lg.FileHandler(filename=filename, mode='a')
    # file_formatter = lg.Formatter(
    #     "[{name} - {levelname} at {asctime}]: {message}",
    #     style='{',
    #     datefmt="%H:%M:%S"
    # )
    # file_handler.setFormatter(file_formatter)
    
    # logger.addHandler(file_handler)

def printf(text: str) -> None:
    sys.stdout.write(text + '\n')
    sys.stdout.flush()