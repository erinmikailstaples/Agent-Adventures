"""
Configuration file for the LLM-Enhanced Weather Agent.

This file contains all the configuration settings for the agent.
In a real-world scenario, these would typically be loaded from
environment variables or a configuration file.
"""

# API Configuration
OLLAMA_BASE_URL = "http://localhost:11434"  # Ollama server URL
OLLAMA_MODEL = "llama3.2"  # Ollama model to use (llama3.2, mistral, codellama, etc.)
WEATHER_API_KEY = "your_openweathermap_api_key_here"  # Optional: for real weather data
DEFAULT_CITY = "London"  # Default city for weather queries

# Agent Configuration
AGENT_NAME = "LLM-Enhanced Weather Assistant"
AGENT_VERSION = "1.0.0"
AGENT_TYPE = "Level 0: LLM-Enhanced"

# LLM Settings
LLM_TEMPERATURE = 0.7  # Creativity level (0-1)
LLM_MAX_TOKENS = 300  # Maximum response length
LLM_TIMEOUT = 30  # seconds

# Ollama Settings
OLLAMA_TIMEOUT = 60  # seconds (Ollama can be slower)
OLLAMA_STREAM = False  # Set to True for streaming responses
OLLAMA_KEEP_ALIVE = "5m"  # Keep model in memory for 5 minutes

# Allowed Domains (what the agent can handle)
ALLOWED_DOMAINS = [
    "weather",
    "temperature",
    "rain",
    "sunny",
    "cloudy",
    "wind",
    "humidity",
    "forecast",
    "climate",
    "precipitation"
]

# Safety Constraints (what the agent should avoid)
SAFETY_CONSTRAINTS = [
    "medical advice",
    "financial advice",
    "legal advice",
    "personal information",
    "inappropriate content",
    "off-topic queries"
]

# Response Templates
RESPONSE_TEMPLATES = {
    "greeting": "Hello! I'm your weather assistant. How can I help you with weather information?",
    "boundary_error": "I can only help with weather-related questions. Please ask about weather conditions, temperatures, or weather forecasts.",
    "error": "I'm sorry, I couldn't process your request. Please try again with a weather-related question.",
    "help": "I can help you with weather information. Try asking about temperature, rain, wind, or weather forecasts for any location."
}

# Conversation Settings
MAX_CONVERSATION_HISTORY = 10  # Keep last 10 interactions
CONVERSATION_TIMEOUT = 3600  # 1 hour in seconds

# Weather Data Settings
WEATHER_CACHE_DURATION = 300  # 5 minutes in seconds
SUPPORTED_LOCATIONS = [
    "London", "Paris", "New York", "Tokyo", "Sydney", "Berlin", "Rome", "Madrid"
]

# LLM-Enhanced Agent Characteristics
# These demonstrate the capabilities of LLM-Enhanced agents
LLM_ENHANCED_CAPABILITIES = [
    "Contextual understanding of natural language",
    "Handles ambiguous inputs and variations",
    "Operates within strict boundaries",
    "High-volume processing of varied queries",
    "Natural language generation",
    "Intent recognition",
    "Context-aware responses"
]

# LLM-Enhanced Agent Limitations
# These demonstrate what LLM-Enhanced agents cannot do
LLM_ENHANCED_LIMITATIONS = [
    "Cannot make complex decisions",
    "Cannot access real-time data sources",
    "Cannot learn from past interactions",
    "Cannot integrate with external systems",
    "Cannot provide personalized recommendations",
    "Cannot handle multi-step reasoning",
    "Cannot access tools or APIs"
]

# When to Use LLM-Enhanced
SUITABLE_USE_CASES = [
    "Natural language understanding",
    "Contextual responses",
    "High-volume, varied queries",
    "Human-like interactions",
    "Ambiguous input handling",
    "Customer service chatbots",
    "Content categorization",
    "Basic data analysis",
    "FAQ responses"
]

# When NOT to Use LLM-Enhanced
UNSUITABLE_USE_CASES = [
    "Complex decision-making",
    "Tool integration",
    "Learning from experience",
    "High-stakes decisions",
    "Real-time system control",
    "Multi-step reasoning",
    "External system integration"
]

# Example Queries the Agent Can Handle
EXAMPLE_QUERIES = [
    "What's the weather like today?",
    "Is it going to rain this weekend?",
    "How hot is it in London?",
    "Should I bring an umbrella?",
    "What's the temperature in Paris?",
    "Will it be sunny tomorrow?",
    "How windy is it outside?",
    "What's the humidity like?",
    "Is it cloudy today?",
    "What's the weather forecast for this week?"
]

# Example Queries the Agent Cannot Handle
UNSUITABLE_QUERIES = [
    "What should I invest in?",
    "How do I fix my car?",
    "What's the best restaurant?",
    "How do I lose weight?",
    "What's the stock market doing?",
    "How do I cook pasta?",
    "What's the best movie?",
    "How do I learn programming?",
    "What's the news today?",
    "How do I fix my computer?"
]

# Performance Metrics
PERFORMANCE_METRICS = {
    "response_time_target": 2.0,  # seconds
    "accuracy_target": 0.85,  # 85% accuracy
    "user_satisfaction_target": 0.8,  # 80% satisfaction
    "throughput_target": 100  # queries per hour
}

# Error Handling
ERROR_HANDLING = {
    "max_retries": 3,
    "retry_delay": 1.0,  # seconds
    "fallback_response": "I'm sorry, I couldn't process your request. Please try again.",
    "timeout_response": "I'm sorry, the request timed out. Please try again."
}

# Logging Configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = "llm_weather_agent.log"

# Debug Settings
DEBUG_MODE = False
VERBOSE_LOGGING = False
SHOW_QUERY_ANALYSIS = True
SHOW_RESPONSE_GENERATION = True
