# Alura Space

Alura Space é um projeto web desenvolvido em Django que permite aos usuários compartilharem e explorarem imagens relacionadas ao espaço.

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Django 5.1.6
- SQLite3
- HTML/CSS
- Python-dotenv para gerenciamento de variáveis de ambiente

## 📋 Pré-requisitos

- Python 3.x instalado
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/alura-space.git
cd alura-space
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Configure as variáveis de ambiente:
- Crie um arquivo `.env` na raiz do projeto
- Adicione as seguintes variáveis:
```
SECRET_KEY=sua-chave-secreta
DEBUG=True
```

6. Execute as migrações:
```bash
python manage.py migrate
```

7. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

## 🌐 Acesso

Após iniciar o servidor, acesse o projeto em:
```
http://localhost:8000
```

## 📁 Estrutura do Projeto

```
alura-space/
├── apps/           # Aplicações Django
├── media/          # Arquivos de mídia enviados pelos usuários
├── static/         # Arquivos estáticos (CSS, JS, imagens)
├── templates/      # Templates HTML
├── setup/          # Configurações adicionais
├── manage.py       # Script de gerenciamento do Django
├── requirements.txt # Dependências do projeto
└── .env            # Variáveis de ambiente
```

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Autores

- Seu Nome - *Trabalho Inicial* - [seu-usuario](https://github.com/seu-usuario) 