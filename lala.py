from dataclasses import dataclass

@dataclass
class Fruta:
    nome: str
    cor: str

frutas = [
    Fruta(nome="Maçã", cor="Vermelha"),
    Fruta(nome="Banana", cor="Amarela"),
    Fruta(nome="Uva", cor="Roxa"),
]
for fruta in frutas:
    
    if fruta.cor == "Roxa":
        print(fruta.nome)

