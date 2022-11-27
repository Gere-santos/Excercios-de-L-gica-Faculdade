nAlunos = int(input())

arrayNotaOriginal = []
arrayNovaNota = []

vControle = nAlunos * 2
i = 1

contador =0

if(1 <= nAlunos <= 999):
    while(i <= vControle):
        nota = float(input())
            
        if(nota >= 0 and nota <=10):
            if(i<=nAlunos):
                arrayNotaOriginal.append(nota)
            elif(i>=nAlunos):
                arrayNovaNota.append(nota)
                
            
            i += 1
codAluno2 = 1
notaOriginal = 0

while(codAluno2 <= nAlunos):
    x1 = arrayNotaOriginal[notaOriginal]
    x2 = arrayNovaNota[notaOriginal]

    if(x1 <10 and x2 == 10):
        contador = contador +1
    codAluno2 += 1
    notaOriginal += 1

        
print("NOTAS ALTERADAS: {}".format(contador))

codAluno = 1    
notaOriginal = 0    
while(codAluno <= nAlunos):
    n1 = arrayNotaOriginal[notaOriginal]
    n2 = arrayNovaNota[notaOriginal]
   
    if(n1 == 10 or n2 < 10):
        total = n1
        print("-(00{})".format(codAluno) + " original: {:0>4}{}".format(n1,0)
        + " | " + "final: {:0>4}{}".format(total,0))
    elif(n1 < 10 and n1 > 8):
        total = (10 - n1) + n1
        
        print("*(00{})".format(codAluno) + " original: {:0>4}{}".format(n1,0)
        + " | " + "final: {:0>4}{}".format(total,0))
    elif(n1 <= 8):
        total = n1 + 2
        
        print("*(00{})".format(codAluno) + " original: {:0>4}{}".format(n1,0)
         + " | " + "final: {:0>4}{}".format(total,0))
        
    
   
    
    codAluno += 1
    notaOriginal += 1
