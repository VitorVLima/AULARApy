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

'''disciplinas = ["RAD\n", "C++\n", "Python\n", "C\n"]

with open("disciplinas.txt", "w") as arquivo:
    arquivo.writelines(disciplinas)

with open("disciplinas.txt", "r") as arquivo:
    print(arquivo.read())'''

''''try:
    with open("naoexistetxt", "r") as arquivo:
        print(arquivo.read())

except FileNotFoundError as error:
    print("arquivo inexistente", error)'''

'''try:
    with open("naoexistetxt", "r") as arquivo:
        arquivo.write("java")
except IOError as e:
    print("O erro foi: ", e)'''

alunos = [("carlos",10.0), ("pedro", 9.6), ("Lucas", 9.6)]

with open("notas.txt", "w") as arquivo:
    for aluno in alunos:
        arquivo.write(f"Nome: {aluno[0]}, Nota: {aluno[1]}\n")


try:
    with open("notas.txt", "w") as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print("arquivo inexistente")
except IOError:
    print("erro na leitura do arquivo")








