idade = 20
frase = "Sou a Ândrya e tenho {} anos de idade"

'''
fraseF = frase + str(idade)
print(fraseF)
'''
print(frase.format(idade))

quantidade = 3
item = "bolo"
valor = 14.99
meuPedido = "Eu quero {} pedaços de {} por {} reais."
meuPedido2 = "Eu quero pagar {2} reais pelos {0} pedaços de {1}."

print(meuPedido.format(quantidade, item, valor))
print(meuPedido2.format(quantidade, item, valor))
