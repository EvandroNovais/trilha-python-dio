#count
#Conta elementos dentro de uma listas
cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

#extend
#extende uma lista juntando com outra no final.
linguagens = ["python", "js", "c"]

print(linguagens)

linguagens.extend(["java", "csharp"])

print(linguagens)

#index
#Traz o indice da primeira ocorrência de determinado elemento em uma lista.
linguagens = ["python", "java", "c", "java", "csharp"]
print()

#pop
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop(0))

