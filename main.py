from pdf_reader import ler_pdf
from alg import executar


def main():

    print("Iniciando processamento...")

    circuitos = ler_pdf()

    print(
        f"PDF processado. "
        f"{len(circuitos)} circuitos encontrados."
    )

    resultado = executar(circuitos)

    # ========================================================
    # 3. RESULTADO
    # ========================================================

    print(
        f"\nProcessamento finalizado."
    )


if __name__ == "__main__":
    main()