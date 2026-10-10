class CircuitManager:
    def __init__(self, circuitos):
        self.circuitos = circuitos
    
    def _filtrar_por_modificacao(self, *modifications):
        """Método auxiliar privado para evitar repetir list comprehensions."""
        return [c for c in self.circuitos if c.modification in modifications]
    
    def mostrar_circuitos(self):
        print("\n=== LISTA DE CIRCUITOS ===")
        circuitos_filtrados = self._filtrar_por_modificacao('A', 'M')
        for circuito in circuitos_filtrados:
            print(f"{circuito.id} {circuito.origem} {circuito.destino}")
    
    def comparar_circuitos(self):
        circuitos_a_e = self._filtrar_por_modificacao('A', 'E')
        
        if len(circuitos_a_e) < 2:
            print("\nNão há circuitos com modificações 'A' e 'E' para comparar.")
            return []
        
        print("\n=== COMPARAÇÃO DE SOBRAS (Adicionado vs Eliminado) ===")
        print(f"\nCONFLITO/SOBRA DETECTADO\n")
        
        pares_encontrados = []
        
        n = len(circuitos_a_e)
        for i in range(n):
            for j in range(i + 1, n):
                c1 = circuitos_a_e[i]
                c2 = circuitos_a_e[j]
                
                if c1.filtro_sobra(c2):
                    pares_encontrados.append((c1, c2))
                    print(f"Cabo Adicionado: {c2.id} | Cabo: {c2.cable_dtr} | {c2.length}m")
                    print(f"Cabo Eliminado:  {c1.id} | Cabo: {c1.cable_dtr} | {c1.length}m")
                    print("-" * 65)
        if not pares_encontrados:
            print("Nenhum par correspondente entre 'A' e 'E' com mesmo cabo e comprimento foi encontrado.")
            
        return pares_encontrados
    
    def mostrar_representacao_corte(self):
        print("\n=== REPRESENTAÇÃO DE CORTE ===")
        circuitos_filtrados = self._filtrar_por_modificacao('A')
        for circuito in circuitos_filtrados:
             print(f"{circuito.cable_dtr} {circuito.length}m")