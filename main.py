import csv
from time import sleep
from colorama import Fore

def main():

    qt = input("Nova adição ao arquivo? (Y/N): ")
    qt = qt.upper()

    if qt == 'Y':
        new_marks()
    else:
        read_marks()
    
    exits = input("Press any key to exit...")

def new_marks():
    what_is()
    sleep(1)

    linha = Fore.GREEN + '\n' + '-' * 70 + Fore.WHITE

    question_1 = input("Situação de Humor: ")
    print(linha)
    question_2 = input("Estado de Humor: ")
    print(linha)
    question_3 = input("Pensamento Automatico (P.A): ")
    print(linha)
    question_4 = input("Evidencias que apoiam o P.A: ")
    print(linha)
    question_5 = input("Evidencias que NÃO apoiam o P.A: ")
    print(linha)
    question_6 = input("Pensamentos alternativos\nCompensatorios\nConclusão: ")
    print(linha)
    question_7 = input("Avalie o estado de humor: ")
    print(linha)

    print("Saving...")
    
    with open('consulta.csv', 'a', newline='') as csv_file:
        fieldnames = ["situacao", "estado_humor","pa" ,"e.p.a", "e.n.p.a", "pensamentos_alternativos",
                      "avaliacao_humor"]
        csv_file = csv.DictWriter(csv_file, fieldnames=fieldnames)

        csv_file.writerow({'situacao' : question_1, 
                            'estado_humor' : question_2,
                            'pa' : question_3,
                            'e.p.a' : question_4,
                            'e.n.p.a': question_5, 
                            'pensamentos_alternativos' : question_6,
                            'avaliacao_humor' : question_7})
    
    sleep(2)
    print("Finish")

def read_marks():
    with open('consulta.csv', 'r', newline='') as csv_reader:
        
        linha = Fore.GREEN + '\n' + '-' * 70 + Fore.WHITE

        csv_reader = csv.DictReader(csv_reader, delimiter=',')
        for row in csv_reader:
            print("#" * 100 + "\n\n")
            print(linha)
            print(f"Situação: {row['situacao']} {linha}")
            print(f"Estado de Humor: {row['estado_humor']} {linha}")
            print(f"Pensamento Automatico: {row['pa']} {linha}")
            print(f"Evidencias que apoião o PA: {row['e.p.a']} {linha}")
            print(f"Evidencias que NÃO apoião o PA: {row['e.n.p.a']} {linha}")
            print(f"Pensamentos Alternativos: {row['pensamentos_alternativos']} {linha}")
            print(f"Estado de Humor após: {row['avaliacao_humor']} {linha}")

def what_is():
    print()
    print(Fore.GREEN + "Situação: Com quem você estava? O que estava fazendo? Quando foi? Onde foi?")
    print()
    print("Estado de humor: Descreva com uma palavra a sua emoção. Avalie a intensidade 0-100%")
    print()
    print("Pensamento Automatico: ")
    print("O que estava passando pela minha cabeça antes de começar a me sentir desse modo? O que isso diz")       
    print("ao meu respeito? O que significa em relação a mim, à minha vida e meu futuro? O que de pior pode")
    print("acontecer se isso for verdade? O que significa em termos do modo como as outras pessoas pensam a ")
    print("meu respeito? O que isso significa em relação às outras pessoas? Que imagens ou lembranças eu tenho") 
    print("desta situação?")
    print()
    print("Evidencias que apoiam o PA:")
    print("Escreva evidências factuais para apoiar seu pensamento (Evite leitura de pensamentos ou interpretações de fatos)")
    print()
    print("Evidencias que NÃO apoia o PA: ")
    print("Escreva evidências factuais que não apoiam seu pensamento (Evite leitura de pensamentos ou interpretações de fatos)")
    print()
    print("Pensamentos Alternativos: ")
    print("Escreva um pensamento alternativo a partir da conclusão das evidências (colunas anteriores).")
    print("Quanto você acredita no pensamento alternativo? 0-100%") 
    print("Dica: o que você diria para um amigo passando por essa situação?")
    print()
    print("Avalie o Humor: ")
    print("Copie os sentimentos da segunda coluna e reavalie a intensidade 0-100% Como sente agora?" + Fore.WHITE)
    print()

if __name__ == '__main__':
    main()