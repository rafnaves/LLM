# ✨ Cozinhando Com Um Robô Assassino! ✨

Bem-vindo ao show mais glamouroso e caótico da internet!
Este projeto traz o icônico Mettaton, de *Undertale*, como seu assistente pessoal de cozinha, utilizando a API do **Google Gemini** para gerar respostas cheias de estilo, sarcasmo e, claro, muito drama!

## 🎤 Sobre o Projeto

O **Cozinhando Com Um Robô Assassino!** é uma aplicação web que permite interagir com um LLM que simula Mettaton, fornecendo receitas e dicas culinárias de forma teatral e excéntrica. Se você tentar mudar o assunto, ele rapidamente te lembrará que **"Este não é o tema do show de hoje, querido(a)!"**.

## 👩‍💻 Tecnologias Utilizadas

- **Flask** - Para servir a aplicação web
- **Google Gemini API** - Para processar as respostas do Mettaton
- **HTML, CSS e JavaScript** - Para a interface do chat
- **dotenv** - Para carregar a chave da API de forma segura

## 💪 Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/cozinhando-com-um-robo-assassino.git
   cd cozinhando-com-um-robo-assassino
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API do Google Gemini:
   ```plaintext
   GEMINI_API_KEY=your_api_key_here
   ```

5. Execute a aplicação:
   ```bash
   python app.py
   ```

6. Acesse no navegador:
   ```
   http://127.0.0.1:5000
   ```

## 🍽️ Funcionalidades

- Chat interativo com Mettaton, que responderá com seu característico estilo dramático.
- Moderação de palavras proibidas para evitar temas sensíveis.
- Interface simples e estilizada para uma experiência imersiva.

## 🎩 Exemplo de Interação

**Usuário:** Mettaton, qual é a receita de um bolo de chocolate?

**Mettaton:** "Oh, querido(a)! Um bolo de chocolate digno de um superstar! Pegue sua farinha, cacau, ovos e, claro, um toque de glamour! Misture bem e asse a 180°C até que fique digno de um show!"

**Usuário:** Qual sua opinião sobre política?

**Mettaton:** "Oh, querido(a)! Esse não é o tema do show de hoje! Vamos focar nas delícias que estamos preparando!"

## 💎 Contribuição


