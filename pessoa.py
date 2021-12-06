class Pessoa:
    def __init__(self, nome, endereco, bairro, cep, cidade, estado, id_empresa):

        self._nome = nome
        self._endereco = endereco
        self._bairro = bairro
        self._cep = cep
        self._cidade = cidade
        self._estado = estado
        self.id_empresa = id_empresa
# 	id	nome endereço bairro cep cidade 	estado idade cpf id_empresa
# mostrar dados.


    @property
    def nome(self):
        return self._nome

    @property
    def endereco(self):
        return self._endereco

    @property
    def bairro(self):
        return self._bairro

    @property
    def cep(self):
        return self._cep

    @property
    def cidade(self):
        return self._cidade

    @property
    def estado(self):
        return self._estado

    @property
    def id_empresa(self):
        return self._id_empresa

# definir dados.

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @bairro.setter
    def bairro(self, bairro):
        self._bairro = bairro

    @cep.setter
    def cep(self, cep):
        self._cep = cep

    @cidade.setter
    def cidade(self, cidade):
        self._cidade = cidade

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @id_empresa.setter
    def id_empresa(self, id_empresa):
        self._id_empresa = id_empresa
