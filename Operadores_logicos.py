# AND = para ser True td tem que ser True
# OR = para ser True apenas um deve ser True

print(True and True and True)
print(True and False and True)
print(True or True or True)
print(True or False or False)
print(False or False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial =  True


expressao1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(expressao1)

expressao2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(expressao2)

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite) 
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

expressao3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(expressao3)