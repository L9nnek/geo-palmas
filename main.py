from conversor import Conversor


def main():
    print("\n" * 50)
    while True:
        print(
            r"""
▗▄▄▖▗▄▄▄▖ ▗▄▖ ▗▄▄▖  ▗▄▖ ▗▖   ▗▖  ▗▖ ▗▄▖  ▗▄▄▖
▐▌   ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌   ▐▛▚▞▜▌▐▌ ▐▌▐▌
▐▌▝▜▌▐▛▀▀▘▐▌ ▐▌▐▛▀▘ ▐▛▀▜▌▐▌   ▐▌  ▐▌▐▛▀▜▌ ▝▀▚▖
▝▚▄▞▘▐▙▄▄▖▝▚▄▞▘▐▌   ▐▌ ▐▌▐▙▄▄▖▐▌  ▐▌▐▌ ▐▌▗▄▄▞▘

    Conversor de Endereços - Palmas / TO
            Feito por Línnek

    [1] Converter para formato numérico.
    [2] Converter para formato com sigla.
    [3] Sair
"""
        )

        escolha = input("     Escolha uma opção (1, 2 ou 3): ").strip()

        if escolha == "1":
            print("\n" * 50)
            Conversor.converter_para_numerado()

        elif escolha == "2":
            print("\n" * 50)
            Conversor.converter_para_sigla()

        elif escolha == "3":
            print("\n         ✅ Programa encerrado!\n")
            break

        else:
            print("\n" * 50)
            print("\n     Opção inválida! Digite 1, 2 ou 3.\n")


if __name__ == "__main__":
    main()
