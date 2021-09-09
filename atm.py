# Programa de ATM

print("\nNotas disponíveis: 100, 50, 10, 5 e 1.")
    
notas = {100:0, 50:0, 10:0, 5:0, 1:0}
    
try:
    saque = int(input("Digite o valor de saque em R$: ").replace(',','.'))
        
    if 10 <= saque <= 600:
        raise Exception("O valor deve ser entre 10 e 600 reais")
            
    for nota in notas.keys():   
        if saque % nota > 0 or saque//nota > 0:
            notas[nota] = saque//nota
            saque = saque % nota


    print(f"Serão fornecidas:\n",
        f"{notas[100]} notas de 100\n",
        f"{notas[50]} notas de 50\n", 
        f"{notas[10]} notas de 10\n",
        f"{notas[5]} notas de 5\n",
        f"{notas[1]} notas de 1\n")

except Exception as err:
    print(err)
