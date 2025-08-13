from palmas import Palmas
from curiosidades import Curiosidades
from utils.terminal import clear_screen


class Conversor:
    @staticmethod
    def converter_para_numerado():
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
                + "\n"
                + "\n"
                + r"""

     [1] Voltar para o MENU
"""
            )
            busca = (
                input("     Digite o endereço (ex. ARSO 12, ARNO 13, etc): ")
                .upper()
                .strip()
            )
            if busca == "1":
                clear_screen()
                return
            cidade = Palmas()
            achou = False
            for d in cidade.quadras.values():
                for chave_0, valor_1 in d.items():
                    if busca == chave_0:
                        clear_screen()
                        print(f"     🔎 Busca: {chave_0} | 📍 Resultado: {valor_1}")
                        achou = True
                if achou:
                    break
            if not achou:
                clear_screen()
                print("             Endereço", busca, "inválido!")
    @staticmethod
    def converter_para_sigla():
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
                + "\n"
                + "\n"
                + r"""

     [1] Voltar para o MENU
"""
            )
            busca = (
                input("     Digite o endereço (ex. 603 Sul, 108 Norte): ")
                .title()
                .strip()
            )
            if busca == "1":
                clear_screen()
                return
            cidade = Palmas()
            achou = False
            for d in cidade.quadras.values():
                for chave_0, valor_1 in d.items():
                    if busca == valor_1:
                        clear_screen()
                        print(f"     🔎 Busca: {valor_1} | 📍 Resultado: {chave_0}")
                        achou = True
                if achou:
                    break
            if not achou:
                clear_screen()
                print("             Endereço", busca, "inválido!")

