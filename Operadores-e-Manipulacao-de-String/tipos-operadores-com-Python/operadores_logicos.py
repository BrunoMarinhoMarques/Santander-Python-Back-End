saldo = 1000
saque = 250
limite = 200
conta_especial = True

resposta = (saldo >= saque and saque <= limite) or (conta_especial and saldo>= saque)

print(resposta)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque


concatenacao_operadores = conta_especial_com_saldo_suficiente or conta_normal_com_saldo_suficiente
print(concatenacao_operadores)