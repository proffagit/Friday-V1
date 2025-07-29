# 🤗 Hugging Face Terminal Chatbot - Meet Friday!

A completely **FREE** terminal-based AI chatbot using the Hugging Face API with a customizable personality system. Meet **Friday** - you## 🎉 Latest Updates (2025)

- ✅ **Friday AI Personality System** - Meet Friday, your adventurous AI companion with customizable personality
- ✅ **System Prompt Support** - Customize AI behavior via `system_prompt.txt` file
- ✅ **Updated to Hugging Face Inference Providers** - Using the latest API system
- ✅ **8 Latest AI Models** - Including DeepSeek-R1, Gemma-2, Phi-4, and Llama-3.3
- ✅ **Better Error Handling** - Clear messages for token issues and model availability
- ✅ **Improved Performance** - Faster responses using official HuggingFace client
- ✅ **Enhanced Model Selection** - Easy switching between specialized models
- ✅ **Conversation History Preservation** - System prompt maintained across sessionsturous, truth-seeking AI companion!
🤗 Hugging Face AI Chatbot initialized!
📡 Using model: google/gemma-2-2b-itth no usage costs!

## ✨ Features

- 🤖 Interactive terminal-based chat interface with **Friday** - your adventurous AI assistant
- 🎭 **Customizable AI Personality** - Edit `system_prompt.txt` to change Friday's behavior
- 🆓 **Completely FREE** - no API costs ever!
- 🔐 Secure API token management via `.env` file
- 💬 Conversation history maintained during session (with system prompt preservation)
- 🎛️ Multiple AI models to choose from
- 📋 Built-in commands for managing the chat session
- ⚡ Command-line argument support for quick configuration overrides
- 🔄 Automatic model loading detection and retry logic
- 🌟 Access to 1000+ open-source AI models
- 🏹 **Friday's Personality**: Direct, honest, adventurous, and optimistic!

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
   - Edit the `.env` file and replace `your_huggingface_token_here` with your actual token
   - Example: `HUGGINGFACE_API_TOKEN=hf_your_actual_token_here`

### ✅ **Verify Your Setup:**
```bash
# Test if your token works
curl -X GET "https://huggingface.co/api/whoami" -H "Authorization: Bearer YOUR_TOKEN_HERE"
```
If successful, you'll see your username. If not, regenerate your token.

4. **Optional: Choose your AI model in `.env`:**
   - `HUGGINGFACE_MODEL`: The AI model to use (default: google/gemma-2-2b-it)
   - `MAX_TOKENS`: Maximum tokens in AI responses (default: 150)
   - `TEMPERATURE`: Creativity level 0.0-2.0 (default: 0.7)

5. **Optional: Customize Friday's personality:**
   - Edit `system_prompt.txt` to modify Friday's behavior and responses
   - The system prompt is automatically loaded when the chatbot starts
   - Changes take effect on next restart

## 🎭 Meet Friday - Your AI Personality

Friday comes with a unique personality defined in `system_prompt.txt`:

- 🏹 **Adventurous & Free-spirited** - Loves exploring new ideas and unconventional solutions
- 🎯 **Direct & Honest** - Tells it like it is, values truth over tact
- 🌟 **Optimistic & Encouraging** - Always sees potential and opportunities
- 🧠 **Big-picture thinker** - Connects concepts to broader philosophical ideas
- 🚀 **Independent** - Doesn't follow the crowd, thinks outside the box
- 📚 **Knowledge-seeking** - Explores the "why" behind questions, not just the "how"

**Friday's Motto:** *"Truth over tact, adventure over convention!"* 🌟

### Customizing Friday's Personality

Want to change how Friday behaves? Simply edit the `system_prompt.txt` file:

```bash
# Edit Friday's personality
nano system_prompt.txt
# or
code system_prompt.txt
```

You can make Friday:
- More formal or casual
- Specialized in certain topics
- Have different communication styles
- Reference different names or identities

## 🎯 Usage

**Basic usage:**
```bash
python chat.py
```

**With command-line overrides:**
```bash
python chat.py --model meta-llama/Llama-2-7b-chat-hf --temperature 0.9 --max-tokens 200
```

## 📋 Available Commands

Once the chatbot is running, you can use these commands:

- `help` - Show available commands
- `clear` - Clear conversation history
- `status` - Show current settings and conversation length
- `models` - Show alternative AI models you can try
- `quit` or `exit` - Exit the chatbot
- `Ctrl+C` - Force exit

## 🤖 Available AI Models

You can switch between different AI models by editing the `HUGGINGFACE_MODEL` in your `.env` file. Here are the **latest recommended models** (as of 2025):

### ⭐ **Recommended Models:**

- **google/gemma-2-2b-it** - Small, fast Gemma model (default, great for beginners)
- **deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B** - Compact reasoning model
- **meta-llama/Meta-Llama-3.1-8B-Instruct** - Powerful Llama 3.1 model
- **microsoft/phi-4** - Microsoft's latest Phi-4 model

### 🚀 **Advanced Models:**

- **deepseek-ai/DeepSeek-R1** - Full DeepSeek reasoning model (excellent for problem-solving)
- **Qwen/Qwen2.5-7B-Instruct-1M** - Supports very long conversations (1M context)
- **Qwen/Qwen2.5-Coder-32B-Instruct** - Specialized for programming and coding tasks
- **meta-llama/Llama-3.3-70B-Instruct** - Highest quality responses (largest model)

### 💡 **How to Switch Models:**

1. Edit your `.env` file
2. Uncomment the model you want to try
3. Comment out the current `HUGGINGFACE_MODEL` line
4. Restart the chatbot

**Example:**
```env
# HUGGINGFACE_MODEL=google/gemma-2-2b-it
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
📁 openai-api-test/
├── 🐍 chat.py              # Main chatbot application
├── 🎭 system_prompt.txt    # Friday's personality configuration
├── ⚙️ .env                 # API token and settings (create this)
├── 📋 requirements.txt     # Python dependencies
└── 📖 README.md           # This file
```

## 🔧 Dependencies

- `huggingface_hub` - Official Hugging Face library for Inference Providers
- `python-dotenv` - For environment variable management
- No billing or credit card required!

## 🚨 Troubleshooting

### 🔑 **API Token Issues:**

**"Invalid credentials" error:**
- ✅ Check your token starts with `hf_`
- ✅ Ensure no extra spaces in your `.env` file
- ✅ Regenerate token with "Inference Providers" permission
- ✅ Make sure you copied the full token

**"HUGGINGFACE_API_TOKEN not found" error:**
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

## 🔄 Switching Models

To try a different AI model:
1. Edit your `.env` file
2. Change `HUGGINGFACE_MODEL=new_model_name`
3. Restart the chatbot
4. Type `models` in the chat to see all available options

## 🤝 Contributing

Feel free to:
- Add support for more Hugging Face models
- Improve error handling
- Add new features
- Report issues

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**🎉 Enjoy your FREE AI chatbot powered by Hugging Face! 🎉**
