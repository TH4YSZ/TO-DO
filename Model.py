from Dao import *

dao = DAO("Tarefa.txt")

class ToDo():    

    def AdicionarTarefa(self, tarefa):
        dao.adicionar_tarefa(tarefa)
        return True

    def ExcluirTarefa(self, excluir):
        return dao.excluir_tarefa(excluir)

    def ListarTarefas(self):
        return dao.Listar_tarefas()

    def AlterarTarefa(self, indice, new_tarefa):
        return dao.Alterar_Tarefa(indice, new_tarefa)

    def concluir_tarefa(self, concluir):
        dao.concluir_tarefa(concluir)
    
        
        

TODO = ToDo()