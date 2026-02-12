from sqlalchemy.orm import Session
from models import Contribution

def create_contribution(db: Session, user_id: int, category: str, type: str, file_path: str):
    db_contribution = Contribution(user_id=user_id, category=category, type=type, file_path=file_path)
    db.add(db_contribution)
    db.commit()
    db.refresh(db_contribution)
    return db_contribution