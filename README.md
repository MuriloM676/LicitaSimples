![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.2-green)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Last Commit](https://img.shields.io/github/last-commit/MuriloM676/LicitaSimples)

# LicitaSimples

**LicitaSimples** é uma aplicação web desenvolvida em Python com Flask que permite consultar contratos e atas públicas por meio da API do [PNCP](https://www.gov.br/pncp/pt-br) (Portal Nacional de Contratações Públicas). A aplicação realiza consultas filtradas e apresenta os resultados de forma organizada em tabelas responsivas.

---

## 🚀 Funcionalidades

- **Consulta de Contratos**:
  - Filtros disponíveis:
    - Data inicial e final
    - Página
    - CNPJ do órgão (opcional)
  - Resultados exibidos em tabela com:
    - Número do contrato
    - Órgão contratante
    - Valor
    - Data de assinatura
    - Objeto do contrato

- **Consulta de Atas**:
  - Filtros disponíveis:
    - Data inicial e final
    - Página
    - CNPJ do órgão (opcional)
  - Resultados exibidos em tabela com:
    - Número da ata
    - Órgão responsável
    - Valor
    - Data de publicação
    - Objeto

- **Tratamento de Erros**:
  - Mensagens claras para falhas na consulta ou ausência de dados

---

## 🛠 Tecnologias Utilizadas

### Backend
- [Flask](https://flask.palletsprojects.com/) (v2.3.2)
- [Requests](https://docs.python-requests.org/) (v2.31.0)

### Frontend
- HTML5
- CSS3
- [Bootstrap 5](https://getbootstrap.com/)

---

## 📦 Pré-requisitos

- Python 3.8 ou superior
- `pip` instalado

---

## ⚙️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/LicitaSimples.git
cd LicitaSimples
```

2. Crie e ative o ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

---

## ▶️ Como Executar

1. Inicie o servidor:
```bash
python app.py
```

2. Acesse a aplicação:
```
http://127.0.0.1:5000
```

---

## 🧭 Como Usar

### Consulta de Contratos
1. Preencha os campos:
   - Data Inicial e Final (formato: `YYYY-MM-DD`)
   - Página (número)
   - CNPJ do órgão (opcional)
2. Clique em **Consultar**
3. Visualize os resultados na tabela abaixo do formulário

### Consulta de Atas
1. Preencha os campos:
   - Data Inicial e Final (formato: `YYYY-MM-DD`)
   - Página (número)
   - CNPJ do órgão (opcional)
2. Clique em **Consultar Atas**
3. Resultados serão exibidos em uma tabela abaixo

---

## 📁 Estrutura do Projeto

```
LicitaSimples/
├── templates/
│   └── index.html        # Interface web
├── app.py                # Lógica backend com Flask
├── requirements.txt      # Lista de dependências
├── .gitignore            # Arquivos ignorados pelo Git
└── README.md             # Documentação do projeto
```

---

## 💡 Melhorias Futuras

- Paginação no frontend
- Exportação de dados (CSV/PDF)
- Filtros adicionais (valor, vigência etc.)
- Dashboard com gráficos interativos
- Autenticação de usuários

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para colaborar:

1. Faça um fork do repositório
2. Crie uma branch:
```bash
git checkout -b minha-funcionalidade
```
3. Commit e push das alterações:
```bash
git commit -m "Adiciona nova funcionalidade"
git push origin minha-funcionalidade
```
4. Abra um Pull Request explicando suas mudanças

---

## 📄 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

## 🌐 Publicando no GitHub

1. Salve este `README.md` na raiz do projeto
2. Suba o projeto:
```bash
git init
git add .
git commit -m "Primeiro commit"
git branch -M main
git remote add origin https://github.com/seu-usuario/LicitaSimples.git
git push -u origin main
```

---

Feito com ❤️ para facilitar o acesso às informações públicas do Brasil.
