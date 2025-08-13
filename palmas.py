import json
from pathlib import Path
from typing import Dict, Optional


class Palmas:
    """
    Carrega as quadras a partir de um JSON (dict de dicts) e fornece
    um mapa achatado + lookups normalizados para ambos os sentidos.
    """

    def __init__(self, data_path: Optional[str] = None) -> None:
        if data_path is None:
            data_path = Path(__file__).resolve().parent / "data" / "quadras.json"
        else:
            data_path = Path(data_path)

        with data_path.open(encoding="utf-8") as f:
            # Ex.: {"ARNO": {"ARNO 13": "107 Norte", ...}, "ARSO": {...}, ...}
            self.quadras: Dict[str, Dict[str, str]] = json.load(f)

        # Mapa achatado: {"ARSO 12": "105 Sul", ...}
        self._mapa: Dict[str, str] = {}
        for _grupo, d in self.quadras.items():
            self._mapa.update(d)

        # Normalizações para busca robusta
        self._mapa_norm_upper: Dict[str, str] = {k.upper(): v for k, v in self._mapa.items()}
        self._mapa_inverso_title: Dict[str, str] = {v.title(): k for k, v in self._mapa.items()}

    # --- API pública compatível com ambas as versões ---

    def get_mapa(self) -> Dict[str, str]:
        """Retorna o mapa achatado (sem normalização)."""
        return self._mapa

    def get_mapa_inverso(self) -> Dict[str, str]:
        """Retorna o mapa invertido (valores->chaves), com valores em Title Case."""
        return self._mapa_inverso_title

    def lookup_numerado(self, chave: str) -> Optional[str]:
        """
        Busca por chave tipo 'ARSO 12' (case-insensitive via UPPER).
        Retorna valor tipo '105 Sul' ou None.
        """
        return self._mapa_norm_upper.get(chave.upper())

    def lookup_sigla(self, valor: str) -> Optional[str]:
        """
        Busca por valor tipo '105 Sul' (normalizado para Title Case).
        Retorna chave tipo 'ARSO 12' ou None.
        """
        return self._mapa_inverso_title.get(valor.title())