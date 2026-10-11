class CircuitManager:
    def __init__(self, circuitos):
        self.circuitos = circuitos
        self.list_to_filter = []
    
    def _filtrar_por_modificacao(self, *modifications):
        """Método auxiliar privado para evitar repetir list comprehensions."""
        return [c for c in self.circuitos if c.modification in modifications]
    
    
    def _encontrar_pares_sobra(self):
            circuitos_a_e = self._filtrar_por_modificacao('A', 'E')
            
            pares_encontrados = []
            self.list_to_filter.clear()
            
            n= len(circuitos_a_e)
            for i in range(n):
                for j in range(i + 1, n):
                    c1 = circuitos_a_e[i]
                    c2 = circuitos_a_e[j]
                    
                    if c1.filtro_sobra(c2):
                        pares_encontrados.append((c1, c2))
                        self.list_to_filter.append(c1)
            return pares_encontrados
    
    def mostrar_circuitos(self):
        print("\n=== LISTA DE CIRCUITOS ===")
        circuitos_filtrados = self._filtrar_por_modificacao('A', 'M')
        for circuito in circuitos_filtrados:
            print(f"{circuito.id} {circuito.origem} {circuito.destino}")
    
    def comparar_circuitos(self):
        # Obter circuitos com modificações A ou E e os pares correspondentes
        circuitos_a_e = self._filtrar_por_modificacao('A', 'E')
        pares_encontrados = self._encontrar_pares_sobra()

        if len(circuitos_a_e) < 2:
            print("\nNão há circuitos com modificações 'A' e 'E' para comparar.")
            return []

        print("\n=== COMPARAÇÃO DE SOBRAS (Adicionado vs Eliminado) ===")

        if pares_encontrados:
            print("\nCONFLITO/SOBRA DETECTADO\n")
            for c1, c2 in pares_encontrados:
                print(f"Cabo Adicionado: {c2.id} | Cabo: {c2.cable_dtr} | {c2.length}m")
                print(f"Cabo Eliminado:  {c1.id} | Cabo: {c1.cable_dtr} | {c1.length}m")
                print("-" * 65)
        else:
            print(
                "Nenhum par correspondente entre 'A' e 'E' com mesmo cabo e"
                " comprimento foi encontrado."
            )

        return pares_encontrados
    
    def mostrar_representacao_corte(self):
        print("\n=== REPRESENTAÇÃO DE CORTE ===")

        self._encontrar_pares_sobra()

        circuitos_filtrados = self._filtrar_por_modificacao('A')

        # Cria uma lista com os cabos e comprimentos a excluir
        pares_excluir = {
            (c.cable_dtr, c.length)
            for c in self.list_to_filter
        }
        

        for circuito in circuitos_filtrados:
            chave = (circuito.cable_dtr, circuito.length)

            if chave not in pares_excluir:
                print(f"{circuito.cable_dtr} {circuito.length}m")
        