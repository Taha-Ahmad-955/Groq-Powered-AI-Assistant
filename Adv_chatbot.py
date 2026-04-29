from langchain_core.prompts import ChatPromptTemplate  
from langchain_core.output_parsers import StrOutputParser  
from langchain_groq import ChatGroq  
import streamlit as st  
import os  
from dotenv import load_dotenv 

load_dotenv()


# Sets page title and layout
st.set_page_config(page_title="My Groq Assistant", layout="centered")

# Display heading
st.title("My Assistant 🤖")


# st.markdown is used to render HTML/CSS
# unsafe_allow_html=True allows raw HTML (needed for styling)
st.markdown("""
    <style>
    .reportview-container {
        background-color: #f5f5f5; /* Light grey background */
    }
    .stTextInput>div>div>input {
        font-size: 18px; /* Bigger input text */
    }
    </style>
""", unsafe_allow_html=True)


# Initialize chat history if it doesn't already exist
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        ("system", "You are a helpful AI assistant. Respond clearly and concisely.")
    ]


# Slider allows user to control randomness of model
temperature = st.slider("🔧 Set Model Temperature", 0.0, 1.0, 0.7)

# Show current temperature (for understanding/debugging)
st.write(f"Current Temperature: {temperature}")


# ChatGroq connects to Groq API model
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),  # Fetch API key securely
    model_name="openai/gpt-oss-120b",  # Groq model
    temperature=temperature  # Controls randomness
)

# Converts output into simple string
output_parser = StrOutputParser()


# When clicked → reset chat history
if st.button("🗑️ Clear Chat"):
    st.session_state.chat_history = [
        ("system", "You are a helpful Teaching AI assistant. You have to teach Coding and Physics. Explain each topic with clear examples and give references of your response. Respond clearly and concisely. Answer lists in bullet points.")
    ]
    st.rerun()  # Refresh UI instantly


# Loop through each message and display it
# Loop through stored chat messages and display them differently based on who sent them (user or bot)
for role, message in st.session_state.chat_history:

    if role == "user":
        st.markdown(f"**You:** {message}")  # Show user message

    elif role == "assistant":
        st.markdown(f"**Bot:** {message}")  # Show bot reply


# Form ensures input + button are linked
with st.form("chat_form", clear_on_submit=True):

    # Text input box
    user_input = st.text_input("💬 Type your message here", key="user_input")

    # Submit button
    submitted = st.form_submit_button("Send")


# Runs only when user sends message
if submitted and user_input:

    # Save user message to memory
    st.session_state.chat_history.append(("user", user_input))

    # Convert full chat history into structured prompt
    prompt = ChatPromptTemplate.from_messages(st.session_state.chat_history)

    # Prompt → Model → Output Parser
    chain = prompt | llm | output_parser


    # Spinner shows loading animation
    with st.spinner("🤔 Thinking..."):

        try:
            # Send prompt to model and get response
            response = chain.invoke({})

            # Save response in memory
            st.session_state.chat_history.append(("assistant", response))

            # Rerun app to refresh UI and display response
            st.rerun()

        except Exception as e:
            # If error occurs, show it as message
            st.session_state.chat_history.append(("assistant", f"Error: {e}"))
            st.rerun()