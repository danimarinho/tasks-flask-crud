from flask import Flask #importando o Flask

app = Flask(__name__) #variavel name é o nome do arquivo - se executar de forma manual( do desenvolvimento local) a variavel será chamada __main__

#criar uma rota - vai conseguir comunicar com outros clientes. receber e devolver informacoes
@app.route("/") #rota inicial
def hello_world(): #funcao
  return "Hello world!"


@app.route("/about") #definindo outra rota
def about():
  return "Página sobre"

if __name__ == "__main__": #vai executar só em modo manual, do desenvolvimento local
  app.run(debug=True) #executar o programa - debug ajuda a ver as informações


