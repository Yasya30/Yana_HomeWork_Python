from sqlalchemy.orm import Session
from models import Student


def create_student(db: Session, first_name: str, last_name: str, email: str):
    student = Student(
        first_name=first_name,
        last_name=last_name,
        email=email
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def get_student_by_email(db: Session, email: str):
    return db.query(Student).filter(Student.email == email).first()


def update_student_email(db: Session, student_id: int, new_email: str):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        student.email = new_email
        db.commit()
        db.refresh(student)
    return student


def delete_student(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
    return student
