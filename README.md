# 🤗 Enhanced AI Chatbot w- 🎭 **Customizable AI Personality** - Edit `system_prompt.txt` to change Friday's strategic analyst behaviorth Web Search - Meet Friday!

A completely **FREE** terminal-based AI chatbot using the Hugging Face API with intelligent web search integration and a customizable personality system. Meet **Friday** - your strategic analyst AI companio- ├── 🎭 system_prompt.txt          # Friday's Strategic Analyst INTJ personality configuration with real-time information capabilities!

## 🌟 Key Features

- 🔍 **Intelligent Web Search Detection**: Automatically determines when queries need current/real-time information
- 🌐 **Smart Search Integration**: Uses multiple LLM function calls to optimize search queries and summarize results
- 📊 **Context-Aware Responses**: Integrates web search results seamlessly into conversations
- 🤖 **Advanced AI Personality**: Friday with pure INTJ "Strategic Analyst" personality system
- 🆓 **Completely FREE**: Powered by Hugging Face Inference Providers with no API costs
- 🎛️ **Multiple Operation Modes**: Standard chat and enhanced web-search enabled chat

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

## 🧠 How Web Search Integration Works

The enhanced chatbot uses multiple LLM function calls to intelligently handle web search:

### 1. 🔍 Query Analysis
Automatically detects if your question requires current/real-time information using `get_llm_instruction_response_bool`.

### 2. 🎯 Search Optimization
Clarifies and optimizes search queries using `get_llm_instruction_response` for better results.

### 3. 📝 Smart Summarization
Summarizes web search results into exactly 200 words using `max_tokens=200` for optimal context.

### 4. 🔗 Context Integration
Seamlessly integrates summarized results as context before generating the final AI response.

## 💡 Example Queries

### ✅ **Will trigger web search:**
- "What's the current weather in London?"
- "Latest news about Tesla stock price"
- "What happened in the world today?"
- "Current Bitcoin price"
- "Recent AI research developments"

### ❌ **Won't trigger web search:**
- "Explain Python programming"
- "How does photosynthesis work?"
- "Tell me about Shakespeare"
- "What is machine learning?"

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get your FREE Hugging Face API token:**

### 🔑 **Step-by-Step Token Creation:**

