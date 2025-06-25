# Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições e imprima 
# "Dados de usuário válidos" ou o erro específico encontrado.

idade = int(input("Informe uma idade válida - "))
email = input("Informe um email - ")

if not 18 <= idade <= 65:
    print("A idade informada é inválida")
elif "@" not in email and "." not in email:
    print("o e-mail informado está errado")
else:
    print("As informações informadas estão corretas")
    
    