# 📧 Email Sender + Rastreamento de Abertura

Sistema para envio de e-mails com **rastreamento de abertura** usando um **pixel invisível**. Ideal para testar campanhas e-mails com pixel de rastreamento em ambientes de teste.

![Badge](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Badge](https://img.shields.io/badge/SMTP-%F0%9F%94%A5-orange)
![Badge](https://img.shields.io/badge/Python-%F0%9F%92%BB-blue)
![Badge](https://img.shields.io/badge/Tracking-%F0%9F%94%B9-blue)

---

## ✅ Funcionalidades

- 📬 Envio de e-mails com **HTML**
- 📊 **Pixel de rastreamento** (open pixel 1x1) para detectar aberturas
- 🔗 Registro de **abertura de e-mails** em um arquivo JSON
- 🐳 **Rastreador de e-mails** feito com **FastAPI** para servir o pixel

---

## 🧩 Estrutura do Projeto

```
email_tracker/
├── main.py            # Servidor FastAPI com rastreamento
├── send_email.py      # Script para envio de e-mails com pixel
├── emails.json        # Logs de aberturas
├── requirements.txt   # Dependências
└── README.md          # Este arquivo
```

---

## 🚀 Como Usar

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Rodar o Servidor de Rastreamento

Execute o servidor `FastAPI` que servirá o pixel de rastreamento:

```bash
python -m uvicorn main:app --reload
```

Isso vai iniciar o servidor em `http://127.0.0.1:8000`.

### 3. Enviar o E-mail com Pixel de Rastreamento

Edite o arquivo `send_email.py` com suas credenciais e execute:

```bash
python send_email.py
```

### 4. Verificar Logs de Abertura

O arquivo `emails.json` será atualizado com informações de quando e de qual **user-agent** o e-mail foi aberto.

---

## 🧪 Tecnologias Usadas

- **FastAPI**: Para criar o servidor que serve o pixel de rastreamento.
- **smtplib**: Para enviar e-mails via SMTP.
- **JSON**: Para armazenar as informações de rastreamento de abertura.

---

## 📄 Licença

MIT — livre para usar, estudar e modificar.
