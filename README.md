Groq-Powered AI Assistant

A responsive and customizable AI chatbot built using Streamlit and LangChain, powered by Groq’s high-performance language models. This assistant is designed to provide clear, structured, and educational responses with a focus on coding and physics concepts.

Overview

This project demonstrates how to build a conversational AI interface that maintains context, adapts response style, and allows real-time control over model behavior. It integrates modern LLM tooling with a clean user interface to create an interactive learning assistant.

Features
Context-aware conversation with persistent chat history
Adjustable model temperature for response control
Structured and concise answers with teaching-oriented prompts
Focused assistance in coding and physics topics
Clean and responsive Streamlit interface
Secure API key handling using environment variables
One-click chat reset functionality
Technologies Used
Python
Streamlit
LangChain
LangChain Core
LangChain Groq
python-dotenv
Installation

Follow these steps to set up the project locally:

Clone the repository:
git clone https://github.com/your-username/groq-assistant.git
Navigate to the project directory:
cd groq-assistant
Create a virtual environment:
python -m venv venv
Activate the virtual environment:

On Windows:

venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate
Install the required dependencies:
pip install -r requirements.txt
Environment Setup

Create a .env file in the root directory and add your Groq API key:

GROQ_API_KEY=your_api_key_here
Running the Application

Launch the Streamlit app using:

streamlit run your_filename.py

Replace your_filename.py with the name of your script file.

How It Works
The application initializes a chat interface using Streamlit
User input is stored in session state to preserve conversation history
Chat history is converted into a structured prompt using LangChain
The prompt is processed by a Groq-hosted large language model
Responses are parsed and displayed dynamically
Users can adjust temperature to control creativity and randomness
Use Cases
Learning programming concepts with guided explanations
Understanding physics topics with structured breakdowns
Experimenting with prompt engineering and LLM behavior
Building interactive AI-powered applications
Future Improvements
Streaming responses for real-time output
Integration of voice input and output
Support for multiple model selection
Enhanced UI/UX with chat bubbles and themes
Export or save chat history
Contributing

Contributions are welcome. Feel free to fork the repository and submit improvements through pull requests.

