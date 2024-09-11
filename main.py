#   Polimorfismo,comportamento dado aos metodos das classes. As vezes e necessario qu o metodo seja executada diferente a superclasse
#
#importacao das classes
import clases as cl
import os

if __name__ == '__main__':
    #imputs de dados
    nome = input('Informe  o seu Nome: ')
    email = input('Informe  o seu E-mail: ')
    cpf = input('Informe  o seu Cpf: ')
    profissao = input('Informe  a sua Profissao: ')
    endereco = input('Informe  o seu Endereço: ')
    telefone = input('Informe  o seu Telefone: ')
    os.system('cls')

    #instacia dos objetos de PessoaFisica
    usuario = cl.PessoaFisica(nome, cpf, profissao, endereco, email, telefone) #primeiro os atribustos, na ordem do ocnstrutor, da subclasse e depois da Superclasse

    #entrada de dados da Juridica
    nome = input('Informe o nome da Epresa: ')
    email = input('Informe o e-mail da Epresa: ')
    cnpj = input('Informe o CNPJ da Epresa: ')
    razao_social = input('Informe o Razão Social da Epresa: ')
    endereco = input('Informe o Endereco da Epresa: ')
    telefone = input('Informe o Telefone da Epresa: ')
    os.system('cls')

    #instaciação do objeto PessoaJuridica
    empresa = cl.PessoaJuridica(nome, razao_social, cnpj, endereco, email, telefone)

    #saida de dados
    usuario.mostrar_cartao_visitas()
    print('_'*30)
    empresa.mostrar_cartao_visitas()