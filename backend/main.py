from fastapi import FastAPI, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import User, Contribution
import crud

Base.metadata.create_all(bind=engine)
app = FastAPI(title="FinEx API", version="0.1")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint upload contribution
@app.post("/contributions/")
def upload_contribution(user_id: int, category: str, type: str, file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        file_location = f"uploads/{file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())

        contribution = crud.create_contribution(db, user_id=user_id, category=category, type=type, file_path=file_location)
        return {"msg": "Contribution uploaded", "id": contribution.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))