array = []
valoresCorridas = int(input())
ii = 0

while(valoresCorridas >= 0):
        array.append(valoresCorridas)
        valoresCorridas = int(input())
        ii += 1  
        
soma = sum(array)
mediaTotal = soma / len(array)
print("MEDIA:",f'{mediaTotal:.2f}')
for i in array:
    if(i <= mediaTotal):
        print(i)