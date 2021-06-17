class Vaso:
    def __init__(self, material, alto, uso):
        self.material = material
        self.alto = alto
        self.uso = uso

    def uso(self): 
        if self.uso == "Bebida Fria":
            print("Puede tomar una bebida fria")
        else: print("Puede tomar bebida caliente")
        return self

    def __str__(self):
        return f"El vaso es de {self.material}. Tiene {self.alto}cms de alto. Se usa para: {self.uso}"

vaso1=Vaso("Vidrio", 15, "Bebida Fria")
vaso2=Vaso("Ceramica", 10, "Bebida Caliente")

print(vaso1)
print(vaso2)