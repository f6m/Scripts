data = [16, 25, 47, 56, 23, 45, 19, 55, 44, 27]

tallo = {} #Define tallo como un diccionario

for n in data: #recorre el array
    s, l = divmod(n, 10) #Divide cada valor del array entre 10:unidades, decenas
    tallo.setdefault(s, []).append(l) #Define keyname value default

print(tallo)

for s in sorted(tallo):
    print(f"{s} | {''.join(map(str, sorted(tallo[s])))}") 
    #Convierte los valores del diccionario en cadenas las junta y las despliega
    #f"{s} es para el formateado de cadenas
