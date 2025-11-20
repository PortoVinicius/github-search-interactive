📘 GitHub Search Simulator (Interactive + Docker)

Um pequeno programa interativo que roda dentro do Docker e permite buscar repositórios no GitHub digitando palavras-chave diretamente no terminal — igual um “simulador” de busca inspirado no estilo do nosso simulador OBD2, mas agora voltado para explorar projetos no GitHub.

🚀 Características

🔍 Busca repositórios no GitHub pela palavra que você digitar

💬 Interface interativa: o programa fica esperando comandos

⭐ Mostra Stars, URL e Descrição dos 5 melhores repositórios

🐳 Executado totalmente dentro de um container Docker

🧩 Código simples em Python (requests + loops)

🛑 Comando exit para sair do simulador



📂 Estrutura do projeto

github-search-interactive/
│
├── Dockerfile
├── search.py
└── README.md


📥 Como instalar e rodar
1. Clone este repositório (ou crie a pasta manualmente)
```bash
git clone https://github.com/seu-nome/github-search-interactive
cd github-search-interactive
```
2. Build da imagem Docker
```bash
docker build -t github-search-sim .
```
🛠 Como usar
```bash
GitHub Search Simulator Started. Type 'exit' to quit.
Enter search term:
```
Digite qualquer palavra, por exemplo:
```bash
flask
```
A saída será algo assim:
```bash
📌 flask
⭐ Stars: 65000
🔗 URL: https://github.com/pallets/flask
📝 Description: The Python micro framework for building web applications
```
Para fechar o simulador.
```bash
exit
```


🤝 Contribuições
Sinta-se à vontade para melhorar o código ou abrir ideias novas.
Este é um projeto inicial para aprendizado e exploração da API do GitHub.



