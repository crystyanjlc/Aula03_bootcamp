numero_desejo = int(input("Informe um número inteiro entre 0 e 10 - "))

while numero_desejo <= 0 or  numero_desejo >= 11:
   numero_desejo = int(input("Informe um número inteiro entre 0 e 10 - "))
   
   
tentativa = int(input("Tente adivinhar o número que é entre 0 e 10 - "))
while tentativa != numero_desejo:
    if tentativa > numero_desejo:
        print("O número informado é maior. Tente novamente")
        tentativa = int(input("Tente adivinhar o número que é entre 0 e 10 - "))
    else:
        print("O número informado é menor. Tente novamente")
        tentativa = int(input("Tente adivinhar o número que é entre 0 e 10 - "))
        
print(f"Você acertou, o número é - {numero_desejo}")

      
      
