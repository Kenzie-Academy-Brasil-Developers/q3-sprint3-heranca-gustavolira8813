from classes import Recipiente, Copo

if __name__ == "__main__":
    # Execute suas testagens manuais aqui
    ...

r = Recipiente(100)
print(r)
print(r.esta_limpo())
r.sujar()
print(r.esta_limpo())
r.lavar()
print(r.esta_limpo())

c = Copo(500)
print(c)
c.encher("nescau")
print(c.bebida)
print(c)
c.beber(49)
print(c)
print(c.esta_limpo())
c.lavar()
print(c)

