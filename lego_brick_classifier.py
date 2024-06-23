import pickle
from typing import Union
from pathlib import Path

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

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

    def load_model(self) -> None:
        if Path("nearest_neighbor_model.pkl").exists():
            with open('nearest_neighbor_model.pkl', 'rb') as f:
                self.nearest_neighbor_model = pickle.load(f)

    def save_model(self) -> None:
        with open('nearest_neighbor_model.pkl', 'wb') as f:
            pickle.dump(self.nearest_neighbor_model, f)

    def train_model(self, dataset_path: str) -> None:
        # TODO: should be cleaned up before
        train_df = pd.read_csv(dataset_path)
        y = train_df["brick_id"]
        x = train_df.drop(["brick_id"], axis=1)

        self.nearest_neighbor_model.fit(x, y)


    def run(self) -> None:
        """
        predicts the brick id from the "data" and sends it to the database
        """
        dataset = pd.DataFrame([self.color_id, self.weight])
        self.nearest_neighbor_model.predict(dataset)
