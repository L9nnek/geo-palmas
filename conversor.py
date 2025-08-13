from palmas import Palmas
from curiosidades import Curiosidades
from utils.terminal import clear_screen


class Conversor:
    @staticmethod
    def converter_para_numerado():
        # Ex.: ARSO 12  ->  105 Sul
        while True:
            print(
                r"""
▗▄▄▖▗▄▄▄▖ ▗▄▖ ▗▄▄▖  ▗▄▖ ▗▖   ▗▖  ▗▖ ▗▄▖  ▗▄▄▖
▐▌   ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌   ▐▛▚▞▜▌▐▌ ▐▌▐▌
▐▌▝▜▌▐▛▀▀▘▐▌ ▐▌▐▛▀▘ ▐▛▀▜▌▐▌   ▐▌  ▐▌▐▛▀▜▌ ▝▀▚▖
▝▚▄▞▘▐▙▄▄▖▝▚▄▞▘▐▌   ▐▌ ▐▌▐▙▄▄▖▐▌  ▐▌▐▌ ▐▌▗▄▄▞▘
"""
                + "\n\n"
                + Curiosidades.frases()
                + "\n\n"
                + r"     [1] Voltar para o MENU\n"
            )
            busca = input("     Digite o endereço (ex. ARSO 12, ARNO 13, etc): ").upper().strip()
            if busca == "1":
                clear_screen()
                return

            cidade = Palmas()
            resultado = cidade.lookup_numerado(busca)

            clear_screen()
            if resultado:
                print(f"     🔎 Busca: {busca} | 📍 Resultado: {resultado}")
            else:
                print(f"             Endereço {busca} inválido!")

    @staticmethod
    def converter_para_sigla():
        # Ex.: 105 Sul  ->  ARSO 12
        while True:
            print(
                r"""
▗▄▄▖▗▄▄▄▖ ▗▄▖ ▗▄▄▖  ▗▄▖ ▗▖   ▗▖  ▗▖ ▗▄▖  ▗▄▄▖
▐▌   ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌   ▐▛▚▞▜▌▐▌ ▐▌▐▌
▐▌▝▜▌▐▛▀▀▘▐▌ ▐▌▐▛▀▘ ▐▛▀▜▌▐▌   ▐▌  ▐▌▐▛▀▜▌ ▝▀▚▖
▝▚▄▞▘▐▙▄▄▖▝▚▄▞▘▐▌   ▐▌ ▐▌▐▙▄▄▖▐▌  ▐▌▐▌ ▐▌▗▄▄▞▘
"""
                + "\n\n"
                + Curiosidades.frases()
                + "\n\n"
                + r"     [1] Voltar para o MENU\n"
            )
            busca = input("     Digite o endereço (ex. 603 Sul, 108 Norte): ").title().strip()
            if busca == "1":
                clear_screen()
                return

            cidade = Palmas()
            resultado = cidade.lookup_sigla(busca)

            clear_screen()
            if resultado:
                print(f"     🔎 Busca: {busca} | 📍 Resultado: {resultado}")
            else:
                print(f"             Endereço {busca} inválido!")