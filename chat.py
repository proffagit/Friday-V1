#!/usr/bin/env python3
"""
AI Chatbot with Web Search Integration
Uses LLM functions to determine when web search is needed and processes results
"""

import os
import sys
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import argparse
from LLMfunc import get_llm_instruction_response_bool, get_llm_instruction_response, get_llm_chat_response
from websearch import web_search

class HuggingFaceChatbot:
    def __init__(self):
        """Initialize the chatbot with web search capabilities"""
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
        self.instruction_model = os.getenv('HUGGINGFACE_INSTRUCTION_MODEL', 'Qwen/Qwen2.5-7B-Instruct-1M')
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
        
        print("🤗 AI Chatbot with Web Search initialized!")
        print(f"📡 Using model: {self.model}")
        print(f"🔍 Instruction model: {self.instruction_model}")
        print(f"🎛️  Temperature: {self.temperature}")
        print(f"📝 Max tokens: {self.max_tokens}")
        print("🌐 Web search enabled with intelligent detection")
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

    def check_if_web_search_needed(self, user_query: str) -> bool:
        """
        Use LLM to determine if the user query requires web search
        """
        try:
            query_condition = """
            Does this user query require current, real-time, or recent information that would need a web search to answer accurately? 
            Consider queries about:
            - Current events, news, or recent developments
            - Current prices, stock market, or financial data
            - Weather information
            - Recent research or studies
            - Current sports scores or results
            - Today's date-specific information
            - Real-time data or statistics
            - Recent product releases or updates
            
            Answer 'true' if web search is needed, 'false' if the query can be answered with general knowledge.
            """
            
            result = get_llm_instruction_response_bool(
                query_condition=query_condition,
                content=user_query,
                model=self.instruction_model,
                max_tokens=50
            )
            
            return result
            
        except Exception as e:
            print(f"⚠️ Error checking web search requirement: {str(e)}")
            return False

    def clarify_search_request(self, user_query: str) -> str:
        """
        Use LLM to clarify and optimize the search query
        """
        try:
            clarification_instruction = """
            Based on the user's query, create an optimized search query for web search engines. 
            Make it concise, specific, and likely to return relevant results. 
            Focus on the key information needed to answer the user's question.
            Return only the search query without explanations.
            """
            
            clarified_query = get_llm_instruction_response(
                query_instruction=clarification_instruction,
                content=user_query,
                model=self.instruction_model,
                max_tokens=100
            )
            
            return clarified_query.strip().strip('"').strip("'")
            
        except Exception as e:
            print(f"⚠️ Error clarifying search request: {str(e)}")
            return user_query

    def summarize_search_results(self, search_results: list, original_query: str) -> str:
        """
        Use LLM to summarize search results into a 200-word context
        """
        try:
            # Combine all search results into a single text
            combined_content = ""
            for i, result in enumerate(search_results, 1):
                combined_content += f"Source {i} ({result['title']}):\n{result['content']}\n\n"
            
            # Limit content to avoid token limits
            if len(combined_content) > 8000:
                combined_content = combined_content[:8000] + "..."
            
            summarization_instruction = f"""
            Based on the following web search results, provide a comprehensive summary in exactly 200 words that directly answers this question: "{original_query}"
            
            Focus on:
            1. Direct answers to the user's question
            2. Key facts and current information
            3. Important details and context
            4. Sources when relevant
            
            Make the summary informative, accurate, and well-structured. Use exactly 200 words.
            """
            
            summary = get_llm_instruction_response(
                query_instruction=summarization_instruction,
                content=combined_content,
                model=self.instruction_model,
                max_tokens=200
            )
            
            return summary
            
        except Exception as e:
            print(f"⚠️ Error summarizing search results: {str(e)}")
            return "Error occurred while summarizing search results."

    def get_ai_response_with_search(self, user_input: str):
        """Get AI response with optional web search integration"""
        try:
            # Check if web search is needed
            print("🔍 Analyzing if web search is needed...")
            needs_search = self.check_if_web_search_needed(user_input)
            
            search_context = ""
            if needs_search:
                print("🌐 Web search required - performing search...")
                
                # Clarify the search query
                search_query = self.clarify_search_request(user_input)
                print(f"🔎 Optimized search query: {search_query}")
                
                # Perform web search
                search_results = web_search(search_query, num_results=3)
                
                if search_results:
                    print(f"📊 Found {len(search_results)} results, summarizing...")
                    
                    # Summarize search results
                    search_summary = self.summarize_search_results(search_results, user_input)
                    
                    # Add search context to conversation
                    search_context = f"\n\n[WEB SEARCH CONTEXT]\n{search_summary}\n[END CONTEXT]\n"
                    print("✅ Search completed and summarized")
                else:
                    print("⚠️ No search results found")
                    search_context = "\n\n[WEB SEARCH CONTEXT]\nNo current information found for this query.\n[END CONTEXT]\n"
            else:
                print("💭 Using general knowledge (no web search needed)")
            
            # Add user message with search context to conversation history
            user_message_with_context = user_input + search_context
            self.conversation_history.append({"role": "user", "content": user_message_with_context})
            
            # Keep conversation history manageable (last 10 exchanges)
            if len(self.conversation_history) > 21:  # 1 system + 20 messages
                # Keep system message and last 18 user/assistant messages
                system_msg = self.conversation_history[0] if self.conversation_history[0]["role"] == "system" else None
                recent_messages = self.conversation_history[-18:]
                self.conversation_history = ([system_msg] if system_msg else []) + recent_messages
            
            # Get AI response using the chat function
            ai_response = get_llm_chat_response(
                messages=self.conversation_history,
                model=self.model,
                max_tokens=self.max_tokens
            )
            
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
        print("  search  - Toggle web search mode")
        print("  quit    - Exit the chatbot")
        print("  exit    - Exit the chatbot")
        print("  Ctrl+C  - Force exit")
        print()
        print("🌐 Web search is automatically enabled when needed")
        print("💡 Ask about current events, prices, weather, or recent information")
        print()

    def show_status(self):
        """Show current chatbot status and settings"""
        print(f"\n📊 Current Status:")
        print(f"  Chat Model: {self.model}")
        print(f"  Instruction Model: {self.instruction_model}")
        print(f"  Temperature: {self.temperature}")
        print(f"  Max tokens: {self.max_tokens}")
        print(f"  System prompt: {'✅ Loaded' if self.system_prompt else '❌ Not loaded'}")
        print(f"  Conversation length: {len(self.conversation_history)} messages")
        print(f"  Using: Hugging Face Inference Providers")
        print(f"  Web Search: ✅ Enabled with intelligent detection")
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
        print("For HUGGINGFACE_INSTRUCTION_MODEL (used for search logic):")
        print("  Qwen/Qwen2.5-7B-Instruct-1M            - Default for instructions")
        print("  meta-llama/Meta-Llama-3.1-8B-Instruct  - Alternative for instructions")
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
                
                # Get AI response with web search integration
                print("\n🤖 AI: ", end="", flush=True)
                response = self.get_ai_response_with_search(user_input)
                print(response)
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
        except Exception as e:
            print(f"\n❌ Unexpected error: {str(e)}")

def main():
    """Main function with command line argument support"""
    parser = argparse.ArgumentParser(description='AI Chatbot with Web Search Integration')
    parser.add_argument('--version', action='version', version='AI Chatbot v1.0')
    parser.add_argument('--model', help='Override the Hugging Face chat model')
    parser.add_argument('--instruction-model', help='Override the Hugging Face instruction model')
    parser.add_argument('--temperature', type=float, help='Override the temperature setting')
    parser.add_argument('--max-tokens', type=int, help='Override the max tokens setting')
    
    args = parser.parse_args()
    
    # Create and run chatbot
    chatbot = HuggingFaceChatbot()
    
    # Override settings if provided via command line
    if args.model:
        chatbot.model = args.model
        print(f"🔧 Chat model overridden to: {args.model}")
    if args.instruction_model:
        chatbot.instruction_model = args.instruction_model
        print(f"🔧 Instruction model overridden to: {args.instruction_model}")
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
