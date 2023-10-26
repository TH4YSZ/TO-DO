from Model import *

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):
        self.tarefa = tarefa
    
        try:
            if self.tarefa == " " or self.tarefa == "":
                print("Informe uma tarefa válida")
            elif self.tarefa == int:
                print("Informe uma tarefa válida")
            else:
                if TODO.AdicionarTarefa(self.tarefa) == True:
                    print("Tarefa Adicionada!")
                else:
                    print("Algum problema foi encontrado ao tentar adicionar a tarefa.")
        except Exception as erro:
            print("Erro:", erro._class.name_)
        


class ControllerExcluirTarefa():
    def __init__(self, excluir):
        indice = int(excluir)
        self.excluir = indice - 1 

        try:
            if self.excluir >= 0 and self.excluir < len(TODO.ListarTarefas()):
                tarefa_removida = TODO.ExcluirTarefa(self.excluir) 
                if tarefa_removida:
                    print(f"Tarefa Excluída: {tarefa_removida}")
                else:
                    print("Algum problema foi encontrado ao tentar excluir a tarefa.")
            else:
                print("Índice inválido. Certifique-se de que o índice indicado existe.")
        except Exception as erro:
            print("Erro:", type(erro).__name__)


class ControllerListarTarefa():
    def __init__(self):
        tarefas = TODO.ListarTarefas()
        cont = 1
        
        for tarefa in tarefas:
            if tarefa == "":
                pass
            else:
                print(tarefa)
            cont += 1

            print(tarefa)