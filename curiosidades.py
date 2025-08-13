import random


class Curiosidades:
    @staticmethod
    def frases():
        frases = [
            "Palmas foi projetada com base em quadras numeradas, facilitando a localização em toda a cidade.",
            "A organização urbana de Palmas é inspirada no modelo de Brasília, com setores bem definidos.",
            "Cada quadra em Palmas possui uma sigla que indica a região e sua posição no mapa da cidade.",
            "As quadras da região Norte começam com ARNO, ARNE e AVNO; enquanto as do Sul são ARSO, ARSE e AVSO.",
            "Os nomes das quadras representam a função e localização, como Área Residencial Norte ou Sul.",
            "As ruas em Palmas são largas e retas, pensadas para facilitar o fluxo de veículos e pedestres.",
            "Palmas é dividida em regiões Norte e Sul, com o centro administrativo na divisa entre as duas.",
            "A numeração das quadras segue uma lógica geográfica, indo de Norte para Sul e de Leste para Oeste.",
            "A sigla de uma quadra em Palmas pode indicar se ela é residencial, comercial ou de serviços.",
            "Além das quadras, a cidade possui avenidas principais que conectam rapidamente diferentes setores.",
            "A estrutura em quadras reduz o uso de nomes de ruas, tornando os endereços mais diretos.",
            "A divisão em quadras permite um planejamento urbano eficiente e de fácil expansão futura.",
            "Setores como ACSU e ACNO indicam áreas comerciais, enquanto ARSO e ARNO são áreas residenciais.",
            "A cidade também conta com áreas específicas para serviços públicos e zonas industriais.",
            "A Setorização de Palmas foi pensada para separar moradia, comércio e serviços de forma equilibrada.",
            "As quadras são identificadas com placas que trazem a sigla e o número, facilitando a navegação.",
            "As avenidas Teotônio Segurado e JK são eixos principais que cruzam grande parte da cidade.",
            "O formato das quadras e a sinalização padronizada ajudam na orientação mesmo para quem visita a cidade pela primeira vez.",
            "O mapa de Palmas lembra um tabuleiro, com regiões bem separadas e vias amplas de ligação.",
            "A cidade possui setores específicos para atividades comerciais, administrativas e habitacionais, o que evita a mistura desordenada.",
        ]
        return random.choice(frases)

