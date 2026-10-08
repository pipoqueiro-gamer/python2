português = input("digite sua palavra em português: ")
l = []

# O Python lê diretamente cada letra da palavra, uma por uma
for letra in português:
    if letra in "aeiouáéíóúâêôãõAEIOUÁÉÍÓÚÂÊÔÃÕ":
        l.append(letra)

print("As vogais encontradas foram:", l)


