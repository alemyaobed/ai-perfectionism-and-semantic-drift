def setup_logging(log_file='app.log'):
    import logging

    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def log_info(message):
    import logging
    logging.info(message)

def log_warning(message):
    import logging
    logging.warning(message)

def log_error(message):
    import logging
    logging.error(message)

def log_debug(message):
    import logging
    logging.debug(message)