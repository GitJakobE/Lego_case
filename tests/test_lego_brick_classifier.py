from pathlib import Path

from pytest import fixture
import pandas as pd

from lego_brick_classifier import LegoBrickClassifier
from constants import MODEL_PATH

@fixture
def training_df():
    df = pd.DataFrame(data={'weights': [1.0, 1.1, 1.0, 2, 2, 1.8, 5, 6, 7, 8, 9, 10],
                            'color_id': [1, 1, 1, 2, 3, 2, 7, 8, 9, 10, 11, 12],
                            'brick_id': [1, 1, 1, 2, 2, 2, 7, 8, 9, 10, 11, 12]})
    return df


def test_load_save_model() -> None:
    """saves a model deletes it and loads it again with cleanup"""
    identifier = LegoBrickClassifier()
    identifier.save_model()
    identifier.nearest_neighbor_model = None
    identifier.load_model()
    assert identifier.nearest_neighbor_model is not None
    Path(MODEL_PATH).unlink()
    assert not Path(MODEL_PATH).exists()


def test_train_model(training_df) -> None:
    """tests that we are able to train a model with the two attributes"""
    training_df.to_csv("test_dataset.csv", index_label=False)
    identifier = LegoBrickClassifier()
    identifier.train_model(dataset_path="test_dataset.csv")
    assert identifier.nearest_neighbor_model.predict([[2.1, 2]]) == [2]
    Path("test_dataset.csv").unlink()


def test_predict(training_df) -> None:
    training_df.to_csv("test_dataset.csv", index_label=False)
    identifier = LegoBrickClassifier()
    identifier.train_model(dataset_path="test_dataset.csv")
    assert identifier.predict(1, 1) is not None
    Path("test_dataset.csv").unlink()