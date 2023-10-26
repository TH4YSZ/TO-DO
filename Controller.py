from Model import *

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):
        self.tarefa = tarefa
    
        try:
            if self.tarefa == " " or self.tarefa == "":
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
            if tarefa[0] == "STATUS " or tarefa[0] == "\n" or tarefa[0] == "STATUS":
                pass
            else:
                # print(tarefa[3])
                print(tarefa)
            
            cont += 1

class ControllerAlterarTarefa():
    def __init__(self, indice, alterar):
        indice = int(alterar)
        self.alterar = indice

    # try:
    #     if self.alterar >= 0 and self.alterar < len(TODO.ListarTarefas()):
    #         tarefa_alterada = TODO.AlterarTarefa(self.alterar) 
    #         if tarefa_alterada:
    #             print(f" VOCÊ ESTÁ ALTERANDO : {tarefa_alterada}")
    #             novaTarefa = input("DIGITE A ALTERAÇÃO >>")
    #             tarefa_alterada = tarefa_alterada.replace(tarefa[i], novaTarefa)
    #         else:
    #             print("Algum problema foi encontrado ao tentar alterar a tarefa.")
    #     else:
    #         print("Índice inválido. Certifique-se de que o índice indicado existe.")
    # except Exception as erro:
    #     print("Erro:", type(erro).__name__)
        
            
class ControllerConcluirTarefa():
    def __init__(self, indice):
        self.indice = indice

        TODO.concluir_tarefa(self.indice)
        
# class Listar_tarefasC():
#     def __init__(self):
#         if self.tarefas == tarefa_concluida:
#             print(f"A tarefa: {self.tarefa} foi Concluída")
        
            
#         tarefas = [tarefa.split("\t",) for tarefa in tarefas ]