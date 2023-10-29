import random

class DAO:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.ids_salvos = []
        self.id = random.randint(1000, 9999)
        self.titulos_adicionados = False
        self.A = "A"

    def adicionar_tarefa(self, tarefa):
        with open(self.arquivo, 'a') as Arquivo:
            if not self.titulos_adicionados:
                Arquivo.write("STATUS\tID\tTAREFA\n\n")
                self.titulos_adicionados = True

            while True:
                self.id = random.randint(1000, 9999)
                if self.id not in self.ids_salvos:
                    True
                    break

            Arquivo.write(f"{self.A}\t{self.id}\t{tarefa}\n")
    
        self.ids_salvos.append(self.id)
    
    def Listar_tarefas(self): 
        tarefas = []
        with open(self.arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                if '\t' not in linha:
                    continue
                status, id, tarefa = linha.split('\t', 2)
                tarefas.append((status.strip(), id.strip(), tarefa.strip()))
        return tarefas



            