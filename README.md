# PNA Chatbot 🤖

O **PNA Chatbot** é uma aplicação web de chat interativo construída em Python utilizando o framework **Streamlit** e integrada à API oficial da **Google GenAI**. O sistema é capaz de manter o contexto de conversas contínuas em tempo real, utilizando a inteligência do modelo **Gemini 2.5 Flash**.

---

## 🚀 Funcionalidades

* **Histórico em Tempo Real:** Mantém o contexto de toda a conversa na sessão atual (você pode referenciar mensagens anteriores e a IA lembrará).
* **Interface Fluida:** Componentes nativos de chat do Streamlit (`st.chat_input` e `st.chat_message`) para uma experiência visual limpa e responsiva.
* **Segurança Baseada em TOML:** Gerenciamento seguro da chave de API através do ecossistema de *Secrets* do Streamlit, evitando a exposição de credenciais no GitHub.

---

## 🛠️ Tecnologias Utilizadas

* [Python](https://www.python.org/) (Linguagem base)
* [Streamlit](https://streamlit.io/) (Interface Frontend e Servidor)
* [Google GenAI SDK](https://github.com/google/generative-ai-python) (Integração com o modelo Gemini)
* [Gemini 2.5 Flash](https://ai.google.dev/) (Modelo de Linguagem de Alta Performance e Baixa Latência)

---

## 📦 Como Executar o Projeto Localmente

### 1. Clonar o Repositório
```bash
git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
cd NOME_DO_REPOSITORIO
```
### Instalar as Dependências
```bash
pip install streamlit google-genai
```
### 3. Configurar as Credenciais (Secrets)
Para que a aplicação funcione com segurança sem expor sua chave de API, siga estes passos:

Na raiz do projeto, crie uma pasta chamada .streamlit/.

Dentro dessa pasta, crie um arquivo chamado secrets.toml.

Adicione a sua chave de API do Google AI Studio da seguinte forma:
# .streamlit/secrets.toml
GEMINI_API_KEY = "SUA_CHAVE_DE_API_AQUI"

⚠️ **Nota**: A pasta .streamlit/ já está incluída no arquivo .gitignore para garantir que suas credenciais privadas nunca sejam enviadas para o repositório público.

### 4. Rodar a Aplicação
Execute o servidor do Streamlit com o comando:
```bash
streamlit run my_ai.py
```
A aplicação abrirá automaticamente no seu navegador padrão no endereço http://localhost:8501.

---
Desenvolvido com atenção e dedicação. Sinta-se livre para contribuir com melhorias, abrir issues ou enviar pull requests!