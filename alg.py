def mostrar_circuitos(circuitos):

    print("\n=== CIRCUITOS ===")
    
    circuitos = [c for c in circuitos if c.modification in ('A', 'M')]
    
    for circuito in circuitos:
        print(
            f"{circuito.id} {circuito.origem} {circuito.destino}"
        )

def mostrar_representacao_corte(
    circuitos
):
    print("\n=== REPRESENTAÇÃO DE CORTE ===")

    circuitos = [c for c in circuitos if c.modification in ('A')]
        
    for circuito in circuitos:
        print(
            f"{circuito.cable_dtr} {circuito.length}m"
        )


def comparar_circuitos(circuitos):

    circuitos_a_e = [c for c in circuitos if c.modification in ('A', 'E')]
    
    if len(circuitos_a_e) < 2:
        print("\nNão há circuitos com modificações 'A' e 'E' para comparar.")
        return []
    
    print("\n=== COMPARAÇÃO DE SOBRAS (A vs E) ===")
    
    pares_encontrados = []
    
    n = len(circuitos_a_e)
    for i in range(n):
        for j in range(i + 1, n):
            c1 = circuitos_a_e[i]
            c2 = circuitos_a_e[j]
            
            if c1.filtro_sobra(c2):
                pares_encontrados.append((c1, c2))
                print(f"[CONFLITO/SOBRA DETECTADO]")
                print(f"  -> Item 1: ID {c1.id} | Mod: {c1.modification} | Cabo: {c1.cable_dtr} | Comp: {c1.length}m")
                print(f"  -> Item 2: ID {c2.id} | Mod: {c2.modification} | Cabo: {c2.cable_dtr} | Comp: {c2.length}m")
                print("-" * 80)
    if not pares_encontrados:
        print("Nenhum par correspondente entre 'A' e 'E' com mesmo cabo e comprimento foi encontrado.")
        
    return pares_encontrados

def executar(circuitos):

    print(
        f"\nQuantidade de circuitos: "
        f"{len(circuitos)}"
    )

    mostrar_circuitos(circuitos)

    mostrar_representacao_corte(circuitos)

    comparar_circuitos(circuitos)

    return circuitos