#   No python se cria um arquivo pois ele reconhece as clases como se fosse uma pasta, diferente do java que 
#que é um arquivo para cada Classe 
#
#Classe Pai, Superclasse ou Classe Base
class Pessoa:
    #atributos definidos no METODO CONSTRUTOR
    def __init__(self, endereco, email, telefone):
        self.endereco = endereco
        self.email = email
        self.telefone = telefone

    #METODO de acao
    def mostrar_cartao_visitas(self):
        print(f'Endereço: {self.endereco}.')
        print(f'E-mail: {self.email}.')
        print(f'Telefone: {self.telefone}.')

#subclasse, classe filha, classe derivada de Pessoa
class PessoaFisica(Pessoa):
    #POLIMORFISMO
    def __init__(self, nome, cpf, profissao, endereco, email, telefone): #nao repete os atributos do construtor, somente os snovos
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao
        super().__init__(endereco, email, telefone)# pega os atributos do construtor e adciona novo comportamento 

    def mostrar_cartao_visitas(self):
        print(f'Nome do Usuário: {self.nome}.')
        print(f'Nome do Usuário: {self.cpf}.')
        print(f'Nome do Usuário: {self.profissao}.')
        super().mostrar_cartao_visitas()

#Ssubclasse Juridica
class PessoaJuridica(Pessoa):
    #polimorfismo do construtor
    def __init__(self,nome_fantasia, razao_social, cnpj, endereco, email, telefone):
        self.nome_fantasia = nome_fantasia
        self.razao_social = razao_social
        self.cnpj = cnpj
        super().__init__(endereco, email, telefone)

    def mostrar_cartao_visitas(self):
        print(f' Nome da Empresa: {self.nome_fantasia}')
        print(f' Nome Social: {self.razao_social}')
        print(f' CNPJ da Empresa: {self.cnpj}')
        super().mostrar_cartao_visitas()