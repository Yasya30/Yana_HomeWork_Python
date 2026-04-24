import pytest
from api.projects_api import ProjectsAPI


class TestProjectsAPI:

    # ==================== POST /api-v2/projects ====================

    def test_create_project_positive(self, projects_api):
        """Позитивный тест: создание проекта с валидными данными"""
        project_title = "Мой первый проект"
        response = projects_api.create_project(project_title)

        assert response.status_code == 201
        response_data = response.json()
        assert "id" in response_data
        
        # Проверяем, что проект действительно создался с правильным названием
        project_id = response_data.get("id")
        get_response = projects_api.get_project(project_id)
        assert get_response.status_code == 200
        assert get_response.json().get("title") == project_title

    def test_create_project_negative_missing_title(self, projects_api):
        """Негативный тест: создание проекта без обязательного поля title"""
        response = projects_api.create_project(title=None)

        assert response.status_code == 400
        response_data = response.json()
        assert "error" in response_data or "message" in response_data

    # ==================== PUT /api-v2/projects/{id} ====================

    def test_update_project_positive(self, projects_api):
        """Позитивный тест: обновление названия проекта"""
        # Сначала создаём проект
        create_response = projects_api.create_project("Старое название")
        assert create_response.status_code == 201
        project_id = create_response.json().get("id")

        # Обновляем название
        new_title = "Новое название"
        update_response = projects_api.update_project(project_id, title=new_title)

        assert update_response.status_code == 200
        
        # Проверяем, что название обновилось
        get_response = projects_api.get_project(project_id)
        assert get_response.status_code == 200
        assert get_response.json().get("title") == new_title

    def test_update_project_negative_invalid_id(self, projects_api):
        """Негативный тест: обновление проекта с несуществующим ID"""
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = projects_api.update_project(fake_id, title="Новое название")

        assert response.status_code == 404
        response_data = response.json()
        assert "error" in response_data or "not found" in response.text.lower()

    # ==================== GET /api-v2/projects/{id} ====================

    def test_get_project_positive(self, projects_api):
        """Позитивный тест: получение проекта по ID"""
        # Создаём проект
        create_response = projects_api.create_project("Проект для получения")
        assert create_response.status_code == 201
        project_id = create_response.json().get("id")

        # Получаем проект по ID
        response = projects_api.get_project(project_id)

        assert response.status_code == 200
        response_data = response.json()
        assert response_data.get("id") == project_id
        assert response_data.get("title") == "Проект для получения"

    def test_get_project_negative_not_found(self, projects_api):
        """Негативный тест: получение проекта по несуществующему ID"""
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = projects_api.get_project(fake_id)

        assert response.status_code == 404
        
        