class Contato:
    def __init__(self, telefone, email):
        self._telefone = telefone
        self._email = email

# getters
    @property
    def telefone(self):
        return self._telefone

    @property
    def email(self):
        return self._email

# setters
    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @email.setter
    def email(self, email):
        self._email = email
