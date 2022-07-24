from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import false
from sqlalchemy.orm import Session
from fastapi import APIRouter
import datetime


from models import note as note_model
from models import db
from validation import note as note_schema
router = APIRouter()

@router.get("/notes",tags=["note"])
def get_notes(db: Session = Depends(db.get_db)):
    L_notes = db.query(note_model.Note).filter().all()
    return L_notes

@router.get("/note/{slug_url}",tags=["note"])
def get_note(slug_url:str,db: Session = Depends(db.get_db)):
    instance = db.query(note_model.Note).filter(
        note_model.Note.slug_url == slug_url 
    ).first()
    if not instance:
        return {
            'success':false,
            "err":'Not Found'
        }
    return instance

@router.get("/note-content/{slug_url}",tags=["note"])
def get_note(slug_url:str,db: Session = Depends(db.get_db)):
    instance = db.query(note_model.Note).filter(
        note_model.Note.slug_url == slug_url 
    ).first()
    if not instance:
        return {
            'success':false,
            "err":'Not Found'
        }
    return instance.content

@router.post("/insert-note",tags=["note"])
def create_note(item:note_schema.note,db: Session = Depends(db.get_db)):
    instance = note_model.Note(
        **item.__dict__,
        created_at = datetime.datetime.utcnow()+datetime.timedelta(hours=7),
        updated_at = datetime.datetime.utcnow()+datetime.timedelta(hours=7)
    )
    try:
        db.add(instance)
        db.commit()
        db.refresh(instance)
        return instance
    except Exception as e:
        return {
            "err":'%s'%e,
            'success':False
        }


@router.post("/update-note",tags=["note"])
def create_note(item:note_schema.note,db: Session = Depends(db.get_db)):
    instance = db.query(
        note_model.Note
    ).filter(
        note_model.Note.slug_url == item.slug_url 
    ).first()
    if not instance:
        return {
            'success':false,
            "err":'Not Found'
        }
    
    try:
        instance.content = item.content
        instance.slug_url = item.slug_url
        instance.updated_at = datetime.datetime.utcnow()+datetime.timedelta(hours=7)
        
        db.commit()
        db.refresh(instance)
        return instance
    except Exception as e:
        return {
            "err":'%s'%e,
            'success':False
        }