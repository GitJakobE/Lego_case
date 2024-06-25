from loguru import logger
from lego_brick_classifier import LegoBrickClassifier


def main():
    logger.info("Reads in the config")
    logger.info("Starts a UI")

    logger.info("Starts a number of threads to round robin the processes")
    # This could run a thread to start a round robin series to get weight and the color
    # Instead we will run it only once
    identifier = LegoBrickClassifier()
    logger.info("Recognition")
    brick_id = identifier.predict(weight=10.2, color_id=20)
    logger.info("Sorting of LEGO bricks into specific sets")


# Run the program
if __name__ == '__main__':
    main()
