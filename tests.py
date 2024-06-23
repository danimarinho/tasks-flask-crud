import pytest
import requests


#definindo as variáveis que vou testar
BASE_URL = "http://127.0.0.1:5000"
tasks = [] #todas as tarefas criadas serão add na lista para testar no futuro

#CRUD
#CREATE - vai testar a criação de uma atividade
def test_create_task():
    new_task_data = { #dados ficticios da atividade criada
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa"
    }

    #vai enviar a requisição, json vai enviar o dado que eu quero - o post responde um objeto.
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data) #

    #assert - verificar / validar o status. se o status code for 200 deu tudo certo neste caso
    assert response.status_code == 200

    #recuperar a resposta do servidor - vai ser 0 corpo do retorno, vou verificar se existe a message e se existe o id
    response_json = response.json()

    assert "message" in response_json
    assert "id" in response_json
    
    #adicionar o id na lista de tasks criado
    tasks.append(response_json["id"])


#READ - TESTE DE LEITURA
#Recuperar TODAS as atividades cadastradas
def test_get_tasks():
    #enviar requisição GET na url
    response = requests.get(f"{BASE_URL}/tasks")
    
    assert response.status_code == 200 #validação
    
    response_json = response.json() #este método vai trazer o corpo da resposta
    assert "tasks" in response_json #validação
    assert "total_tasks" in response_json #validação


#Recuperar uma tarefa específica
def test_get_task():
    #usar a lista task criada anteriormente
    if tasks:
        task_id  = tasks[0] #pegar a 1ª atividade criada, 1º posicao do id     
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")  #enviar a url com o id na requisição GET
       
        assert response.status_code == 200  #fazer as condições/recuperações - status_code e id
       
        response_json = response.json() #este método vai trazer o corpo da resposta
        
        #comparar se o task_id é igual ao identificador que estou tesntando recuperar (response_json['id'])
        assert task_id == response_json["id"]