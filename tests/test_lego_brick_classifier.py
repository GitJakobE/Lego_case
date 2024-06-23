from pathlib import Path

import pandas as pd

from lego_brick_classifier import LegoBrickClassifier


def test_load_save_model() -> None:
    """saves a model deletes it and loads it again with cleanup"""
    identifier = LegoBrickClassifier()
    identifier.save_model()
    identifier.nearest_neighbor_model = None
    identifier.load_model()
    assert identifier.nearest_neighbor_model is not None
    Path("nearest_neighbor_model.pkl").unlink()
    assert not Path("nearest_neighbor_model.pkl").exists()


def test_train_model() -> None:
    df = pd.DataFrame(data={'weights': [1.0, 1.1, 1.0, 2, 2, 1.8, 5, 6, 7, 8, 9, 10],
                            'color_id': [1, 1, 1, 2, 3, 2, 7, 8, 9, 10, 11, 12],
                            'brick_id': [1, 1, 1, 2, 2, 2, 7, 8, 9, 10, 11, 12]})
    df.to_csv("test_dataset.csv", index_label=False)
    identifier = LegoBrickClassifier()
    identifier.train_model(dataset_path="test_dataset.csv")
    assert identifier.nearest_neighbor_model.predict([[2.1, 2]]) == [2]
    Path("test_dataset.csv").unlink()