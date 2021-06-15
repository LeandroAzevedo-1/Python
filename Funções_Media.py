#Funções - trecho de código damos nomes passamos alguns componentes
#funções tras vantagens, facilita a escrita e como ler.
#permite a reutilização de código .
#sintaxe basica começando com def nomes da função e os parâmetros exemplos

#Funçao que não recebe parâmetro
def exibemsg():
    print("Crinado Funções")# retorna essa mensagem entre aspas
    
exibemsg() # chamando a função

#Função com Parâmetro
#Cria uma função que calcule a média aritmética de 3 números

#Função média 
def media(n1,n2,n3):
    calcMedia =(n1+n2+n3)/3
    print(calcMedia)
media(3,7,9)  #chamandoa a função os valos ta de forma fixa mais pode pedir p usuário


#Funçao media pedindo para o usuario digitar o número
def media(n1,n2,n3):
    calcMedia =(n1+n2+n3)/3
    print(calcMedia)
num1 = int(input())
num2 = int(input())
num3 = int(input())
media(num1,num2,num3)#passamos entre parâmetro as variaveis digitada pelo usuario.
