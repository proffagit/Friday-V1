import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables
load_dotenv()

def get_llm_instruction_response(query_instruction: str, content: str, model: str = None, max_tokens: int = None) -> str:
    """
    Get LLM instruction response using Hugging Face Inference API
    
    Args:
        query_instruction (str): The instruction or prompt for the LLM
        content (str): The content to be processed by the LLM
        model (str, optional): Model to use. If None, uses HUGGINGFACE_INSTRUCTION_MODEL from .env
        max_tokens (int, optional): Maximum tokens to generate. If None, uses MAX_TOKENS from .env
    
    Returns:
        str: The LLM response
    
    Raises:
        ValueError: If API token is not configured
        Exception: If API call fails
    """
    
    # Get configuration from environment variables
    api_token = os.getenv('HUGGINGFACE_API_TOKEN')
    if not api_token:
        raise ValueError("HUGGINGFACE_API_TOKEN not found in environment variables")
    
    # Use provided model or fallback to instruction model environment variable
    model_name = model or os.getenv('HUGGINGFACE_INSTRUCTION_MODEL', 'Qwen/Qwen2.5-7B-Instruct-1M')
    max_tokens = max_tokens or int(os.getenv('MAX_TOKENS', 150))
    temperature = float(os.getenv('TEMPERATURE', 0.5))
    
    # Initialize the Inference Client
    client = InferenceClient(api_key=api_token)
    
    try:
        # Combine instruction and content into a single prompt
        full_prompt = f"{query_instruction}\n\nContent: {content}"
        
        # Create messages format for chat completions
        messages = [{"role": "user", "content": full_prompt}]
        
        # Make the API call using chat completions
        completion = client.chat.completions.create(
            model=model_name,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            stream=False
        )
        
        return completion.choices[0].message.content.strip()
        
    except Exception as e:
        raise Exception(f"Failed to get LLM response: {str(e)}")


def get_llm_instruction_response_bool(query_condition: str, content: str, model: str = None, max_tokens: int = None) -> bool:
    """
    Get LLM instruction response and return a boolean based on the query condition
    
    Args:
        query_condition (str): The condition or question for the LLM to evaluate (should be answerable with yes/no or true/false)
        content (str): The content to be evaluated by the LLM
        model (str, optional): Model to use. If None, uses HUGGINGFACE_INSTRUCTION_MODEL from .env
        max_tokens (int, optional): Maximum tokens to generate. If None, uses MAX_TOKENS from .env
    
    Returns:
        bool: True if the condition is met, False otherwise
    
    Raises:
        ValueError: If API token is not configured
        Exception: If API call fails
    """
    
    # Get configuration from environment variables
    api_token = os.getenv('HUGGINGFACE_API_TOKEN')
    if not api_token:
        raise ValueError("HUGGINGFACE_API_TOKEN not found in environment variables")
    
    # Use provided model or fallback to instruction model environment variable
    model_name = model or os.getenv('HUGGINGFACE_INSTRUCTION_MODEL', 'Qwen/Qwen2.5-7B-Instruct-1M')
    max_tokens = max_tokens or int(os.getenv('MAX_TOKENS', 150))
    temperature = float(os.getenv('TEMPERATURE', 0.5))
    
    # Initialize the Inference Client
    client = InferenceClient(api_key=api_token)
    
    try:
        # Create a prompt that asks for a boolean response
        full_prompt = f"{query_condition}\n\nContent: {content}\n\nPlease respond with only 'true' or 'false'."
        
        # Create messages format for chat completions
        messages = [{"role": "user", "content": full_prompt}]
        
        # Make the API call using chat completions
        completion = client.chat.completions.create(
            model=model_name,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            stream=False
        )
        
        # Get the response and convert to boolean
        response = completion.choices[0].message.content.strip().lower()
        
        # Parse the response to boolean
        if response in ['true', 'yes', '1', 'correct', 'positive']:
            return True
        elif response in ['false', 'no', '0', 'incorrect', 'negative']:
            return False
        else:
            # If response is ambiguous, try to determine based on common patterns
            if any(word in response for word in ['yes', 'true', 'correct', 'positive', 'valid']):
                return True
            else:
                return False
        
    except Exception as e:
        raise Exception(f"Failed to get LLM boolean response: {str(e)}")


def get_llm_chat_response(messages: list, model: str = None, max_tokens: int = None) -> str:
    """
    Get LLM response using chat completions format
    
    Args:
        messages (list): List of message dictionaries with 'role' and 'content'
        model (str, optional): Model to use. If None, uses HUGGINGFACE_MODEL from .env
        max_tokens (int, optional): Maximum tokens to generate. If None, uses MAX_TOKENS from .env
    
    Returns:
        str: The LLM response
    
    Raises:
        ValueError: If API token is not configured
        Exception: If API call fails
    """
    
    # Get configuration from environment variables
    api_token = os.getenv('HUGGINGFACE_API_TOKEN')
    if not api_token:
        raise ValueError("HUGGINGFACE_API_TOKEN not found in environment variables")
    
    # Use provided model or fallback to environment variable
    model_name = model or os.getenv('HUGGINGFACE_MODEL', 'google/gemma-2-2b-it')
    max_tokens = max_tokens or int(os.getenv('MAX_TOKENS', 150))
    temperature = float(os.getenv('TEMPERATURE', 0.5))
    
    # Initialize the Inference Client
    client = InferenceClient(api_key=api_token)
    
    try:
        # Make the chat completions API call
        completion = client.chat.completions.create(
            model=model_name,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            stream=False
        )
        
        return completion.choices[0].message.content.strip()
        
    except Exception as e:
        raise Exception(f"Failed to get LLM chat response: {str(e)}")
