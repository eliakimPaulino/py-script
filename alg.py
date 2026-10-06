def mostrar_circuitos(circuitos, quantidade=5):

    print("\n=== CIRCUITOS ===")

    for circuito in circuitos[:quantidade]:

        print(
            circuito.xmt_properties()
        )


def mostrar_representacao_corte(
    circuitos,
    quantidade=5
):
    print("\n=== REPRESENTAÇÃO DE CORTE ===")

    for circuito in circuitos[:quantidade]:

        print(
            circuito.corte_representation()
        )


def comparar_circuitos(circuitos):

    if len(circuitos) < 2:

        print(
            "Não existem circuitos suficientes "
            "para comparação."
        )

        return

    referencia = circuitos[1]

    print("\n=== COMPARAÇÃO ===")

    for circuito in circuitos[:5]:

        resultado = circuito.filtro_sobra(
            referencia
        )

        print(
            f"{circuito.id} "
            f"x "
            f"{referencia.id} "
            f"=> {resultado}"
        )


def executar(circuitos):

    print(
        f"\nQuantidade de circuitos: "
        f"{len(circuitos)}"
    )

    mostrar_circuitos(circuitos)

    mostrar_representacao_corte(circuitos)

    #comparar_circuitos(circuitos)

    return circuitos