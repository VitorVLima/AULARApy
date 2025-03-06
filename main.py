'''arquivo = open("texto.txt","r")
print(arquivo.read())'''
'''print(arquivo.readline())
print(arquivo.readline())
print(arquivo.seek(0))
print(arquivo.readlines())
#print(arquivo.seek(0))'''
'''print(arquivo.tell())
arquivo.close()
print(arquivo.closed)'''
'''print(arquivo.read())
print(arquivo.seek(0))
print(arquivo.read(8))'''
'''print(arquivo.name)
print(arquivo.mode)
print(arquivo.closed)'''

'''arquivo = open("novo.txt","w")
arquivo.write("Arquivo de escrita")
arquivo.close()
print(arquivo.closed)'''

'''arquivo = open("frutas.txt","w")
arquivo.write("banana\n")
arquivo.write("uva\n")
arquivo.write("mamao\n")
arquivo.close()'''

'''precos = [8000]

with open("precos.txt", "w") as arquivo:
    for preco in precos:
        arquivo.write(f"{preco} \n")
print(arquivo.closed)'''

'''precos = [500, 600, 300, 660]

with open("precos.txt", "a") as arquivo:
    for preco in precos:
        arquivo.write(f"{preco} \n")
print(arquivo.closed)'''

disciplinas = ["RAD\n", "C++\n", "Python\n", "C\n"]

with open("disciplinas.txt", "w") as arquivo:
    arquivo.writelines(disciplinas)





