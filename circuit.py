class Circuito:
    def __init__(self, id, origem, destino, cable_dtr, diameter, length, modification):
        self.id = id
        self.origem = origem
        self.destino = destino
        self.cable_dtr = cable_dtr
        self.diameter = diameter
        self.length = float(length)
        self.modification = modification.strip().upper()

    def __str__(self):
        return (
            f"ID: {self.id}, "
            f"Origem: {self.origem}, "
            f"Destino: {self.destino}, "
            f"Cable DTR: {self.cable_dtr}, "
            f"Diâmetro: {self.diameter}, "
            f"Comprimento: {self.length}, "
            f"Modificação: {self.modification}"
        )

    def xmt_properties(self):
        return f"{self.id} {self.origem} {self.destino}"

    def corte_representation(self):
        return f"{self.cable_dtr} {self.length}m"

    def filtro_sobra(self, other):
        
        valid_modification = {self.modification, other.modification} == {'A', 'E'}
        return (
            valid_modification
            and self.length == other.length
            and self.modification != other.modification
        )

    def __eq__(self, other):
        if not isinstance(other, Circuito):
            return NotImplemented

        return (
            self.id == other.id
            and self.origem == other.origem
            and self.destino == other.destino
            and self.cable_dtr == other.cable_dtr
            and self.diameter == other.diameter
            and self.length == other.length
            and self.modification == other.modification
        )

    def __hash__(self):
        return hash((
            self.id,
            self.origem,
            self.destino,
            self.cable_dtr,
            self.diameter,
            self.length,
            self.modification
        ))