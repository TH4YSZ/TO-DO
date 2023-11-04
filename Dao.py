

class DAO:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.titulos_adicionados = False

    def adicionar_tarefa(self, tarefa):
        with open(self.arquivo, 'a') as Arquivo:
            if not self.titulos_adicionados:
                Arquivo.write("STATUS\tID\tTAREFA\n\n")
                self.titulos_adicionados = True
            Arquivo.write(tarefa)
    
    def excluir_tarefa(self, excluir):
        tarefass = self.Listar_tarefas()
        status, id, descricao = tarefass[excluir]
        tarefass[excluir] = ("E", id, descricao)
                    
        with open(self.arquivo, 'w') as arquivo:
            for s, i, t in tarefass:
                arquivo.write(f"{s}\t{i}\t{t}\n")
        return True
    
    def concluir_tarefa(self, concluir):
        tarefas = self.Listar_tarefas()
        status, id, descricao = tarefas[concluir]
        tarefas[concluir] = ("C", id, descricao)
                    
        with open(self.arquivo, 'w') as arquivo:
            for s, i, t in tarefas:
                arquivo.write(f"{s}\t{i}\t{t}\n")
        return True
    
    def Alterar_Tarefa(self, indice, new_tarefa):
        tarefass = self.Listar_tarefas()
        status, id, descricao = tarefass[indice]
        tarefass[indice] = (status, id, new_tarefa)

        with open(self.arquivo, 'w') as arquivo:
            for s, i, t in tarefass:
                arquivo.write(f"{s}\t{i}\t{t}\n")
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




            