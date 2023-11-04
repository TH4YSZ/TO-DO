

class DAO:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def adicionar_tarefa(self, tarefa):
        with open(self.arquivo, 'a') as Arquivo:
            Arquivo.write(tarefa)
    
    def excluir_tarefa(self, excluir):
        with open(self.arquivo, 'w') as arquivo:
            for s, i, t in tarefas:
                    Arquivo.write(f"{s}\t{i}\t{t}\n")
            return True
                    
    
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

    def AlterarTarefa():
        pass


            