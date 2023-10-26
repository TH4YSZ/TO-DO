import random

class DAO:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.ids_salvos = []
        self.id = random.randint(1000, 9999)
        self.titulos_adicionados = False

    def adicionar_tarefa(self, tarefa):
        with open(self.arquivo, 'a') as Arquivo:
            if not self.titulos_adicionados:
                Arquivo.write("----------------\nID \t\t TAREFA\n\n")
                self.titulos_adicionados = True

            while True:
                self.id = random.randint(1000, 9999)
                if self.id not in self.ids_salvos:
                    True
                    break

            Arquivo.write(f"{self.id} \t {tarefa}\n")
    
        self.ids_salvos.append(self.id)
    
    def Listar_tarefas(self): 
        with open('tarefa.txt', 'r') as arquivo:
            tarefas = arquivo.readlines()
    
        tarefas = [tarefa.strip() for tarefa in tarefas]

        return tarefas