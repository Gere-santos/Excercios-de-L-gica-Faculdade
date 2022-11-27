inicioTabuada = int(input())
fimTabuada = int(input())

i = 1
cont = inicioTabuada

if(inicioTabuada > fimTabuada):
    print("Nenhuma tabuada no intervalo!")

while(inicioTabuada <= fimTabuada):
    while(i <= 10):
        print(cont,"x",i,"=",inicioTabuada*i)
        i += 1
    print("----------")
    inicioTabuada += 1
    i = 1
    cont += 1