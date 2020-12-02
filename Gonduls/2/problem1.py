with open('input.txt', 'r') as inputf:
    inlist = inputf.readlines()

lista=[]
risposta=0
for element in inlist:
    lista = (element.replace('-', ' ' ).replace('\n','').replace(':','').split(' '))
    lista[0]=int(lista[0])
    lista[1]=int(lista[1])
    if (lista[-1].count(lista[-2]) >= lista[0]  and lista[-1].count(lista[-2]) <= lista[1]):
        risposta += 1
print(risposta)
