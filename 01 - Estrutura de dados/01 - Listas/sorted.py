# Função built-in
linguagens = ["python", "js", "c", "java", "csharp"]

# Pode passar ou não a lista, e a chave lambda
print(sorted(linguagens, key=lambda x:len(x)))

print(sorted(linguagens, key=lambda x:len(x), reverse=True))


