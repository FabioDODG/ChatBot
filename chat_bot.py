# Projeto de chat bot de agendamentos de consultas médicas.
medicos = {'Cardiologista': 1, 'Dermatologista': 2, 'Ginecologista': 3, 'Urologista': 4 , 'Endocrinologista': 5}

especialidades = {'Cardiologista': '(Doutora) Renata Damico.', 'Dermatologista': '(Doutora) Juliana Dias', 'Ginecologista':
                  '(Doutora) Letícia Moura', 'Urologista': '(Doutor) Jefferson Nunes', 'Endocrinologista': '(Doutor) Marcio Costa'
                 }

dias_de_funcionamento = {'Cardiologista': 'Agenda: segundas e terças de 6:00 ás 11:00 / 13:00 ás 18:00.',
                         'Dermatologista': 'Agenda: segundas e quartas de 8:00 ás 11:00 / 14:00 ás 19:00.',
                         'Ginecologista': 'Agenda: terças e quintas de 6:00 ás 12:00 / 14:00 ás 17:00.',
                         'Urologista': 'Agenda: quartas e sextas de 6:00 ás 10:00 / 13:00 ás 16:00.',
                         'Endocrinologista': 'Agenda: segundas e sextas de 7:00 ás 11:00 / 13:00 ás 18:00.'
                        }
#print(especialidades)

print('''
Escolha a modalidade que deseja marcar consulta. 
[1] Cardiologista.
[2] Dermatologista.
[3] Ginecologista.
[4] Urologista.
[5] Endocrinologista.
''')


resposta_certa1 = False
resposta_certa2 = False
resposta_certa3 = False

while not resposta_certa1:
    escolha_modalidade= int(input("Digite sua escolha: "))
    if (1<= escolha_modalidade <=5):
        if escolha_modalidade == 1:
            print(especialidades['Cardiologista'], dias_de_funcionamento['Cardiologista'])
            print("Digite o dia e horário que deseja marcar a consulta.")
            while not resposta_certa2:
                dia1 = input("Digite o dia que deseja: ").lower()
                if dia1 == "segunda" or dia1 =="terca":
                    resposta_certa2 = True
                    while not resposta_certa3:
                        hora1 = int(input("Digite a hora que deseja: "))
                        if (6 <= hora1 <= 11) or (13 <= hora1 <= 18):
                            print("Consulta marcada para {} ás {}.".format(dia1, hora1))
                            resposta_certa3 = True
                            resposta_certa1 = True
                        else:
                            print("Digite a hora correta para marcar a consulta. ")
                else:
                    print("Digite o dia correto para poder marcar a consulta.")
                  
            
        if escolha_modalidade == 2:
          print(especialidades['Dermatologista'],dias_de_funcionamento['Dermatologista'])
          print("Digite o dia e horário que deseja marcar a consulta.")
          while not resposta_certa2:
              dia2 = input("Digite o dia que deseja: ").lower()
              if dia2 == "segunda" or dia2 =="quarta":
                resposta_certa2 = True
                while not resposta_certa3:
                  hora2 = int(input("Digite a hora que deseja: "))
                  if (8 <= hora2 <= 11) or (14 <= hora2 <= 19):
                      print("Consulta marcada para {} ás {}.".format(dia2, hora2))
                      resposta_certa3 = True
                      resposta_certa1 = True
                  else:
                      print("Digite a hora correta para marcar a consulta. ")
              else:
                  print("Digite o dia correto para poder marcar a consulta. ")

                
        if escolha_modalidade == 3:
                 print(especialidades['Ginecologista'],dias_de_funcionamento['Ginecologista'])
                 print("Digite o dia e horário que deseja marcar a consulta.")
                 while not resposta_certa2:
                     dia3 = input("Digite o dia que deseja: ").lower()
                     if dia3 == "terca" or dia3 =="quinta":
                       resposta_certa2= True
                       while not resposta_certa3:
                         hora3 = int(input("Digite a hora que deseja: "))
                         if (6 <= hora3 <= 12) or (14 <= hora3 <= 17):
                            print("Consulta marcada para {} ás {}.".format(dia3, hora3))
                            resposta_certa3 = True 
                            resposta_certa1 = True
                         else:
                            print("Digite a hora correta para marcar a consulta. ")
                     else:
                       print("Digite o dia correto para poder marcar a consulta. ")

                       
        if escolha_modalidade == 4:
                print(especialidades['Urologista'], dias_de_funcionamento['Urologista'])
                print("Digite o dia e horário que deseja marcar a consulta.")
                while not resposta_certa2:
                    dia4 = input("Digite o dia que deseja: ").lower()
                    if dia4 == "quarta" or dia4 =="sexta":
                        resposta_certa2 = True
                        while not resposta_certa3:
                          hora4 = int(input("Digite a hora que deseja: "))
                          if (6 <= hora4 <= 10) or (13 <= hora4 <= 16):
                              print("Consulta marcada para {} ás {}.".format(dia4, hora4))
                              resposta_certa3 = True
                              resposta_certa1 = True
                          else:
                              print("Digite a hora correta para marcar a consulta. ")
                    else:
                      print("Digite o dia correto para poder marcar a consulta. ")

                      
        if escolha_modalidade == 5:
                    print(especialidades['Endocrinologista'],dias_de_funcionamento['Endocrinologista'])
                    print("Digite o dia e horário que deseja marcar a consulta.")
                    while not resposta_certa2:
                        dia5 = input("Digite o dia que deseja: ").lower()
                        if dia5 == "segunda" or dia5 =="sexta":
                          resposta_certa2 = True
                          while not resposta_certa3:
                            hora5 = int(input("Digite a hora que deseja: "))
                            if (7 <= hora5 <= 11) or (13 <= hora5 <= 18):
                                print("Consulta marcada para {} ás {}.".format(dia5, hora5))
                                resposta_certa3 = True
                                resposta_certa1 = True
                            else:
                                print("Digite a hora correta para marcar a consulta. ")
                        else:
                          print("Digite o dia correto para poder marcar a consulta.")                 
        
    else:
      print("Digite o número do médico novamente")
      