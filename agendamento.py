# relação de dias da semana que cada médico atende
medicos = {
'cardiologista' :['terca', 'quarta'],
'ortopedista': ['terca', 'quinta'], 
'dermatologista':['segunda', 'quarta', 'sexta'],
'neurologista':['terca', 'quinta', 'sexta'],
'psiquiatra':['segunda', 'quarta', 'sexta']
}
# Calcula quais os dias possíveis para dois médicos

def disponibilidade_dois(medico1, medico2):

    dias = (set(medico1).intersection(set(medico2)))
    if dias:
        print(dias)
    else:
        print("Não é possível obter as duas especialidades em um dia")
     
# Calcula quais os dias possíveis para três médicos
def disponibilidade_tres(medico1, medico2, medico3):
    dias = (set(medico1).intersection(set(medico2))).intersection(set(medico3))
    if dias:
        print(dias)
    else:
        print("Não é possível obter as três especialidades em um dia")

def main():

    print("Escolha a opção: \n 1 - Duas especialidades \n 2 - Três especialidades")

    escolha = int(input())
    if escolha == 1:
        escolha_dois()
    elif escolha == 2:
        escolha_tres()
    else:
        print("Valor inválido, tente novamente")
        main()

def escolha_dois():
    print("Escolha a opção com as especialidades desejadas")
    print("1 - cardiologista e ortopedista") 
    print("2 - cardiologista e dermatologista")
    print("3 - cardiologista e psiquiatra")
    print("4 - cardiologista e neurologista")
    print("5 - dermatologista e psiquiatra")
    print("6 - dermatologista e neurologista")
    print("7 - ortopedista e dermatologista")
    print("8 - ortopedista e neurologista")
    print("9 - ortopedista e psiquiatra")
    print("10 - neurologista e psiquiatra")

    opcao = int(input("Sua opção: "))

    if opcao == 1:

        disponibilidade_dois(medicos['cardiologista'], medicos['ortopedista'])

    elif opcao == 2:

        disponibilidade_dois(medicos['cardiologista'], medicos['dermatologista'])

    elif opcao == 3:

        disponibilidade_dois(medicos['cardiologista'], medicos['psiquiatra'])
    elif opcao == 4:

        disponibilidade_dois(medicos['cardiologista'], medicos['neurologista'])
    elif opcao == 5:

        disponibilidade_dois(medicos['dermatologista'], medicos['psiquiatra'])

    elif opcao == 6:

        disponibilidade_dois(medicos['dermatologista'], medicos['neurologista'])

    elif opcao == 7:

        disponibilidade_dois(medicos['ortopedista'], medicos['dermatologista'])

    elif opcao == 8:
         disponibilidade_dois(medicos['ortopedista'], medicos['neurologista'])


    elif opcao == 9:

         disponibilidade_dois(medicos['ortopedista'], medicos['psiquiatra'])

    elif opcao == 10:
         disponibilidade_dois(medicos['neurologista'], medicos['psiquiatra'])


def escolha_tres():
    print("Escolha a opção com as especialidades desejadas")
    print("1 - cardiologista, ortopedista e dermatologista") 
    print("2 - cardiologista, ortopedista e neurologista")
    print("3 - cardiologista, ortopedista e psiquiatra")
    print("4 - cardiologista, dermatologista e neurologista")
    print("5 - cardiologista, dermatologista e psiquiatra")
    print("6 - cardiologista, neurologista e psiquiatra")
    print("7 - ortopedista, dermatologista e neurologista")
    print("8 - ortopedista, dermatologista e psiquiatra")
    print("9 - ortopedista, neurologista e psiquiatra")
    print("10 - dermatologista, neurologista e psiquiatra")

    opcao = int(input("Sua opção: "))

    if opcao == 1:

        disponibilidade_tres(medicos['cardiologista'], medicos['ortopedista'], medicos['dermatologista'])

    elif opcao == 2:

        disponibilidade_tres(medicos['cardiologista'], medicos['ortopedista'], medicos['neurologista'])

    elif opcao == 3:

        disponibilidade_tres(medicos['cardiologista'], medicos['ortopedista'], medicos['psiquiatra'])
    elif opcao == 4:

        disponibilidade_tres(medicos['cardiologista'], medicos['dermatologista'], medicos['neurologista'])
    elif opcao == 5:

        disponibilidade_tres(medicos['cardiologista'], medicos['dermatologista'], medicos['psiquiatra'])

    elif opcao == 6:

        disponibilidade_tres(medicos['cardiologista'], medicos['neurologista'], medicos['psiquiatra'])

    elif opcao == 7:

        disponibilidade_tres(medicos['ortopedista'], medicos['dermatologista'], medicos['neurologista'])

    elif opcao == 8:

         disponibilidade_tres(medicos['ortopedista'], medicos['dermatologista'], medicos['psiquiatra'])

    elif opcao == 9:

         disponibilidade_tres(medicos['ortopedista'], medicos['neurologista'], medicos['psiquiatra'])

    elif opcao == 10:
         disponibilidade_tres(medicos['dermatologista'], medicos['neurologista'], medicos['psiquiatra'])

    else:
        print("Valor inválido")
        main()

if __name__ == "__main__":
    main()