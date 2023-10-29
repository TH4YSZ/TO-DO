from Controller import *
import os

sair = False

while sair == False:
    os.system("cls")
    print("SOFTWARE DE TO-DO \n")
    menu = input("[1] Adicionar tarefa\n[2] Listar tarefas \n[3] Alterar tarefa \n[4] Concluir tarefa \n[5] Listar tarefas concluídas \n[6] Excluir tarefa \n[7] Sair \n \nDigite a opção desejada: ")
    match menu:
        case "1":
            os.system("cls")
            print("-- ADICIONAR TAREFA ---\n")
            tarefa = input("Adicione uma tarefa: ")
            addTarefa = ControllerAdicionarTarefa(tarefa)
            os.system("pause")
            
        case "2":
            os.system("cls")
            print("--- LISTAR TAREFAS ---\n")
            listarTarefa = ControllerListarA()
            print("")
            os.system("pause")
            os.system("cls") 
        
        case "3":
            os.system("cls")
            print("--- ALTERAR TAREFA ---\n")
            listarTarefa = ControllerListarTarefa()
            alt = input("Digite o ID da tarefa que deseja alterar: ")
            print("")
            os.system("pause")
            os.system("cls") 
        
        case "4":
            os.system("cls")
            print("--- CONCLUIR TAREFA ---\n")
            listarTarefa = ControllerListarA()
            clr = input("Digite o ID da tarefa que deseja concluir: ")
            concluir_tarefa = ControllerConcluirTarefa(clr)
            print("")
            os.system("pause")
            os.system("cls") 

        case "5":
            os.system("cls")
            print("--- LISTAR TAREFAS CONCLUÍDAS ---\n")
            listarC = ControllerListarC()
            print("")
            os.system("pause")
            os.system("cls") 

        case "6":
            os.system("cls")
            print("--- EXCLUIR TAREFA ---\n")
            listarTarefa = ControllerListarTarefa()
            excluir = input("\nDigite o índice da tarefa que deseja excluir: ")
            excluirTarefa = ControllerExcluirTarefa(excluir)
            os.system("pause")
            os.system("cls")

        case "7":
            sair = True
            
        case _:
            print("\nOpção inválida.")
            os.system("pause")