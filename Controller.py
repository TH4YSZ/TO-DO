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

        tarefass = TODO.ListarTarefas()


        if self.excluir == " " or self.excluir == "":
            print("Informe um índice válido.")
        elif 0 <= self.excluir < len(tarefass):
            status, id, descricao = tarefass[self.excluir]
            if status == "A" or status == "C":
                tarefass[self.excluir] = ("E", id, descricao)
                    
                with open(dao.arquivo, 'w') as arquivo:
                    for s, i, t in tarefass:
                        arquivo.write(f"{s}\t{i}\t{t}\n")

                print(f"Tarefa excluída: {descricao}")
            else:
                print("Essa tarefa já foi excluída.")
        else:
            print("Índice inválido. Certifique-se de que o índice indicado existe.")

class ControllerListarA():
    def __init__(self):
        tarefas = TODO.ListarTarefas()
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

        if self.alterar == " " or self.alterar == "":
                print("Informe um índice válido.")
        elif self.alterar >= 0 and self.alterar < len(TODO.ListarTarefas()):
            tarefa_alterada = TODO.AlterarTarefa(self.alterar) 
            if tarefa_alterada:
                print(f" VOCÊ ESTÁ ALTERANDO : {tarefa_alterada}")
                novaTarefa = input("DIGITE A ALTERAÇÃO >>")
                tarefa_alterada = tarefa_alterada.replace(tarefa[i], novaTarefa)
            else:
                print("Algum problema foi encontrado ao tentar alterar a tarefa.")
        else:
            print("Índice inválido. Certifique-se de que o índice indicado existe.")
    
        
            
class ControllerConcluirTarefa():
    def __init__(self, indice):
        self.indice = int(indice)

        tarefas = TODO.ListarTarefas()
     
        if self.indice == " " or self.indice == "":
            print("Informe um índice válido.")
        elif 0 <= self.indice < len(tarefas):
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
        tarefas = TODO.ListarTarefas()
        cont = 0
        for tarefa in tarefas:
            status, _, descricao = tarefa
            if status == "C":
                print(f"{cont}\t{descricao}")
            cont += 1

class ControllerListarTarefa():
    def __init__(self):
        tarefas = TODO.ListarTarefas()
        cont = 0
        for tarefa in tarefas:
            status, _, descricao = tarefa
            if status == "A" or status == "C":
                print(f"{cont}\t{descricao}")
            cont += 1
