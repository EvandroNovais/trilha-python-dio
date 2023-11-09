# Ordena a lista
from trace import Trace


linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()


linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True) #Orde ao contrario

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)

print(linguagens)