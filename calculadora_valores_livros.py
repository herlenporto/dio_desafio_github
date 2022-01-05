#Disciplina: Projeto integrador de competências em ciência da computação 1
#Aluna: Herlen Vital Porto
#Atividade 1

qtd_livros = float(input("quantos livros você quer comprar? "))

criterio_a = (0.25 * qtd_livros) + 7.50
criterio_b = (0.50 * qtd_livros) + 2.50
criterio_c = (0.65 * qtd_livros) + 1.50

if criterio_a == criterio_b:
    print("o seu total é de R$%.2f de acordo com o criterio c" %criterio_c)
elif criterio_a == criterio_c:
    print("o seu total é de R$%.2f de acordo com o criterio b" %criterio_b)
elif criterio_b == criterio_c:
    print("o seu total é de R$%.2f de acordo com o criterio a" %criterio_a)
elif criterio_a > criterio_b and criterio_a > criterio_c:
    print("o seu total é de R$%.2f de acordo com o criterio a" %criterio_a)
elif criterio_b > criterio_c and criterio_b > criterio_a:
    print("o seu total é de R$%.2f de acordo com o criterio b" %criterio_b)
elif criterio_c > criterio_a and criterio_c > criterio_b:
    print("o seu total é de R$%.2f de acordo com o criterio c" %criterio_c)
