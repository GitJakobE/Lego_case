from loguru import logger
import pickle
from typing import Union
from pathlib import Path

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

from common.constants import MODEL_PATH
from schemas import LegoPiece


class LegoBrickClassifier:
    """
    Class to identify a lego piece from an image, a weight and a color.
    """

    def __init__(self) -> None:
        self.image = None
        self.weight = None
        self.color_id = None

        self.piece: Union[LegoPiece, None] = None

        self.nearest_neighbor_model = KNeighborsClassifier(metric='manhattan', n_neighbors=3, weights='distance')
        self.load_model()

    def load_model(self, filename: str = MODEL_PATH) -> None:
        logger.debug(f"Loading model from {filename}")
        if Path(filename).exists():
            with open(filename, 'rb') as f:
                self.nearest_neighbor_model = pickle.load(f)
        else:
            logger.warning(f"No model found at {filename}")

    def save_model(self, filename: str = MODEL_PATH) -> None:
        logger.debug(f"Saving model to {filename}")
        with open(filename, 'wb') as f:
            pickle.dump(self.nearest_neighbor_model, f)

    def train_model(self, dataset_path: str) -> None:
        # TODO: data should be cleaned up before
        logger.info("Starting to train model")
        train_df = pd.read_csv(dataset_path)
        y = train_df["brick_id"]
        x = train_df.drop(["brick_id"], axis=1)

        self.nearest_neighbor_model.fit(x, y)
        logger.info("Model trained")

    def predict(self, weight: float, color_id: int) -> int:
        """
        predicts the brick id from the data
        """
        return self.nearest_neighbor_model.predict([[weight, color_id]])[0]
