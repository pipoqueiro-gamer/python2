lista_de_compras = []
conta = 0.0  # Inicializa a variável do total geral

while True:
    item = input("---digite um item para adicionar à sua lista de compras (ou digite 'sair' para encerrar)---\n")
    
    if item.lower() == 'sair':
        break
        
    try:
        valores = float(input("digite o valor do item: "))
        quantidade = int(input("digite a quantidade do item: "))
    except ValueError:
        print("Valores ou quantidade inválidos, tente novamente.\n")
        continue
        
    total_item = valores * quantidade
    conta += total_item
    
    lista_de_compras.append({
        "item": item,
        "valor": valores,
        "quantidade": quantidade,
        "total_item": total_item
    })

# O loop de impressão fica fora do 'while' para mostrar tudo apenas no final
print("\n=== SUA LISTA DE COMPRAS ===")
for produto in lista_de_compras:
    print(f"Item: {produto['item']} | Valor: R$ {produto['valor']:.2f} | Qtd: {produto['quantidade']} | Total do Item: R$ {produto['total_item']:.2f}")

print(f"\nValor total da conta: R$ {conta:.2f}")
