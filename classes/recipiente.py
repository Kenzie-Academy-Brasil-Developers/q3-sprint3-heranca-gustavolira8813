# Desenvolva sua classe Recipiente aqui.
class Recipiente:
    
    def __init__(self, tamanho, conteudo = 0, limpo: bool = True) -> None:
        if tamanho > 0:
            self.tamanho = tamanho
        else:
            self.tamanho = 0
        self.conteudo = conteudo
        self.limpo = limpo
    
    def esvaziar(self) -> None:
        self.conteudo = 0
    
    def esta_vazio(self):
        if self.conteudo == 0:
            return True
        else:
            return False

    def lavar(self):
        self.conteudo = 0
        self.limpo = True
    
    def esta_limpo(self):
        return self.limpo

    def estado(self):
        if self.limpo == True:
            return "limpo"
        else:
            return "sujo"

    def sujar(self):
        self.limpo = False
        
    def __repr__(self):
        return f"Um recipiente {self.estado()} não especificado"

    def __str__(self):
        return f"Um recipiente {self.estado()} não especificado"


