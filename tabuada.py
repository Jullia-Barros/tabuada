print ("################################")
print ("Seja bem vindo!!")
print("#################################")

numero= int (input ("qual número você quer calcular a tabuada?:"))

for i in range(1,11):
    mensagem = "{} X {}= {}".format(numero, i, numero*i)
    print(mensagem)