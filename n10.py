boletim_dos_alunos=[]
print("---boletim de notas dos alunos---\n")
while True:
    aluno=input("Digite o nome do aluno: (ou digite 'não'para sair e nao por aluno---) ")
    if aluno.lower()=="não":
        print("saindo do programa e gerando o relatorio")
        break
    try:
        nota1=float(input("digite a nota do aluno de(0 a 10): "))
        nota2=float(input("digite a nota do aluno de(0 a 10): "))
    except ValueError:
        print("valor invalido, tente novamente")
        continue
    media=(nota1+nota2)/2
    status="aprovado" if media>=6 else "reprovado"
    boletim_dos_alunos.append({
        "nome":aluno,
        "nota1":nota1,
        "nota2":nota2,
        "media":media,
        "status":status
    })
    if boletim_dos_alunos:
     print("\n"+"="*65)
     print(f"{'aluno':<20} | {'nota':<8} | {'nota2':<8} | {'media':<8} | {'status':<10}")
     print("="*65)
     for tabela in boletim_dos_alunos:
        print(f"{tabela['nome']:<20} | {tabela['nota1']:<8.1f} | {tabela['nota2']:<8.1f} | {tabela['media']:<8.1f} | {tabela['status']:<10}")
    else:
       print("\terminou o programa")