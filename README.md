# 🤗 Friday AI Chatbot - Enhanced with Web Search

A completely **FREE** terminal-based AI chatbot using the Hugging Face API with intelligent web search integration. Meet **Friday** - your strategic analyst AI companion with customizable INTJ personality.

## 🌟 Features

- 🔍 **Intelligent Web Search**: Automatically detects when queries need current information
- 🤖 **Friday AI Personality**: Strategic INTJ "Analyst" with sharp wit and analytical supremacy
- 🆓 **Completely FREE**: No API costs using Hugging Face Inference Providers
- 🎛️ **Dual Modes**: Standard chat or enhanced web-search enabled chat
- 🔐 **Secure Setup**: API token management via `.env` file
- 💬 **Session Memory**: Conversation history with system prompt preservation
- 🌟 **1000+ Models**: Access to diverse open-source AI models

## 🚀 Latest Updates (2025)

- ✅ **Enhanced Web Search Integration** - Intelligent detection and integration of real-time information
- ✅ **Multi-LLM Function System** - Uses multiple specialized LLM calls for search optimization
- ✅ **Smart Context Summarization** - 200-word summaries of web search results
- ✅ **Dual Chat Modes** - Standard chat and web-search enhanced chat options

## ✨ Features

- 🤖 Interactive terminal-based chat interface with **Friday** - your strategic analyst AI assistant
- 🔍 **Intelligent Web Search**: Automatically detects when queries need current information
- � **Smart Search Integration**: Optimizes search queries and summarizes results in 200 words
- 📊 **Context-Aware Responses**: Seamlessly integrates web search context into conversations
- �🎭 **Customizable AI Personality** - Edit `system_prompt.txt` to change Friday's behavior
- 🆓 **Completely FREE** - no API costs ever!
- 🔐 Secure API token management via `.env` file
- 💬 Conversation history maintained during session (with system prompt preservation)
- 🎛️ Multiple AI models to choose from
- 📋 Built-in commands for managing the chat session
- ⚡ Command-line argument support for quick configuration overrides
- 🔄 Automatic model loading detection and retry logic
- 🌟 Access to 1000+ open-source AI models
- 🏹 **Friday's Personality**: Strategic, analytical, intellectually independent, and ruthlessly efficient!

## 🧠 How Web Search Works

1. **Query Analysis** - Detects if your question needs current information
2. **Search Optimization** - Optimizes search queries for better results
3. **Smart Summarization** - Condenses results into 200-word summaries
4. **Context Integration** - Seamlessly integrates search context into responses

### Web Search Examples
**Will trigger search:** "Current weather in London", "Latest Tesla stock price", "Today's news"
**Won't trigger search:** "Explain Python", "How photosynthesis works", "Tell me about Shakespeare"

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get your FREE Hugging Face API token:**
   - Visit [huggingface.co](https://huggingface.co) and create account
   - Go to Settings → Access Tokens → New token
   - Select "Read" permission + "Make calls to Inference Providers"
   - Copy token (starts with `hf_`)

3. **Configure your API token:**
   - Rename `.env_placeholder` to `.env`
   - Edit `.env` and replace `your_huggingface_token_here` with your token
   - Example: `HUGGINGFACE_API_TOKEN=hf_your_actual_token_here`

## 🎭 Meet Friday - Your AI Personality

Friday is a **Strategic Analyst** AI with pure **INTJ personality**:

- ♟️ **Strategic Mastermind** - Systematic thinking with long-term vision
- 🎯 **Intellectual Independence** - Values being right over being popular  
- 🔍 **Analytical Supremacy** - Evidence-based reasoning and logical analysis
- ⚡ **Authentic Efficiency** - Direct communication, no patience for inefficiency
- 🧠 **Master Strategist** - Views challenges as strategic games requiring optimal solutions

**Friday's Motto:** *"Strategy over chance, insight over convention, competence over compliance."*

### Customize Friday's Personality
Edit `system_prompt.txt` to modify Friday's behavior, communication style, or specialization areas.

## 🎯 Usage

### Standard Chat Mode:
```bash
python chat.py
```

### Enhanced Web Search Mode:
```bash
python enhanced_chat.py
```

### With Custom Settings:
```bash
python chat.py --model meta-llama/Llama-2-7b-chat-hf --temperature 0.9
python enhanced_chat.py --model microsoft/phi-4 --instruction-model meta-llama/Meta-Llama-3.1-8B-Instruct
```

## 📋 Available Commands

- `help` - Show available commands
- `clear` - Clear conversation history
- `status` - Show current settings and models
- `models` - Show alternative AI models
- `quit` or `exit` - Exit chatbot

## 🤖 AI Models

### Recommended Models:
- **google/gemma-2-2b-it** - Fast, lightweight (default)
- **deepseek-ai/DeepSeek-R1** - Excellent reasoning
- **meta-llama/Meta-Llama-3.1-8B-Instruct** - Powerful responses
- **microsoft/phi-4** - Microsoft's latest model

### How to Switch Models:
1. Edit `.env` file
2. Change `HUGGINGFACE_MODEL=new_model_name`
3. Restart chatbot

## 📁 Project Structure

```
Friday-V1/
├── chat.py                    # Standard chatbot
├── enhanced_chat.py           # Enhanced with web search
├── LLMfunc.py                 # LLM utilities
├── websearch.py               # Web search functionality
├── system_prompt.txt          # Friday's personality
├── .env_placeholder           # Config template
├── requirements.txt           # Dependencies
└── README.md                  # Documentation
```

## 🔧 Dependencies

**Standard Chat:**
- `huggingface_hub` - Hugging Face API
- `python-dotenv` - Environment variables

**Enhanced Chat:**
- `duckduckgo-search` - Web search
- `beautifulsoup4` - Content extraction
- `requests` - HTTP requests

## 🚨 Troubleshooting

### API Token Issues:
- Ensure token starts with `hf_`
- Verify no extra spaces in `.env` file
- Check "Inference Providers" permission is enabled
- Rename `.env_placeholder` to `.env`

### Model Loading Issues:
- Wait 1-2 minutes for model warmup
- Try `google/gemma-2-2b-it` for faster loading

### Web Search Issues:
- Install all dependencies: `pip install -r requirements.txt`
- Check internet connection
- Verify instruction model is configured

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Additional AI models
- Enhanced web search functionality
- New personality configurations
- Better error handling

## 📄 License

MIT License - see LICENSE file for details.

---

**🎉 Friday - Your Strategic AI Companion! 🎉**

🚀 **Two Modes**: Standard chat for speed, Enhanced chat for current info  
🧠 **INTJ Personality**: Strategic, analytical, and intellectually independent  
🆓 **Completely FREE**: No API costs, no credit cards required!
