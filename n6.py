boletim = []
print("--- boletim de notas dos alunos ---\n")

while True:
    aluno = input("Digite o nome do aluno (ou 'nao' para sair): ")
    
    
    if aluno == "nao" or aluno == "Não" or aluno == "não" or aluno == "NAO":
        print("Saindo do programa e gerando o relatório...\n")
        break
        
    nota1 = float(input("digite a primeira nota do aluno (0 a 10): "))
    nota2 = float(input("digite a segunda nota do aluno (0 a 10): "))
    
    media = (nota1 + nota2) / 2
    
    if media >= 6:
        status = "aprovado"
    else:
        status = "reprovado"
        
    
    boletim.append({
        "nome": aluno,
        "nota1": nota1,
        "nota2": nota2,
        "media": media,
        "status": status
    })

print("=== RELATÓRIO FINAL ===")
for tabela in boletim:
    print(f"Aluno: {tabela['nome']} | Nota 1: {tabela['nota1']} | Nota 2: {tabela['nota2']} | Média: {tabela['media']} | Status: {tabela['status']}")

print("\nPrograma terminado.")
