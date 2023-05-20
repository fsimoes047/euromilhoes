f=open('result.txt', 'r')
chave = f.read().split(';')

print('Fim da 1ª parte')     
chaves=[]
c=0
for cha in chave:   
    cha1 = cha.split(',')
    l2=set()
    for i in cha1:
        if i:
            l2.add(int(i))
    a=0    
    for j in chaves:
        if l2 == j:
            a=1
            break            
    if a==0:
        chaves.append(l2)


print('Fim da 2ª parte')    
print('Numero de chaves: '+ str(len(chaves)))
