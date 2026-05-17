# primeiro passo: título do sistema (visível na parte superior da página)
#campo de mensagens (input do chat)
# cada mensagem que o user mandar deve:
    # mostrar a mensagem que o user mandou no chat
    # pegar a pergunta e enviar para uma IA responder
    # exibir a resposta da IA na tela

# Para criar o frontend e o backend com python -> streamlit
# A IA que será utilizada -> GenAI

import streamlit as st
from google import genai

# Para usar a API da Google, precisamos importar os tipos de conteúdo que ela espera
from google.genai import types

# 1. O cliente SEMPRE é recriado a cada atualização da página para evitar conexões fechadas
modelo_ia = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

st.title("PNA Chatbot")

# 2. Inicializamos uma lista simples para guardar o histórico bruto no formato da Google
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# 3. Mostrar o histórico na tela (convertendo os papéis da Google para o Streamlit)
for message in st.session_state["chat_history"]:
    role = "user" if message.role == "user" else "assistant"
    if message.parts and message.parts[0].text:
        st.chat_message(role).write(message.parts[0].text)

# Campo de entrada de mensagens
user_text = st.chat_input("Digite a sua mensagem")

if user_text:
    # Exibir a mensagem do usuário imediatamente na tela
    st.chat_message("user").write(user_text)
    
    # Criar o objeto de conteúdo do usuário no formato estrito que a API exige
    user_content = types.Content(
        role="user",
        parts=[types.Part.from_text(text=user_text)]
    )
    
    # Adicionar a mensagem do usuário ao histórico da sessão
    st.session_state["chat_history"].append(user_content)
    
    try:
        # 4. Enviamos TODO o histórico acumulado usando um cliente novo e ativo
        response = modelo_ia.models.generate_content(
            model="gemini-2.5-flash",
            contents=st.session_state["chat_history"]
        )
        
        answer_text = response.text
        
        # Exibir a resposta da IA na tela
        st.chat_message("assistant").write(answer_text)
        
        # Criar o objeto de conteúdo da IA no formato correto
        model_content = types.Content(
            role="model",
            parts=[types.Part.from_text(text=answer_text)]
        )
        
        # Adicionar a resposta da IA ao histórico da sessão
        st.session_state["chat_history"].append(model_content)
    
    #Tratar erros de API para evitar que a aplicação quebre
    except Exception as e:
        st.error(f"Erro na API: {e}")