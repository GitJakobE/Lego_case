import numpy as np
from loguru import logger
from .lego_brick_classifier import LegoBrickClassifier


def main():
    logger.info("Reads in the config")
    logger.info("Starts a UI")

    logger.info("Starts a number of threads to round robin the processes")
    # This could run a thread to start a round robin series to get the images and weights
    identifier = LegoBrickClassifier(image=np.zeros((400, 400, 3)), weigh=10.2, color_id=20)
    identifier.run()
    logger.info("Intelligently automates the scanning")

    logger.info("Recognition")

    logger.info("Sorting of LEGO bricks into specific sets")


# Run the program
if __name__ == '__main__':
    main()
