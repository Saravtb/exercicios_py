# Exercício 2: Determinar a estação do ano com base na data e hora

# Passo 1: Pegar as informações
dia = int(input("Digite o dia (1-31): "))
mes = int(input("Digite o mês (1-12): "))
hora = int(input("Digite a hora (0-23): "))
minutos = int(input("Digite os minutos (0-59): "))

# Passo 2: Verificar em qual estação está a data e hora informadas
if (mes == 12 and dia >= 21 and hora >= 12 and minutos >= 3) or (mes in [1, 2]) or (mes == 3 and dia <= 20 and hora <= 6 and minutos < 1):
    estacao = "Verão"
elif (mes == 3 and dia >= 20 and hora>= 6  and minutos >= 1) or (mes in [4, 5]) or (mes == 6 and dia <= 20 and hora <= 23 and minutos < 42):
    estacao = "Outono"
elif (mes == 6 and dia >= 20 and hora>= 23 and minutos >= 42 ) or (mes in [7, 8]) or (mes == 9 and dia <= 22 and hora <= 15 and minutos < 19):
    estacao = "Inverno"
elif (mes >12 or mes<1 ) or (dia >31 or dia < 1):
    estacao = "Data inválida"
elif (hora >23 or hora <0) or (minutos >59 or minutos <0):
    estacao = "Hora inválida"
else:
    estacao = "Primavera"

# Passo 3: Imprimir o resultado
print(f"A data {dia}/{mes} ás {hora}h{minutos} está na estação: {estacao}")

# Exemplo de entrada e saída:
# Entrada:                      Saída:
# Dia: 15                        A data 15/3 ás 14h30 está na estação: Outono
# Mês: 3                    (se a data for 15/3)                                        
# Hora: 14
# Minutos: 30   



