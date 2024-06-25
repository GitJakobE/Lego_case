import datetime as dt
import numpy as np

from pydantic import BaseModel, ConfigDict


class LegoColor(BaseModel):
    id: int
    name: str
    color_hex: str
    in_production: bool


class LegoPiece(BaseModel):
    id: int
    name: str
    weight: float
    color_id: LegoColor
    cad_drawing: str
    in_production: bool


class LegoSet(BaseModel):
    id: int
    name: str
    description: str
    pieces: list[LegoPiece] = []
    in_production: bool
    validation_image: np.ndarray

    model_config = ConfigDict(arbitrary_types_allowed=True)


class ProductionLine(BaseModel):
    id: int
    lego_piece: LegoPiece
    image: np.ndarray
    time_stamp: dt.datetime

    model_config = ConfigDict(arbitrary_types_allowed=True)
