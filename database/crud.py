# mocked
# All the calls to the database
from sqlalchemy.orm import Session

from . import db_models
from schemas import LegoColor


def get_color(db: Session, color_id: int):
    res = db.query(db_models.LegoColor).filter(db_models.LegoColor.id == color_id).first()
    if res is None:
        raise ValueError("Color id not found")
    return LegoColor(**db.query(db_models.LegoColor).filter(db_models.LegoColor.id == color_id).first().__dict__())
