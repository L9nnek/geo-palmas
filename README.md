# 🗺️ GeoPalmas

Conversor de endereços antigos e atuais de **Palmas - TO**.  
Ideal para quem precisa alternar entre siglas como ARNO, ARSO e quadras numéricas sem complicação.

# 💡 Prévia

<img width="381" alt="image" src="https://github.com/user-attachments/assets/a79dd565-517f-434d-8104-f2e01a7c9af1" />

---

## 📦 Instalação

```bash
git clone https://github.com/L9nnek/geo-palmas.git
cd geo-palmas
```

---

## ▶️ Execução

- **Linux/macOS**
  ```bash
  python3 main.py
  ```

- **Windows**
  ```bash
  py main.py
  ```

---

## 📁 Dados das quadras

Os mapeamentos entre siglas e endereços ficam em `data/quadras.json` no formato:

```json
{
  "arno": { "ARNO 12": "AE 105 Norte" },
  "arne": { "ARNE 12": "106 Norte" },
  "arse": { "ARSE 12": "106 Sul" },
  "arso": { "ARSO 12": "105 Sul" }
}
```

Cada chave principal representa uma região da cidade e contém as conversões específicas.

---

## ✅ Requisitos

- Python 3.7 ou superior

---

## 📝 Licença

MIT
