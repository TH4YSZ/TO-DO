from Model import *
import random

class ControllerAdicionarTarefa:
    def AdicionarTarefa(self, tarefa):
        self.tarefa = tarefa
        self.A = "A"
        id_salvos = []


        try:
            id_tarefa = random.randint(1000, 9999)
            id_salvos.append(id_tarefa)

            if id_tarefa != id_salvos:
                if self.tarefa == " " or self.tarefa == "":
                    print("Informe uma tarefa válida.")
                else:
                    new_tarefa = f"{self.A}\t{id_tarefa}\t{self.tarefa}\n"
                    if TODO.AdicionarTarefa(new_tarefa):
                        print("Tarefa adicionada!")
                    else:
                        print("Erro ao adicionar tarefa")
            else:
                id_tarefa = random.randint(1000, 9999)

        except Exception as erro:
            print("Erro:", erro._class.name_)
        

class ControllerExcluirTarefa:
    def __init__(self, excluir):
        self.excluir = int(excluir)
        tarefass = TODO.ListarTarefas()

        try:
            if self.excluir == " " or self.excluir == "":
                print("Informe um índice válido.")
            elif 0 <= self.excluir < len(tarefass):
                status, id, descricao = tarefass[self.excluir]
                if status == "A":
                    if TODO.ExcluirTarefa(self.excluir) == True:
                        print(f"Tarefa excluída: {descricao}")
                    else:
                        print("Tarefa não encontrada.")
                else:
                    print("Essa tarefa já foi excluída.")
            else:
                print("Índice inválido. Certifique-se de que o índice indicado existe.")
        except Exception as erro:
            print("Erro:", erro._class.name_)


class ControllerAlterarTarefa:
    def __init__(self, indice, new_tarefa):
        self.indice = int(indice)
        self.new_tarefa = new_tarefa
        
        try:
            tarefas = TODO.ListarTarefas()
            if self.indice == " " or self.indice == "":
                print("Informe um índice válido.")
            elif self.new_tarefa == " " or self.new_tarefa == "":
                print("Informe uma tarefa válida.")
            elif self.indice >= 0 and self.indice < len(tarefas):
                status, id, descricao = tarefas[self.indice]
                if status == "A":
                    if TODO.AlterarTarefa(self.indice, self.new_tarefa) == True:
                        print(f"Tarefa alterada: {descricao} -> {new_tarefa}")
                    else:
                        print("Tarefa não encontrada.")
                else:
                    print("Não é possível alterar tarefas concluídas.")
            else:
                print("Índice inválido. Certifique-se de que o índice indicado existe.")
        except Exception as erro:
            print("Erro:", erro._class.name_)
            

class ControllerConcluirTarefa():
    def __init__(self, indice):
        self.indice = int(indice)
        tarefass = TODO.ListarTarefas()

        try:
            if self.indice == " " or self.indice == "":
                print("Informe um índice válido.")
            elif 0 <= self.indice < len(tarefass):
                status, id, descricao = tarefass[self.indice]
                if status == "A":
                    if TODO.concluir_tarefa(self.indice) == True:
                        print(f"Tarefa concluída: {descricao}")
                    else:
                        print("Tarefa não encontrada.")
                else:
                    print("Essa tarefa já foi concluída.")
            else:
                print("Índice inválido. Certifique-se de que o índice indicado existe.")
        except Exception as erro:
            print("Erro:", erro._class.name_)
        

class ControllerListarTarefa:
    def __init__(self, status):
        tarefas = TODO.ListarTarefas()
        cont = 0
        for tarefa in tarefas:
            tarefa_status, _, descricao = tarefa
            if tarefa_status == status:
                print(f"{cont}\t{descricao}")
            cont += 1



controlleradd = ControllerAdicionarTarefa()