array = []
array.sort()


valorAdicionar = input(str())
if(valorAdicionar != ""):
    stringQuebrar = valorAdicionar.split(" ")
    for i in stringQuebrar:
        array.append(int(i))

valordigitado = input(str())
textoadicionar = valordigitado[0:9]
numerotextoadicionar = valordigitado[10:]
nRemover = valordigitado[8:]
textoRemover = valordigitado[0:7]
textoExibir = valordigitado[0:6]




while (valordigitado != "encerrar"): 
    
    if(textoRemover == "remover"):
        nRemover = valordigitado[8:]
        textoRemover = valordigitado[0:8]
        if(int(nRemover) in array):
            
            array.remove(int(nRemover)) 
        else:
            print("código",nRemover,"não encontrado")
            
    elif(textoExibir == "exibir"):
        text = ""
        array.sort()
        for i in array:
            text += str(i) + " "
        print(text[:-1])

    elif(textoadicionar == "adicionar"):
        
        textoadicionar = valordigitado[0:9]
        numerotextoadicionar = valordigitado[10:]
        array.append(int(numerotextoadicionar))    
        
      
    
    valordigitado = input(str())
    textoadicionar = valordigitado[0:9]
    numerotextoadicionar = valordigitado[10:]
    nRemover = valordigitado[8:]
    textoRemover = valordigitado[0:7]
    textoExibir = valordigitado[0:6]
    textoEncerrar = valordigitado[0:8]

text = ""
array.sort()
for i in array:
    text += str(i) + " "
print(text[:-1])  