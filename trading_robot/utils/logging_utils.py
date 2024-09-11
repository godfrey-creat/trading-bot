import logging

def setup_logger(name, log_file, level=logging.INFO):
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

# Example usage
# logger = setup_logger('trading_bot', 'bot/trading_bot.log')
# logger.info("Bot started")
