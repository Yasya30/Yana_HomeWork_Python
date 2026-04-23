import pytest
from api.projects_api import ProjectsAPI


@pytest.fixture
def projects_api():
    """Фикстура для работы с API проектов"""
    return ProjectsAPI()


@pytest.fixture
def create_test_project(projects_api):
    """Фикстура для создания тестового проекта"""
    response = projects_api.create_project("Тестовый проект для API")
    assert response.status_code == 201, "Не удалось создать тестовый проект"
    project_id = response.json().get("id")
    yield project_id
    