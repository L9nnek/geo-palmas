from conversor import Conversor
from utils.terminal import clear_screen


def main():
    clear_screen()
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
            clear_screen()
            Conversor.converter_para_numerado()

        elif escolha == "2":
            clear_screen()
            Conversor.converter_para_sigla()

        elif escolha == "3":
            print("\n         ✅ Programa encerrado!\n")
            break

        else:
            clear_screen()
            print("\n     Opção inválida! Digite 1, 2 ou 3.\n")


if __name__ == "__main__":
    main()
