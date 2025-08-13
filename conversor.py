from palmas import Palmas
from curiosidades import Curiosidades


class Conversor:

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
                for i in range(50):
                    print("\n")
                return
            cidade = Palmas()
            resultado = cidade.get_mapa().get(busca)
            if resultado:
                for i in range(50):
                    print("\n")
                print(f"     🔎 Busca: {busca} | 📍 Resultado: {resultado}")
            else:
                for i in range(50):
                    print("\n")
                print("             Endereço", busca, "inválido!")

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
                for i in range(50):
                    print("\n")
                return     
            cidade = Palmas()
            mapa_inverso = {v: k for k, v in cidade.get_mapa().items()}
            resultado = mapa_inverso.get(busca)
            if resultado:
                for i in range(50):
                    print("\n")
                print(f"     🔎 Busca: {busca} | 📍 Resultado: {resultado}")
            else:
                for i in range(50):
                    print("\n")
                print("             Endereço", busca, "inválido!")
