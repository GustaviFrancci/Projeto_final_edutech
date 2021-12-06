class Empresa:
    def __init__(self, id_empresa, razao_social, endereco, cnpj):
        self._id_empresa = id_empresa
        self._razao_social = razao_social
        self._endereco = endereco
        self._cnpj = cnpj

# getters
    @property
    def id_empresa(self):
        return self._id_empresa

    @property
    def razao_social(self):
        return self._razao_social

    @property
    def endereco(self):
        return self._endereco

    @property
    def cnpj(self):
        return self._cnpj

# setters
    @id_empresa.setter
    def id_empresa(self, id_empresa):
        self._id_empresa = id_empresa

    @razao_social.setter
    def razao_social(self, razao_social):
        self._razao_social = razao_social

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @cnpj.setter
    def cnpj(self, cnpj):
        self._cnpj = cnpj
