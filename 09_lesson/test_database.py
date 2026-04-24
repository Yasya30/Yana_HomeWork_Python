import pytest
from sqlalchemy.exc import IntegrityError
from crud import create_student, get_student_by_email, update_student_email, delete_student


class TestStudentDatabase:

    # ==================== ТЕСТ НА ДОБАВЛЕНИЕ ====================

    def test_create_student_positive(self, db_session):
        """Позитивный тест: создание студента"""
        email = "ivan.petrov@example.com"
        student = create_student(
            db_session,
            first_name="Иван",
            last_name="Петров",
            email=email
        )

        assert student.id is not None
        assert student.first_name == "Иван"
        assert student.last_name == "Петров"
        assert student.email == email

        # Проверяем, что студент действительно сохранился в БД
        found = get_student_by_email(db_session, email)
        assert found is not None
        assert found.id == student.id

    def test_create_student_negative_duplicate_email(self, db_session):
        """Негативный тест: создание студента с дублирующимся email"""
        email = "duplicate@example.com"

        # Создаём первого студента
        create_student(db_session, "Первый", "Студент", email)

        # Пытаемся создать второго с тем же email
        with pytest.raises(IntegrityError):
            create_student(db_session, "Второй", "Студент", email)
        db_session.rollback()  # Откатываем после ошибки

    # ==================== ТЕСТ НА ИЗМЕНЕНИЕ ====================

    def test_update_student_email_positive(self, db_session):
        """Позитивный тест: обновление email студента"""
        # Создаём студента
        old_email = "old@example.com"
        new_email = "new@example.com"
        student = create_student(
            db_session,
            first_name="Для",
            last_name="Обновления",
            email=old_email
        )

        # Обновляем email
        updated = update_student_email(db_session, student.id, new_email)

        assert updated.email == new_email
        assert updated.id == student.id

        # Проверяем, что в БД действительно обновилось
        found = get_student_by_email(db_session, new_email)
        assert found is not None
        assert found.id == student.id

    def test_update_student_email_negative_not_found(self, db_session):
        """Негативный тест: обновление email несуществующего студента"""
        fake_id = 999999
        result = update_student_email(db_session, fake_id, "fake@example.com")
        assert result is None

    # ==================== ТЕСТ НА УДАЛЕНИЕ ====================

    def test_delete_student_positive(self, db_session):
        """Позитивный тест: удаление студента"""
        # Создаём студента
        email = "to_delete@example.com"
        student = create_student(
            db_session,
            first_name="На",
            last_name="Удаление",
            email=email
        )
        student_id = student.id

        # Удаляем
        deleted = delete_student(db_session, student_id)

        assert deleted is not None
        assert deleted.id == student_id

        # Проверяем, что студента больше нет в БД
        found = get_student_by_email(db_session, email)
        assert found is None

    def test_delete_student_negative_not_found(self, db_session):
        """Негативный тест: удаление несуществующего студента"""
        fake_id = 999999
        result = delete_student(db_session, fake_id)
        assert result is None
        