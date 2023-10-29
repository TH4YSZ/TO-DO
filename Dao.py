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
        tasks = []
        with open(self.arquivo, 'r') as arquivo:
            lines = arquivo.readlines()
            for line in lines:
                if '\t' not in line:
                    continue
                status, id, task = line.split('\t', 2)
                tasks.append((status.strip(), id.strip(), task.strip()))
        return tasks



            