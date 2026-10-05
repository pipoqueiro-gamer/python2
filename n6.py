# Lista para armazenar os dados e ir salvando na memória durante a execução
boletim = []

print("--- Sistema de Notas (Digite 'esc' no nome para sair) ---\n")

while True:
    aluno = input("Digite o nome do aluno: ").strip()
    
   
    if aluno.lower() == 'esc':
        print("\nSaindo do programa e gerando o relatório...")
        break
        
   
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
    except ValueError:
        print("❌ Erro: Digite apenas números para as notas. Tente novamente o aluno.\n")
        continue
        
    media = (nota1 + nota2) / 2
    status = "Aprovado" if media >= 6 else "Reprovado"
    
    
    boletim.append({
        'nome': aluno,
        'n1': nota1,
        'n2': nota2,
        'media': media,
        'status': status
    })
    print(f"✅ Dados de {aluno} salvos com sucesso!\n")


if boletim:
    print("\n" + "="*65)
    print(f"{'ALUNO':<20} | {'NOTA 1':<8} | {'NOTA 2':<8} | {'MÉDIA':<8} | {'SITUAÇÃO':<10}")
    print("="*65)
    for registro in boletim:
        print(f"{registro['nome']:<20} | {registro['n1']:<8.1f} | {registro['n2']:<8.1f} | {registro['media']:<8.1f} | {registro['status']:<10}")
    print("="*65)
else:
    print("\nNenhum aluno foi cadastrado.")
