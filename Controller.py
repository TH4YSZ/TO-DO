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
        self.excluir = int(excluir)

        tarefas = dao.Listar_tarefas()
        if 0 <= self.excluir < len(tarefas):
            status, id, descricao = tarefas[self.excluir]
            if status == "A" or status == "C":
                tarefas[self.excluir] = ("E", id, descricao)
                
                with open(dao.arquivo, 'w') as arquivo:
                    for s, i, t in tarefas:
                        arquivo.write(f"{s}\t{i}\t{t}\n")

                print(f"Tarefa excluída: {descricao}")
            else:
                print("Essa tarefa já foi excluída.")
        else:
            print("Índice inválido. Certifique-se de que o índice indicado existe.")


class ControllerListarTarefa():
    def __init__(self):
        tarefas = dao.Listar_tarefas()
        cont = 0
        for tarefa in tarefas:
            status, _, descricao = tarefa
            if status == "A":
                print(f"{cont}\t{descricao}")
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
        self.indice = int(indice)

        tarefas = dao.Listar_tarefas()
        if 0 <= self.indice < len(tarefas):
            status, id, descricao = tarefas[self.indice]
            if status == "A":
                tarefas[self.indice] = ("C", id, descricao)

                with open(dao.arquivo, 'w') as arquivo:
                    for s, i, t in tarefas:
                        arquivo.write(f"{s}\t{i}\t{t}\n")

                print(f"Tarefa Concluída: {descricao}")
            else:
                print("Essa tarefa já está concluída.")
        else:
            print("Índice inválido. Certifique-se de que o índice indicado existe.")
        
class ControllerListarC():
    def __init__(self):
        tarefas = dao.Listar_tarefas()
        cont = 0
        for tarefa in tarefas:
            status, _, descricao = tarefa
            if status == "C":
                print(f"{cont}\t{descricao}")
            cont += 1