class Task:
    #construtor
    #id, title, description - atributos
    def __init__(self, id, title, description, completed=False) -> None:
        self.id = id #definindo atributos passando o self
        self.title = title
        self.description = description
        self.completed = completed


    #metodo para retornar o que tem armazenado em dicionario
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed  
        }
  