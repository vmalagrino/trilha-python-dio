# função built-in sorted retorna uma nova lista ordenada a partir de um iterável

linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

# não é obrigatório passar o parâmetro key e reverse
print(sorted(linguagens))  # ["c", "csharp", "java", "js", "python"]
