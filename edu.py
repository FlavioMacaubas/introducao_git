# Aplicativo - Aprovação e frequência

# Informações do usuário 
nota = float(input("Informe a nota final: \n").replace(',','.'))
freq = float(input("Informe a frequência - em porcentagem: \n").replace(',','.'))
reprovacoes = int(input("Informe quantidade de reprovações: \n").replace(',','.'))
cra = float(input("Informe o CRA: \n").replace(',','.'))

# Teste condições
aprovado = (nota >= 7) and (freq >= 75)
desligado = (reprovacoes >= 2) or (cra < 5)

print(f"O aluno foi aprovado: {aprovado} \nO aluno foi desligado: {desligado}")

