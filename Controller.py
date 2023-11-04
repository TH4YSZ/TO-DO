from Model import *
import random

class ControllerAdicionarTarefa:
    def AdicionarTarefa(self, tarefa):
        self.tarefa = tarefa
        self.A = "A"
        id_salvos = []
        titulo_adicionado = False  

        try:
            id_tarefa = random.randint(1000, 9999)
            id_salvos.append(id_tarefa)

       
            if titulo_adicionado == False:
                add_titulo = f"Status\tID\tTarefa\n\n"
                if TODO.AdicionarTarefa(add_titulo) == True:
                    titulo_adicionado = True 

                if id_tarefa != id_salvos:
                    if self.tarefa == " " or self.tarefa == "":
                        print("Informe uma tarefa válida.")
                    else:
                        new_tarefa = f"{self.A}\t{id_tarefa}\t{self.tarefa}\n"
                        if TODO.AdicionarTarefa(new_tarefa) == True:
                            print("Tarefa adicionada!")
                        else:
                            print("Erro ao adicionar tarefa.")
                else:
                    id_tarefa = random.randint(1000, 9999)
            else:
                print("Algum problema foi encontrado ao tentar adicionar a tarefa.")

        except Exception as erro:
            print("Erro:", erro._class.name_)
        

class ControllerExcluirTarefa:
    def __init__(self, excluir):
        self.excluir = int(excluir)

        if self.excluir == " " or self.excluir == "":
            print("Informe um índice válido.")
        else:
            lista_tarefas = TODO.ListarTarefas()
            self.excluir_tarefa(tarefas)

    def excluir_tarefa(self, tarefas):
        if 0 <= self.excluir < len(lista_tarefas):
            status, id, descricao = tarefas[self.excluir]
            if status == "A" or status == "C":
                if TODO.ExcluirTarefa(self.excluir):
                    print(f"Tarefa excluída: {descricao}")
                else:
                    print("Erro ao excluir a tarefa.")
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
    def __init__(self, indice, new_tarefa):
        self.indice = int(indice)
        self.new_tarefa = new_tarefa
        
        tarefas = TODO.ListarTarefas()
        if self.indice == " " or self.indice == "":
            print("Informe um índice válido.")
        elif self.new_tarefa == " " or self.new_tarefa == "":
            print("Informe uma tarefa válida.")
        elif self.indice >= 0 and self.indice < len(tarefas):
            status, id, descricao = tarefas[self.indice]
            
            if status == "A":
                tarefas[self.indice] = (status, id, new_tarefa)
                
                with open(dao.arquivo, 'w') as arquivo:
                    for s, i, t in tarefas:
                        arquivo.write(f"{s}\t{i}\t{t}\n")
                
                print(f"Tarefa alterada: {descricao} -> {new_tarefa}")
            else:
                print("Não é possível alterar tarefas concluídas.")
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

controlleradd = ControllerAdicionarTarefa()