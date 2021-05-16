# Erro de entrada ao validar e-mail mesmo digitado com espaços ou letras foras dos padrões de entrada.
# Criado por robsonvidigal@gmail.com
# Ex: Robson Vidigal @ Gmail.Com (Entrada) --> validação com esse micro programa corrige para robsonvidigal@gmail.com,
# evitando constragimentos pelo erro.

email = str(input('Digite seu email: '))
eliminado_espaco = email.split()
elimando_espaco_caractere = (''.join(eliminado_espaco))
convertendo_minusculo_email = elimando_espaco_caractere.lower()
print('Seu email digitado:{}' .format(convertendo_minusculo_email))