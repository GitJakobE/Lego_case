from pydantic import BaseModel


class LegoPiece(BaseModel):
    id: int
    name: str
    weight: float
    color: str
    cad_drawing: str
    in_production: bool


class LegoSet(BaseModel):
    id: int
    name: str
    description: str
    pieces: list[LegoPiece] = []
    in_production: bool
