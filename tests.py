import pytest
import requests


#definindo as variáveis que vou testar
BASE_URL = "http://127.0.0.1:5000"
tasks = [] #todas as tarefas criadas serão add na lista para testar no futuro

#CRUD
def test_create_task():
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa"
    }

    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)

    assert response.status_code == 200

    response_json = response.json()

    assert "message" in response_json
    assert "id" in response_json

    tasks.append(response_json["id"])