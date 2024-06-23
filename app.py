from flask import Flask, request, jsonify #importando o Flask
from models.task import Task #pasta models, arquivo task

app = Flask(__name__) #variavel name é o nome do arquivo - se executar de forma manual( do desenvolvimento local) a variavel será chamada __main__


# CRUD
# Create, Read, Update and Delete = Criar, Ler, Atualizar, Deletar
# Tabela: Tarefa (tasks)

tasks = [] #as tarefas estarão armazenadas aqui nesta lista, já que ainda não temos um banco de dados. Vamos criar uma classe para este bd
task_id_control = 1

#criar uma rota - vai conseguir comunicar com outros clientes. receber e devolver informacoes
"""@app.route("/") #rota inicial
def hello_world(): #funcao
  return "Hello world!
  """

#metodo route para definir as rotas
@app.route('/tasks', methods=['POST'])
def create_task(): #FUNCAO RESPONSAVEL POR CRIAR A ATIVIDADE; #receber as informacoes do cliente
  global task_id_control #para acessar a variavel fora do metodo, ela deve ser criada dentro do metodo como glkoba
  
  data = request.get_json() #vai recuperar o que o cliente enviou
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
  #encontrar o recurso dentro da lista atraves do for
  #t cada atividade que tem dentro do meu tasks

  for t in tasks:
    if t.id == id:
      return jsonify(t.to_dict())

  return jsonify({"message": "Não foi possível encontrar a atividade"}, 404)


#parametros de rota 
'''
@app.route('/user/<username>')
def show_user(username):
  print(username)
  print(type(username))
  return username

@app.route('/user/<int:user_id>')
def show_user(user_id):
  print(user_id)
  print(type(user_id))
  return "%s" % user_id

@app.route('/user/<float:number>')
def show_user(number):
  print(number)
  print(type(number))
  return "%s" % number        

@app.route('/user/<path:number>fdfdgfgf')
def show_user(number):
  print(number)
  print(type(number))
  return "%s" % number    
'''

#CRUD- ROUTE UPDATE - atualizar
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
  task = None
  for t in tasks:
    if t.id == id:
      task = t
      break
    
  print("MENSAGEM1: ", task)

  if task == None:
    return jsonify({"message": "Não foi possível encontrar a tarefa"}), 404

  data = request.get_json()  #vai recuperar o que o cliente enviou
#request vem do Flask - importar
#metodo get_json() vai recuperar o que o cliente enviou e vai atribuir à variável data
  task.title        = data["title"]
  task.description  = data["description"]
  task.completed    = data["completed"]
  print("MENSAGEM 2: ", task)
  return jsonify({"message": "Tarefa atualizada com sucesso"})

#CRUD- ROUTE DELETE - DELETAR
@app.route('/tasks/<int:id>', methods=["DELETE"])
def delete_task(id):
  task = None
  for t in tasks: #percorrer a lista de atividades para verificar se existe ou nao o identificador 
    print(t.to_dict())
    if t.id == id:
      task = t
      break

  if not task: #igual if task == None
    return jsonify({"message": "Não foi possível encontrar a tarefa"}), 404  

  tasks.remove(task)
  return jsonify({"message": "Tarefa deletada com sucesso"})

if __name__ == "__main__": #vai executar só em modo manual, do desenvolvimento local
  app.run(debug=True) #executar o programa - debug ajuda a ver as informações


