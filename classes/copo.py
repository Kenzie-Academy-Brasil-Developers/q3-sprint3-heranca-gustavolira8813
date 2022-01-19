# Desenvolva sua classe Copo aqui.
from classes.recipiente import Recipiente

class Copo(Recipiente):
    
    def __init__(self, tamanho, conteudo=0, limpo: bool = True, bebida = None) -> None:
        super().__init__(tamanho, conteudo = conteudo, limpo = limpo)
        self.bebida = bebida
   
    def encher(self, bebida = "água"):
        if self.esta_limpo() == True:
            self.sujar()
            self.conteudo += self.tamanho
            self.bebida = bebida
        else:
            return "Não se pode encher um copo sujo"

    def beber(self, quantidade):
        if quantidade < 0:
            return "Quantidade deve ser positiva"
        elif quantidade > self.conteudo:
            return "Não há bebida suficiente no copo"
        else:
            self.conteudo -= quantidade 
    
    def lavar(self):
        self.bebida = None
        self.conteudo = 0
        self.limpo = True
            
    def __repr__(self):
        if not self.conteudo:

            return f"Um copo vazio de {self.tamanho:.1f}ml"

        return f"Um copo de {self.tamanho:.1f}ml contendo {self.conteudo:.1f}ml de {self.bebida}"

    def __str__(self):
        if not self.conteudo:

            return f"Um copo vazio de {self.tamanho:.1f}ml"

        return f"Um copo de {self.tamanho:.1f}ml contendo {self.conteudo:.1f}ml de {self.bebida}"

