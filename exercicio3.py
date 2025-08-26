#Exercicio 3: Determinar o signo do zodíaco com base na data de nascimento

# Passo 1: Pegar as informações
dia = int(input("Digite o dia (1-31): "))       
mes = int(input("Digite o mês (1-12): "))

# Passo 2: Verificar em qual signo está a data informada
if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
    signo = "Áries"
elif (mes == 4 and dia >= 21) or (mes == 5 and dia <= 20):
    signo   = "Touro"
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    signo = "Gêmeos"                        
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 21):  
    signo = "Câncer"
elif (mes == 7 and dia >= 22) or (mes == 8 and dia <= 22):
    signo = "Leão"
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    signo = "Virgem"
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    signo = "Libra"             
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    signo = "Escorpião"     
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    signo = "Sagitário"
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 20):
    signo = "Capricórnio"
elif (mes == 1 and dia >= 21) or (mes == 2 and dia <= 19):
    signo   = "Aquário"
elif (mes == 2 and dia >= 20) or (mes == 3 and dia <= 20):
    signo   = "Peixes"
elif (mes >12 or mes<1 ) or (dia >31 or dia < 1):
    signo = "Data inválida"         
else:
    signo = "Data inválida"

# Passo 3: Imprimir o resultado
print(f"A data {dia}/{mes} está no signo: {signo}")    

# Exemplo de entrada e saída:
# Entrada:                      Saída:
# Dia: 15                        A data 15/3 está no signo: Peixes
# Mês: 3                    (se a data for 15/3)
# Hora: 14
# Minutos: 30       


