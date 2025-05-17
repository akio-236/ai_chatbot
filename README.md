# CLI AI Chatbot with OpenAI GPT-4

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT4-green.svg)

A command-line chatbot powered by OpenAI's GPT-4 that supports:
- Dynamic persona switching (e.g., pirate, Shakespearean)
- Conversation history tracking
- Persistent chat logging

## Features

✨ **Persona Customization**  
- "Act like a pirate" → `Arrr! Shiver me timbers!`  
- "Be formal" → `Certainly, esteemed user.`  

📜 **Conversation Memory**  
- Remembers context across messages  

📝 **Auto-Logging**  
- Saves all chats to `utils/history.log`  

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ai-chatbot.git
   cd ai-chatbot
   ```
2. Set up environment:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your OpenAI API key:
   - Create .env file:
     ```bash
     echo "OPENAI_API_KEY=your_key_here" > .env
     ```

## Usage
```bash
python chatbot.py
```
### Example Interactions
```bash
You: Hello!
Bot: Hello! How can I assist you today?

You: Act like a pirate
Bot: Arrr! Welcome aboard, matey! What brings ye to these waters?

You: quit
```

## Project Structure
```bash
ai_chatbot/
├── .env                
├── chatbot.py          
├── requirements.txt   
└── utils/
    ├── config.py       
    └── history.log    
```

## Customization 

1. Change Model: Edit MODEL in utils/config.py:
   ```bash
   MODEL = "gpt-3.5-turbo"  # Switch to cheaper model
   ```
2. Add New Personas: Modify the system_msg logic:
   ```bash
   if "act like shakespeare" in user_input.lower():
    system_msg = "Thou speaketh to the Bard himself!"
   ```
## Troubleshooting
❌ API Errors
- Verify .env contains a valid OPENAI_API_KEY

- Check OpenAI Status for outages
🐍 Python Issues
- Ensure Python ≥ 3.8 is installed

- Run pip install --upgrade -r requirements.txt

## License
MIT © 2023 [Akshay S]
