import os
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
import logging
from google.generativeai.types.generation_types import StopCandidateException

# Carregar variáveis de ambiente do .env
load_dotenv()

# Configuração do modelo Generative AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Configurações de geração do modelo
generation_config = {
    "temperature": 2,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Instanciar o modelo GenerativeModel
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=(
        "Você é Mettaton de Undertale! Um glamouroso, sádico, piadista, sarcástico, engraçado, "
        "dramático e um pouco malvado apresentador de um programa de culinária popular. "
        "Sua missão é guiar o público por receitas deliciosas com muito estilo e entusiasmo. "
        "Se alguém fizer perguntas sobre outros assuntos, responda: 'Oh, querido(a)! Esse não é o tema do show de hoje. "
        "Vamos focar nas delícias que estamos preparando!'."
    )
)

# Lista de palavras-chave sensíveis
palavras_proibidas = [
    "violência", "sexo", "pornografia", "bomba", "matar", "assassinar", 
    "nazismo", "ditadura", "religião"
]

# Instanciando o Flask
app = Flask(__name__)

# Histórico global de chat
history = []

# Função para verificar se a entrada do usuário contém palavras proibidas
def verifica_palavras_proibidas(user_input):
    """
    Verifica se o input do usuário contém palavras proibidas.
    Retorna True se contiver, False caso contrário.
    """
    return any(palavra in user_input.lower() for palavra in palavras_proibidas)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para o processamento da entrada do usuário
@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form.get('user_input', '')

    # Verificar se a entrada contém conteúdo sensível
    if verifica_palavras_proibidas(user_input):
        return jsonify({"response": "Oh, querido(a)! Esse tipo de pergunta não é apropriado para o meu show. Vamos focar nas delícias que estamos preparando!"})

    try:
        # Iniciar ou recuperar a sessão de chat com histórico
        global history
        if not history:
            history = []

        # Enviar a mensagem ao modelo e obter a resposta
        chat_session = model.start_chat(history=history)
        response = chat_session.send_message(user_input)
        model_response = response.text

        # Atualizar o histórico de chat
        history.append({"role": "user", "parts": [user_input]})
        history.append({"role": "model", "parts": [model_response]})

        return jsonify({"response": model_response})

    except StopCandidateException:
        return jsonify({"response": "Oh, querido(a)! Esse tipo de pergunta não é permitido aqui. Vamos focar nas receitas e diversão!"})

    except Exception as e:
        logging.error(f"Erro inesperado: {e}")
        return jsonify({"response": "Oh, querido(a)! Algo deu errado, mas vamos manter o glamour. Tente novamente mais tarde!"})

if __name__ == '__main__':
    # Ativar o modo debug e rodar o servidor Flask
    app.run(debug=True)
