import circuit_manager as cm

def mostrar_circuitos(circuitos):

    cm.CircuitManager(circuitos).mostrar_circuitos()

def mostrar_representacao_corte(
    circuitos
):
    cm.CircuitManager(circuitos).mostrar_representacao_corte()


def comparar_circuitos(circuitos):

    cm.CircuitManager(circuitos).comparar_circuitos()

def executar(circuitos):

    print(
        f"\nQuantidade de circuitos: "
        f"{len(circuitos)}"
    )

    mostrar_circuitos(circuitos)

    mostrar_representacao_corte(circuitos)

    comparar_circuitos(circuitos)

    return circuitos