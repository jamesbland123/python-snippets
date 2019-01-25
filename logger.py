""" Python logging.  Better than putting print statements everywhere """
import logging
logger = logging.getLogger()

def main():
    logger.debug('Debug')
    logger.info('Info')
    logger.warning('Warning')
    logger.error('Error')
    logger.critical('Critical')


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Set Log Level")
    parser.add_argument('-l', '--level', type=str,
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        default='DEBUG',
                        help='Set logging levels')
    
    args = parser.parse_args()
    logging.basicConfig(level=args.level)
    main()