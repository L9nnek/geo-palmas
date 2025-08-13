import json
from pathlib import Path
from typing import Dict, Optional


class Palmas:
    def __init__(self, data_path: Optional[str] = None) -> None:
        """Carrega os dados de quadras a partir de um arquivo JSON."""
        if data_path is None:
            data_path = Path(__file__).resolve().parent / "data" / "quadras.json"
        else:
            data_path = Path(data_path)

        with data_path.open(encoding="utf-8") as f:
            self.quadras: Dict[str, Dict[str, str]] = json.load(f)