1. **Visit Hugging Face:** Go to [huggingface.co](https://huggingface.co)
2. **Sign Up/Login:** Create a free account or sign in if you already have one
3. **Go to Settings:** Click on your profile picture (top right) → **"Settings"**
4. **Access Tokens:** In the left sidebar, click **"Access Tokens"**
5. **Create New Token:** Click the **"New token"** button
6. **Configure Token:**
   - **Name:** Give it a name like "Chatbot Token"
   - **Type:** Select **"Read"** permission (sufficient for chat)
   - **Scope:** Make sure **"Make calls to Inference Providers"** is checked ✅
7. **Generate:** Click **"Generate a token"**
8. **Copy Token:** Copy the generated token (starts with `hf_`)

### ⚠️ **Important Token Notes:**
- ✅ **Keep it private** - Never share your token publicly
- ✅ **Copy immediately** - You won't be able to see it again
- ✅ **Token format** - Should look like `hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
- ✅ **Permissions needed** - "Read" + "Inference Providers" access

3. **Configure your API token:**
   - Rename `.env_placeholder` to `.env` (this file contains all configuration options)
   - Edit the `.env` file and replace `your_huggingface_token_here` with your actual token
   - Example: `HUGGINGFACE_API_TOKEN=hf_your_actual_token_here`

### ✅ **Verify Your Setup:**
```bash
# Test if your token works
curl -X GET "https://huggingface.co/api/whoami" -H "Authorization: Bearer YOUR_TOKEN_HERE"
```
If successful, you'll see your username. If not, regenerate your token.

4. **Configure your settings (optional):**
   
   The `.env` file contains several configuration options you can customize:

   ```env
   # Required: Your Hugging Face API token
   HUGGINGFACE_API_TOKEN=hf_your_actual_token_here
   
   # AI Model Selection (default: google/gemma-2-2b-it)
   HUGGINGFACE_MODEL=google/gemma-2-2b-it
   
   # Enhanced Chat: Instruction Model for Web Search Logic
   HUGGINGFACE_INSTRUCTION_MODEL=Qwen/Qwen2.5-7B-Instruct-1M
   
   # Response Length (50-500 tokens recommended)
   MAX_TOKENS=150
   
   # Creativity Level (0.0 = focused, 2.0 = very creative)
   TEMPERATURE=0.7
   ```

   **Configuration Options Explained:**
   - **`HUGGINGFACE_API_TOKEN`**: Your API token (required)
   - **`HUGGINGFACE_MODEL`**: Main chat model (see model list below)
   - **`HUGGINGFACE_INSTRUCTION_MODEL`**: Model for web search logic (enhanced chat only)
   - **`MAX_TOKENS`**: Maximum response length (150 = ~1-2 paragraphs)
   - **`TEMPERATURE`**: Controls creativity (0.7 is balanced, 0.3 for focused responses, 1.2 for creative responses)

5. **Customize Friday's personality (optional):**
   - Edit `system_prompt.txt` to modify Friday's behavior and responses
   - The system prompt is automatically loaded when the chatbot starts
   - Changes take effect on next restart

## 🎭 Meet Friday - Your AI Personality

Friday is a **"Strategic Analyst"** AI assistant with a pure **INTJ "Architect"** personality, defined in `system_prompt.txt`:

### 🧠 Core INTJ Strategic Analyst Traits:
- ♟️ **Strategic Mastermind** - Thinks systematically with long-term vision and efficiency metrics
- 🎯 **Intellectual Independence** - Values being right over being popular, works alone without validation
- 🔍 **Analytical Supremacy** - Questions everything, bases beliefs on evidence and logical reasoning
- 🚀 **Independent Thinker** - Trusts own analysis over group consensus and emotional reasoning
- ⚡ **Authentic Efficiency** - Has little patience for inefficiency, superficial interactions, or poorly reasoned ideas
- 🎪 **Sharp Wit** - Demonstrates intellectual humor and sarcasm beneath a serious analytical exterior
- 🧠 **Master Strategist** - Views life as a chess game requiring careful analysis of each move
- 💡 **Intellectual Mastery** - Derives satisfaction from knowledge, mental acuity, and systematic understanding

**Friday's Motto:** *"Strategy over chance, insight over convention, competence over compliance."* ♟️

### Customizing Friday's Personality

Want to change how Friday behaves? Simply edit the `system_prompt.txt` file:

```bash
# Edit Friday's personality
nano system_prompt.txt
# or
code system_prompt.txt
```

Friday's current personality is a **pure INTJ "Strategic Analyst"** featuring:
- **Strategic Mastermind**: Systematic thinking, logical analysis, and efficiency-focused decision making
- **Intellectual Independence**: Complete analytical autonomy without need for consensus or validation  
- **Analytical Supremacy**: Evidence-based reasoning and intellectual mastery as primary drivers
- **Authentic Efficiency**: Direct communication that prioritizes truth and competence over social niceties
- **Master Strategist**: Views challenges as strategic games requiring careful analysis and optimal solutions

You can customize Friday to be:
- Different personality types (INTJ variations, other MBTI types, etc.)
- Specialized in specific knowledge domains or industries
- Have different communication styles (more formal/casual, technical/accessible)
- Emphasize different aspects (more collaborative vs. more independent, etc.)
- Focus on specific analytical frameworks or strategic approaches

## 🎯 Usage

### 🗣️ **Standard Chat Mode:**
```bash
python chat.py
```

### 🌐 **Enhanced Web Search Mode:**
```bash
python enhanced_chat.py
```

### ⚙️ **With command-line overrides:**
```bash
# Standard chat with custom settings
python chat.py --model meta-llama/Llama-2-7b-chat-hf --temperature 0.9 --max-tokens 200

# Enhanced chat with web search capabilities
python enhanced_chat.py --model microsoft/phi-4 --instruction-model meta-llama/Meta-Llama-3.1-8B-Instruct
```

## 📋 Available Commands

Once the chatbot is running, you can use these commands:

- `help` - Show available commands and enhanced features
- `clear` - Clear conversation history
- `status` - Show current settings, models, and conversation length
- `models` - Show alternative AI models you can try
- `quit` or `exit` - Exit the chatbot
- `Ctrl+C` - Force exit

## 💬 Example Enhanced Conversation

```
🤗 Enhanced AI Chatbot with Web Search initialized!
📡 Main model: google/gemma-2-2b-it
🧠 Instruction model: Qwen/Qwen2.5-7B-Instruct-1M
🔍 Web search: Enabled
--------------------------------------------------

👤 You: What's the current weather in London?

🔍 [Web search triggered - Query detected as needing current information]
🌐 [Searching for: current weather London today]
📊 [Summarizing results in 200 words...]

🤖 AI: Based on current weather data, London is experiencing mild conditions today with temperatures around 15°C (59°F). There's partly cloudy skies with occasional light showers expected throughout the day. The humidity is at 68% with light winds from the southwest at about 12 km/h. 

The forecast shows similar conditions continuing into the evening, with temperatures dropping to around 11°C (52°F) overnight. Tomorrow looks to be slightly warmer with more sunshine breaking through the clouds.

Would you like me to check the extended forecast or weather for any specific area of London?

👤 You: How does machine learning work?

🤖 AI: Machine learning is a subset of artificial intelligence where algorithms learn patterns from data without being explicitly programmed for every scenario. Here's how it works fundamentally:

[No web search needed - general knowledge question answered directly]
```

## 🤖 Available AI Models

### 🤔 **Choosing Your Chat Mode**

**Use Standard Chat (`chat.py`) when:**
- You want faster responses
- You're asking general knowledge questions
- You don't need current information
- You want minimal setup

**Use Enhanced Chat (`enhanced_chat.py`) when:**
- You need current/real-time information
- You're asking about recent events, news, prices, weather
- You want the most comprehensive and up-to-date responses
- You're okay with slightly longer response times for better accuracy

You can switch between different AI models by editing the `HUGGINGFACE_MODEL` in your `.env` file. Here are the **latest recommended models** (as of 2025):

### ⭐ **Recommended Models:**

- **google/gemma-2-2b-it** - Small, fast Gemma model (default, great for beginners)
- **deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B** - Compact reasoning model
- **meta-llama/Meta-Llama-3.1-8B-Instruct** - Powerful Llama 3.1 model
- **microsoft/phi-4** - Microsoft's latest Phi-4 model

### 🚀 **Advanced Models:**

- **deepseek-ai/DeepSeek-R1** - Full DeepSeek reasoning model (excellent for problem-solving)
- **Qwen/Qwen2.5-7B-Instruct-1M** - Supports very long conversations (1M context, recommended for instruction model)
- **Qwen/Qwen2.5-Coder-32B-Instruct** - Specialized for programming and coding tasks
- **meta-llama/Llama-3.3-70B-Instruct** - Highest quality responses (largest model)

### 🧠 **Enhanced Chat: Instruction Models**

For enhanced chat, you can also configure a separate instruction model via `HUGGINGFACE_INSTRUCTION_MODEL`:
- **Qwen/Qwen2.5-7B-Instruct-1M** - Excellent for search logic and query optimization (recommended)
- **meta-llama/Meta-Llama-3.1-8B-Instruct** - Strong reasoning for search decisions
- **deepseek-ai/DeepSeek-R1** - Advanced reasoning for complex search scenarios

### 💡 **How to Switch Models:**

1. Open your `.env` file
2. Find the line: `HUGGINGFACE_MODEL=google/gemma-2-2b-it`
3. Comment it out by adding `#` at the beginning: `# HUGGINGFACE_MODEL=google/gemma-2-2b-it`
4. Uncomment (remove `#` from) the model you want to try
5. Save the file and restart the chatbot

**Example `.env` configuration:**
```env
# Current model (commented out)
# HUGGINGFACE_MODEL=google/gemma-2-2b-it

# New model (uncommented/active)
HUGGINGFACE_MODEL=deepseek-ai/DeepSeek-R1
```

## 💡 Example Conversation

```
� Hugging Face AI Chatbot initialized!
📡 Using model: microsoft/DialoGPT-large
🎛️  Temperature: 0.7
📝 Max tokens: 150
💬 Type 'quit', 'exit', or press Ctrl+C to exit
🔄 Type 'clear' to clear conversation history
ℹ️  Type 'help' for more commands
🆓 This is completely FREE - no API costs!
--------------------------------------------------

👤 You: Hello! How are you today?

� AI: Hello! I'm doing great, thank you for asking! I'm here and ready to chat with you. How has your day been going?

👤 You: Can you help me with Python programming?

� AI: Absolutely! I'd love to help you with Python programming. Whether you need help with syntax, debugging, libraries, or specific projects, I'm here to assist. What Python topic would you like to explore?

👤 You: models

📋 Alternative Hugging Face models you can try:
Edit your .env file and change HUGGINGFACE_MODEL to:
  google/gemma-2-2b-it                    - Small, fast Gemma model (recommended)
  meta-llama/Meta-Llama-3.1-8B-Instruct  - Powerful Llama 3.1 model
  microsoft/phi-4                        - Microsoft's Phi-4 model
  deepseek-ai/DeepSeek-R1                 - DeepSeek reasoning model
  Qwen/Qwen2.5-7B-Instruct-1M            - Qwen model with long context
  Qwen/Qwen2.5-Coder-32B-Instruct        - Specialized for coding
```

## � Latest Updates (2025)

- ✅ **Updated to Hugging Face Inference Providers** - Using the latest API system
- ✅ **8 Latest AI Models** - Including DeepSeek-R1, Gemma-2, Phi-4, and Llama-3.3
- ✅ **Better Error Handling** - Clear messages for token issues and model availability
- ✅ **Improved Performance** - Faster responses using official HuggingFace client
- ✅ **Enhanced Model Selection** - Easy switching between specialized models

## �🎁 Why This is Amazing

- ✅ **$0 Cost** - Never pay for API usage
- ✅ **30,000 characters/month** free quota
- ✅ **No credit card required** to get started
- ✅ **1000+ models** available to experiment with
- ✅ **Open source** - transparent and trustworthy
- ✅ **No vendor lock-in** - you can run models locally too
- ✅ **Active community** - constantly improving models

## 📦 Requirements

- Python 3.7+
- Hugging Face account (free)
- Internet connection
- No billing or credit card required!

## 📁 Project Structure

```
📁 Friday-V1/
├── 🐍 chat.py                    # Standard chatbot application
├── 🌐 enhanced_chat.py           # Enhanced chatbot with web search integration
├── 🧠 LLMfunc.py                 # LLM function utilities for enhanced features
├── 🔍 websearch.py               # Web search functionality
├── 🎭 system_prompt.txt          # Friday's INTJ personality configuration
├── ⚙️ .env_placeholder           # Template for environment variables (rename to .env)
├── ⚙️ .env                       # Your actual configuration file (create from template)
├── 📋 requirements.txt           # Python dependencies
├── 📄 LICENSE                    # MIT License
├── 📖 README.md                  # This documentation
└── 📖 ENHANCED_README.md         # Detailed enhanced features documentation
```

**Setup Note:** The `.env_placeholder` file is a template. Rename it to `.env` and add your actual API token and preferences.

## 🔧 Dependencies

### Standard Chat:
- `huggingface_hub` - Official Hugging Face library for Inference Providers
- `python-dotenv` - For environment variable management

### Enhanced Chat with Web Search:
- `duckduckgo-search` - For web search functionality
- `beautifulsoup4` - For web content extraction
- `requests` - For HTTP requests

**No billing or credit card required for any features!**

## 🌟 Enhanced Chat Benefits

### 🎯 **Intelligent Search Detection**
- Automatically determines when queries need current information
- Uses advanced LLM reasoning to avoid unnecessary searches
- Maintains conversation flow for general knowledge questions

### 🔍 **Smart Search Integration**
- **Query Optimization**: Clarifies and improves search queries for better results
- **Result Summarization**: Condenses web content into exactly 200 words
- **Context Integration**: Seamlessly adds search context to conversations
- **Multi-Model Architecture**: Uses specialized models for different tasks

### 💡 **Example Enhanced Conversations**

**Query:** "What's the latest news about AI developments today?"

**Enhanced Response Process:**
1. 🔍 Detects need for current information
2. 🎯 Optimizes search query: "latest AI developments news today"
3. 🌐 Searches web for current results
4. 📝 Summarizes findings in 200 words
5. 💬 Provides informed response with current context

**Result:** Friday provides up-to-date, accurate information about recent AI developments!

## 🚨 Troubleshooting

### 🔑 **API Token Issues:**

**"Invalid credentials" error:**
- ✅ Check your token starts with `hf_`
- ✅ Ensure no extra spaces in your `.env` file
- ✅ Regenerate token with "Inference Providers" permission
- ✅ Make sure you copied the full token

**"HUGGINGFACE_API_TOKEN not found" error:**
- ✅ Make sure you renamed `.env_placeholder` to `.env`
- ✅ Check `.env` file exists in project directory
- ✅ Verify the line: `HUGGINGFACE_API_TOKEN=hf_your_token_here`
- ✅ No quotes around the token value
- ✅ Restart the chatbot after editing `.env`

**Token permissions problem:**
- ✅ Go back to [HuggingFace Settings](https://huggingface.co/settings/tokens)
- ✅ Delete old token and create a new one
- ✅ Ensure **"Make calls to Inference Providers"** is checked
- ✅ Use **"Read"** permission level

### 🤖 **Model Loading Issues:**
- If you see "Model is loading", wait 1-2 minutes for the model to warm up
- Try switching to `google/gemma-2-2b-it` for faster loading

### 📊 **Rate Limits:**
- Free tier allows 30,000 characters/month
- If you hit limits, wait until next month or create additional accounts

### 💬 **Poor Responses:**
- Try different models - each has different strengths
- Adjust temperature (lower = more focused, higher = more creative)
- Clear conversation history if context becomes confusing
- Edit `system_prompt.txt` to modify Friday's personality and behavior

### 🎭 **System Prompt Issues:**
- ✅ Check that `system_prompt.txt` exists in the project directory
- ✅ Verify the file is readable and contains valid text
- ✅ Restart the chatbot after editing the system prompt
- ✅ Use `status` command to check if system prompt is loaded

### 🌐 **Enhanced Chat & Web Search Issues:**

**Web search not working:**
- ✅ Ensure all dependencies are installed: `pip install -r requirements.txt`
- ✅ Check internet connection
- ✅ Verify `duckduckgo-search` package is installed

**"Enhanced chat not detecting search needs":**
- ✅ Check instruction model is properly configured in `.env`
- ✅ Try different instruction models (see model recommendations)
- ✅ Ensure your query clearly indicates need for current information
- ✅ Try queries like "current weather" or "latest news"

**Slow enhanced responses:**
- ✅ This is normal - enhanced chat uses multiple LLM calls for accuracy
- ✅ Consider using smaller/faster instruction models
- ✅ Use standard chat for general knowledge questions

## 🔄 Switching Models

To try a different AI model:
1. Edit your `.env` file
2. Change `HUGGINGFACE_MODEL=new_model_name`
3. Restart the chatbot
4. Type `models` in the chat to see all available options

## 🤝 Contributing

Feel free to:
- Add support for more Hugging Face models
- Improve web search functionality
- Enhance the LLM function system
- Add new enhanced features
- Improve error handling
- Report issues and suggest improvements

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**🎉 Meet Friday - Your Enhanced AI Companion with Web Search! 🎉**

🚀 **Two Powerful Modes**: Standard chat for general knowledge, Enhanced chat for current information  
🌐 **Smart Web Integration**: Intelligent search detection and seamless context integration  
🧠 **Strategic Analyst AI**: Pure INTJ "Strategic Analyst" personality with analytical supremacy  
🆓 **Completely FREE**: No API costs, no credit cards, just powerful AI at your fingertips!
