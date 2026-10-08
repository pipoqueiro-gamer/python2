lista_de_compras = []
conta = 0.0

while True:
    print("--- digite um item para adicionar à lista (ou 'sair' para encerrar) ---")
    item = input()
    
    if item == "sair" or item == "SAIR" or item == "Sair":
        break
        
    valores = float(input("digite o valor do item: "))
    quantidade = int(input("digite a quantidade do item: "))
        
    total_item = valores * quantidade
    conta = conta + total_item
    
    lista_de_compras.append({
        "item": item,
        "valor": valores,
        "quantidade": quantidade,
        "total_item": total_item
    })

print() # Deixa uma linha em branco de um jeito bem simples
print("=== SUA LISTA DE COMPRAS ===")
for produto in lista_de_compras:
    print(f"Item: {produto['item']} | Valor: R$ {produto['valor']} | Qtd: {produto['quantidade']} | Total: R$ {produto['total_item']}")

print() 
print(f"Valor total da conta: R$ {conta}")

