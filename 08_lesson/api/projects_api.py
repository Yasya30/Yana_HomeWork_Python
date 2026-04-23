from .client import YougileClient


class ProjectsAPI:
    """API методы для работы с проектами"""

    def __init__(self):
        self.client = YougileClient()

    def create_project(self, title, users=None, guests=None):
        """
        [POST] /api-v2/projects - создание проекта
        Обязательные поля: title
        """
        data = {"title": title}
        if users:
            data["users"] = users
        if guests:
            data["guests"] = guests
        return self.client.post("/api-v2/projects", data)

    def update_project(self, project_id, title=None, users=None, guests=None):
        """
        [PUT] /api-v2/projects/{id} - обновление проекта
        """
        data = {}
        if title:
            data["title"] = title
        if users:
            data["users"] = users
        if guests:
            data["guests"] = guests
        return self.client.put(f"/api-v2/projects/{project_id}", data)

    def get_project(self, project_id):
        """
        [GET] /api-v2/projects/{id} - получение проекта по ID
        """
        return self.client.get(f"/api-v2/projects/{project_id}")
    