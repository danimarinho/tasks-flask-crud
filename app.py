from flask import Flask, request, jsonify #importando o Flask
from models.task import Task

app = Flask(__name__) #variavel name é o nome do arquivo - se executar de forma manual( do desenvolvimento local) a variavel será chamada __main__


# CRUD
# Create, Read, Update and Delete = Criar, Ler, Atualizar, Deletar
# Tabela: Tarefa (tasks)

tasks = [] #as tarefas estarão armazenadas aqui nesta lista, já que ainda não temos um banco de dados. Vamos cruar uma classe para este bd
task_id_control = 1

#criar uma rota - vai conseguir comunicar com outros clientes. receber e devolver informacoes
"""@app.route("/") #rota inicial
def hello_world(): #funcao
  return "Hello world!
  """

@app.route('/tasks', methods=['POST'])
def create_task(): #FUNCAO RESPONSAVEL POR CRIAR A ATIVIDADE
#receber as informacoes do cliente
  global task_id_control #para acessar a variavel fora do metodo, ela deve ser criada dentro do metodo como glkoba
  
  data = request.get_json() #vai recurar o que o cliente enviou
#request vem do Flask - importar
#metodo get_json() vai recuperar o que o cliente enviou e vai atribuir à variável data
  
  #criar uma nova task a partir da classe
  #requisito obrigatorio pode acessar direto, sem, uisar o get =>  title=data.get("title") = title=data["title"]
  new_task = Task(id=task_id_control, title=data.get("title"), description=data.get("description",""))
  task_id_control += 1
  tasks.append(new_task)
  print(tasks)
  #IMPORTAR o jsonify para o print da resposta
  return jsonify({"message": "Nova tarefa criada com sucesso."})


#CRUD- ROUTE READ - GET
@app.route('/tasks', methods=['GET'])
def get_tasks(): #Vai retornar todas as atividades
  task_list = [task.to_dict()  for task in tasks] #o metodo to_dict() vai retornar a lista no formato de dicionario - utilizando o for na mesma linha; #For dentro da lista vai criar a lista com os elementos que tem dentro do tasks, porém executand o to_dict(). + elegante, simpes, economia de tempo/tempo.
  
  #len() - conta quantos elementos tem na lista
  output = {
            "tasks": task_list,
            "total_tasks": len(task_list)
           }
  
  return jsonify(output)



#CRUD- ROUTE READ - GET específico
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
  for t in tasks:
    if t.id == id:
      return jsonify(t.to_dict())

  return jsonify({"messagem": "Não foi possível encontrar a atividade"}, 404)














if __name__ == "__main__": #vai executar só em modo manual, do desenvolvimento local
  app.run(debug=True) #executar o programa - debug ajuda a ver as informações


