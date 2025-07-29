#!/usr/bin/env python3
"""
Terminal-based AI Chatbot using Hugging Face Inference Providers
"""

import os
import sys
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import argparse

class HuggingFaceChatbot:
    def __init__(self):
        """Initialize the chatbot with Hugging Face Inference Providers from .env file"""
        # Load environment variables from .env file
        load_dotenv()
        
        # Get API token from environment
        self.api_token = os.getenv('HUGGINGFACE_API_TOKEN')
        if not self.api_token or self.api_token == 'your_real_huggingface_token_here':
            print("❌ Error: HUGGINGFACE_API_TOKEN not found or not set in .env file")
            print("Please add your Hugging Face API token to the .env file:")
            print("HUGGINGFACE_API_TOKEN=hf_your_actual_token_here")
            print("Get your token at: https://huggingface.co/settings/tokens")
            sys.exit(1)
        
        # Get configuration from environment variables with defaults
        self.model = os.getenv('HUGGINGFACE_MODEL', 'google/gemma-2-2b-it')
        self.max_tokens = int(os.getenv('MAX_TOKENS', '150'))
        self.temperature = float(os.getenv('TEMPERATURE', '0.7'))
        
        # Initialize Hugging Face Inference Client
        try:
            self.client = InferenceClient(api_key=self.api_token)
            print("✅ Successfully connected to Hugging Face Inference Providers!")
        except Exception as e:
            print(f"❌ Failed to initialize Hugging Face client: {str(e)}")
            sys.exit(1)
        
        # Load system prompt from file
        self.system_prompt = self.load_system_prompt()
        
        # Conversation history for chat context (starts with system prompt)
        self.conversation_history = []
        if self.system_prompt:
            self.conversation_history.append({"role": "system", "content": self.system_prompt})
        
        print("🤗 Hugging Face AI Chatbot initialized!")
        print(f"📡 Using model: {self.model}")
        print(f"🎛️  Temperature: {self.temperature}")
        print(f"📝 Max tokens: {self.max_tokens}")
        print("💬 Type 'quit', 'exit', or press Ctrl+C to exit")
        print("🔄 Type 'clear' to clear conversation history")
        print("ℹ️  Type 'help' for more commands")
        print("🆓 This is completely FREE - no API costs!")
        print("-" * 50)

    def load_system_prompt(self):
        """Load system prompt from file"""
        try:
            system_prompt_file = os.path.join(os.path.dirname(__file__), 'system_prompt.txt')
            if os.path.exists(system_prompt_file):
                with open(system_prompt_file, 'r', encoding='utf-8') as f:
                    prompt = f.read().strip()
                    print(f"📜 Loaded system prompt from: system_prompt.txt")
                    return prompt
            else:
                print("⚠️ No system_prompt.txt file found, using default behavior")
                return None
        except Exception as e:
            print(f"⚠️ Error loading system prompt: {str(e)}")
            return None

    def get_ai_response(self, user_input):
        """Get response from Hugging Face Inference Providers"""
        try:
            # Add user message to conversation history
            self.conversation_history.append({"role": "user", "content": user_input})
            
            # Keep conversation history manageable (last 10 exchanges)
            if len(self.conversation_history) > 21:  # 1 system + 20 messages
                # Keep system message and last 18 user/assistant messages
                system_msg = self.conversation_history[0] if self.conversation_history[0]["role"] == "system" else None
                recent_messages = self.conversation_history[-18:]
                self.conversation_history = ([system_msg] if system_msg else []) + recent_messages
            
            # Make API call using the new chat completion interface
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                stream=False
            )
            
            # Extract the response
            ai_response = completion.choices[0].message.content.strip()
            
            # Add AI response to conversation history
            self.conversation_history.append({"role": "assistant", "content": ai_response})
            
            return ai_response
            
        except Exception as e:
            error_msg = str(e)
            if "Model" in error_msg and "not found" in error_msg:
                return f"❌ Model '{self.model}' not available. Try: google/gemma-2-2b-it, meta-llama/Meta-Llama-3.1-8B-Instruct, or microsoft/phi-4"
            elif "token" in error_msg.lower() or "unauthorized" in error_msg.lower():
                return "❌ Invalid token. Please check your HUGGINGFACE_API_TOKEN in .env file"
            elif "quota" in error_msg.lower() or "rate" in error_msg.lower():
                return "⚠️ Rate limit reached. Please wait a moment before trying again."
            else:
                return f"❌ Error: {error_msg}"

    def clear_history(self):
        """Clear conversation history but keep system prompt"""
        if self.system_prompt:
            self.conversation_history = [{"role": "system", "content": self.system_prompt}]
        else:
            self.conversation_history = []
        print("🧹 Conversation history cleared!")

    def show_help(self):
        """Show available commands"""
        print("\n📋 Available commands:")
        print("  help    - Show this help message")
        print("  clear   - Clear conversation history")
        print("  status  - Show current settings")
        print("  models  - Show recommended models you can try")
        print("  quit    - Exit the chatbot")
        print("  exit    - Exit the chatbot")
        print("  Ctrl+C  - Force exit")
        print()

    def show_status(self):
        """Show current chatbot status and settings"""
        print(f"\n📊 Current Status:")
        print(f"  Model: {self.model}")
        print(f"  Temperature: {self.temperature}")
        print(f"  Max tokens: {self.max_tokens}")
        print(f"  System prompt: {'✅ Loaded' if self.system_prompt else '❌ Not loaded'}")
        print(f"  Conversation length: {len(self.conversation_history)} messages")
        print(f"  Using: Hugging Face Inference Providers")
        print()

    def show_models(self):
        """Show recommended models that can be used"""
        print("\n🤖 Recommended Hugging Face models you can try:")
        print("Edit your .env file and change HUGGINGFACE_MODEL to:")
        print("  google/gemma-2-2b-it                    - Small, fast Gemma model (recommended)")
        print("  meta-llama/Meta-Llama-3.1-8B-Instruct  - Powerful Llama 3.1 model")
        print("  microsoft/phi-4                        - Microsoft's Phi-4 model")
        print("  deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B - DeepSeek reasoning model")
        print("  Qwen/Qwen2.5-7B-Instruct-1M            - Qwen model with long context")
        print("  Qwen/Qwen2.5-Coder-32B-Instruct        - Specialized for coding")
        print()
        print("💡 These models are available through Hugging Face Inference Providers")
        print()

    def run(self):
        """Main chat loop"""
        try:
            while True:
                # Get user input
                user_input = input("\n👤 You: ").strip()
                
                # Handle empty input
                if not user_input:
                    continue
                
                # Handle commands
                if user_input.lower() in ['quit', 'exit']:
                    print("👋 Goodbye!")
                    break
                elif user_input.lower() == 'clear':
                    self.clear_history()
                    continue
                elif user_input.lower() == 'help':
                    self.show_help()
                    continue
                elif user_input.lower() == 'status':
                    self.show_status()
                    continue
                elif user_input.lower() == 'models':
                    self.show_models()
                    continue
                
                # Get AI response
                print("\n🤖 AI: ", end="", flush=True)
                response = self.get_ai_response(user_input)
                print(response)
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
        except Exception as e:
            print(f"\n❌ Unexpected error: {str(e)}")

def main():
    """Main function with command line argument support"""
    parser = argparse.ArgumentParser(description='Terminal-based AI Chatbot using Hugging Face Inference Providers')
    parser.add_argument('--version', action='version', version='Hugging Face AI Chatbot v2.0')
    parser.add_argument('--model', help='Override the Hugging Face model')
    parser.add_argument('--temperature', type=float, help='Override the temperature setting')
    parser.add_argument('--max-tokens', type=int, help='Override the max tokens setting')
    
    args = parser.parse_args()
    
    # Create and run chatbot
    chatbot = HuggingFaceChatbot()
    
    # Override settings if provided via command line
    if args.model:
        chatbot.model = args.model
        print(f"🔧 Model overridden to: {args.model}")
    if args.temperature is not None:
        chatbot.temperature = args.temperature
        print(f"🔧 Temperature overridden to: {args.temperature}")
    if args.max_tokens:
        chatbot.max_tokens = args.max_tokens
        print(f"🔧 Max tokens overridden to: {args.max_tokens}")
    
    # Start the chat
    chatbot.run()

if __name__ == "__main__":
    main()
