# 📊 Coletor de Dados de Planilhas (.xlsx ou Google Sheets)

O **Coletor de Dados de Planilhas** é um script Python desenvolvido para automatizar a extração e filtragem de informações de planilhas, seja do Google Sheets ou de arquivos locais no formato `.xlsx`.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

## 📝 Descrição

Este projeto permite filtrar registros de planilhas com base em critérios configuráveis, como por exemplo: "retornar os nomes de todos os registros em que a coluna U tenha valor maior ou igual a 1". Toda a configuração é feita de forma prática através de um arquivo `.env`, facilitando a personalização sem necessidade de alterar o código-fonte.

Ideal para analistas de dados, cientistas de dados, profissionais de BI ou desenvolvedores que precisam automatizar processos simples de coleta e limpeza de dados.

## ✨ Funcionalidades

- 📥 Leitura de dados diretamente de planilhas do **Google Sheets** usando API segura
- 📂 Suporte a **planilhas locais** no formato `.xlsx` via `openpyxl`
- 🔍 Filtro por valor mínimo em qualquer coluna (ex: coluna U ≥ 1)
- 📌 Retorno de dados da coluna A (nomes ou identificadores)
- 🛠️ Configuração totalmente personalizada via `.env`
- 🧪 Estrutura modular, fácil de estender ou adaptar
- ❌ Ignora automaticamente linhas incompletas ou mal formatadas

## 🛠️ Tecnologias utilizadas

- Python 3.8+
- `gspread` (acesso ao Google Sheets)
- `openpyxl` (leitura de arquivos Excel)
- `oauth2client` (autenticação com Google)
- `python-dotenv` (leitura de variáveis de ambiente)

## 🚀 Como usar

### Pré-requisitos

- Python 3.8 ou superior instalado
- Conta no Google Cloud Platform (se for usar Google Sheets)
- Arquivo de credenciais do Google Sheets (se for usar Google Sheets)

### Configuração

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/coletor-dados-planilhas.git
cd coletor-dados-planilhas
```
2. Crie um ambiente virtual (opcional mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o arquivo .env com suas preferências:
```ini
# Escolha a fonte dos dados (google_sheets ou local)
DATA_SOURCE=google_sheets

# Configurações para Google Sheets
SPREADSHEET_NAME=NomeDaPlanilha
SHEET_NAME=Página1
COLUMN_TO_FILTER=U
MIN_VALUE=1

# OU Configurações para arquivo local
LOCAL_FILE_PATH=planilha.xlsx
```

### Execução

Execute o script principal:
```bash
python main.py
```
## 📌 **EXEMPLO DE USO**

### 🔢 **Entrada de Dados** (Planilha Original)

| **Nome**       | **Departamento** | **Pontuação** (Coluna U) |
|----------------|------------------|--------------------------|
| Maria Silva    | Financeiro       | 2                        |
| João Mendes    | TI               | 0                        |
| Carla Souza    | RH               | 1.5                      |

### 💻 **Saída do Sistema**

```bash
🌟 **Resultados Filtrados** (Pontuação ≥ 1):
----------------------------------
- MARIA SILVA (Pontuação: 2)
- CARLA SOUZA (Pontuação: 1.5)
```
## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📧 Contato
Para dúvidas ou sugestões, entre em contato pelo email: dinholiro@gmail.com