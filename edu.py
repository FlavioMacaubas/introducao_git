# Aplicativo - Aprovação e frequência

# Informações do usuário 
faltas = float(input("Informe as faltas: \n").replace(',','.'))

# Verificando reprovação
if faltas > 15:
    situacao = 'reprovado por falta'
else:
    nota = float(input("Informe a nota: \n").replace(',','.'))
    if nota >= 7:
        situacao = "aprovado por média"
    elif (4 <= nota < 7):
        nota_final = float(input("Informe a nota final/recuperação: \n"))
        media_final = (0.6*nota + 0.4*nota_final)
        situacao = "aprovado na final" if media_final >= 5 else "reprovado na final"
    else:
        situacao = "reprovado por média"
        
print(f"O aluno foi {situacao}")

