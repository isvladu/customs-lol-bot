import logging

from bot.customs_bot import CustomsBot

if __name__ == '__main__':
    logger = logging
    logger.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                       level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S')

    bot = CustomsBot()
    bot.run()
