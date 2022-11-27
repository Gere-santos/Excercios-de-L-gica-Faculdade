array = []

cont = 1
qtdlinhas = int(input())

while(cont<=qtdlinhas<=200):
     entradaDados = str(input())
     array.append(entradaDados)
     cont += 1
    
cont2 = 0
valorPremium = float(input())
valorNaoPremium = float(input())

print("-----\n"
    "BÔNUS\n"
    "-----")

while(cont2 < len(array)):
    
    stringquebrada = array[cont2].split(';') 
    nomeCanal = str(stringquebrada[0])
    moneyMesAnterior = float(stringquebrada[2])
    nDeInscritos = int(stringquebrada[1])
    premiumOuNao = str(stringquebrada[-1])
    divisaoTrucada = nDeInscritos // 1000
    if(premiumOuNao == "sim" and divisaoTrucada >= 1):
        valorBonus = (divisaoTrucada * valorPremium) + moneyMesAnterior
        print(str(nomeCanal) + ': R$ ' + str('{:.2f}'.format(valorBonus)))
    elif(premiumOuNao == "não" and divisaoTrucada >= 1):
        valorBonus = (divisaoTrucada * valorNaoPremium) + moneyMesAnterior
        print(str(nomeCanal) + ': R$ ' + str('{:.2f}'.format(valorBonus))) 
    else:
        print(str(nomeCanal) + ': R$ ' + str('{:.2f}'.format(moneyMesAnterior)))
    cont2 += 1
 