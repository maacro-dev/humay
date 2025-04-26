import logging

logger = logging.getLogger("humay")
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(name)s:     >> %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
