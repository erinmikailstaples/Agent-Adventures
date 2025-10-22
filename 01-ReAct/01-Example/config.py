"""
Configuration file for the ReAct Weather Planning Agent.

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
AGENT_NAME = "ReAct Weather Planning Agent"
AGENT_VERSION = "1.0.0"
AGENT_TYPE = "Level 1: ReAct"

# LLM Settings
LLM_TEMPERATURE = 0.7  # Creativity level (0-1)
LLM_MAX_TOKENS = 500  # Maximum response length
LLM_TIMEOUT = 30  # seconds

# Ollama Settings
OLLAMA_TIMEOUT = 60  # seconds (Ollama can be slower)
OLLAMA_STREAM = False  # Set to True for streaming responses
OLLAMA_KEEP_ALIVE = "5m"  # Keep model in memory for 5 minutes

# ReAct Agent Settings
MAX_PLANNING_ITERATIONS = 5  # Maximum planning iterations
PLANNING_CONFIDENCE_THRESHOLD = 0.7  # Minimum confidence for plan execution
ADAPTIVE_PLANNING_ENABLED = True  # Enable adaptive planning
STRATEGIC_THINKING_DEPTH = 3  # Depth of strategic thinking

# Weather Planning Parameters
WEATHER_PLANNING_HORIZON = 7  # Days to plan ahead
WEATHER_ACTIVITY_TYPES = [
    "outdoor_activities",
    "indoor_activities", 
    "travel_planning",
    "gardening",
    "exercise",
    "social_events",
    "work_schedule"
]

# Planning Strategies
PLANNING_STRATEGIES = [
    "conservative",  # Plan for worst weather
    "optimistic",    # Plan for best weather
    "adaptive",      # Adjust based on conditions
    "balanced"       # Consider multiple scenarios
]

# Activity Categories
ACTIVITY_CATEGORIES = {
    "outdoor_activities": {
        "sunny": ["hiking", "picnic", "beach", "gardening", "cycling"],
        "rainy": ["indoor_museum", "shopping", "cooking", "reading"],
        "cloudy": ["walking", "photography", "outdoor_dining"],
        "windy": ["kite_flying", "wind_sports", "indoor_activities"]
    },
    "indoor_activities": {
        "any": ["cooking", "reading", "movies", "games", "crafts", "exercise"]
    },
    "travel_planning": {
        "sunny": ["beach_destinations", "outdoor_tours", "hiking_trips"],
        "rainy": ["museums", "indoor_attractions", "cultural_sites"],
        "cloudy": ["city_tours", "indoor_outdoor_mix"],
        "windy": ["indoor_destinations", "protected_areas"]
    }
}

# ReAct Agent Characteristics
# These demonstrate the capabilities of ReAct agents
REACT_CAPABILITIES = [
    "Strategic thinking and planning",
    "Multi-step decision making",
    "Dynamic problem solving",
    "Task decomposition",
    "Adaptive planning",
    "Systematic approach",
    "Self-correcting behavior"
]

# ReAct Agent Limitations
# These demonstrate what ReAct agents cannot do
REACT_LIMITATIONS = [
    "Cannot access real-time external data",
    "Cannot learn from past interactions",
    "Cannot integrate with external systems",
    "Cannot perform physical actions",
    "Limited to reasoning and planning",
    "No memory of past experiences",
    "No tool integration capabilities"
]

# When to Use ReAct
SUITABLE_USE_CASES = [
    "Strategic weather planning",
    "Multi-step weather-related tasks",
    "Complex weather problem solving",
    "Adaptive weather planning",
    "Weather-based decision making",
    "Project management",
    "Research tasks",
    "Problem diagnosis",
    "Workflow optimization",
    "Strategic planning"
]

# When NOT to Use ReAct
UNSUITABLE_USE_CASES = [
    "Real-time weather monitoring",
    "Tool integration with weather services",
    "Learning from past weather patterns",
    "High-stakes weather decisions",
    "Environmental control systems",
    "Immediate weather responses",
    "Physical weather manipulation"
]

# Example Weather Planning Tasks
EXAMPLE_TASKS = [
    "Plan a weekend outdoor activity based on weather conditions",
    "Create a travel itinerary considering weather forecasts",
    "Optimize my daily schedule based on weather patterns",
    "Plan a garden project considering seasonal weather trends",
    "Create a weather-based exercise routine",
    "Plan a wedding considering weather contingencies",
    "Organize a company picnic with weather backup plans"
]

# Planning Templates
PLANNING_TEMPLATES = {
    "outdoor_activity": {
        "steps": [
            "Analyze weather conditions",
            "Identify suitable activities",
            "Plan activity timeline",
            "Prepare contingency plans",
            "Finalize activity plan"
        ]
    },
    "travel_planning": {
        "steps": [
            "Research destination weather",
            "Plan weather-appropriate activities",
            "Pack appropriate clothing",
            "Plan indoor alternatives",
            "Create flexible itinerary"
        ]
    },
    "daily_schedule": {
        "steps": [
            "Check weather forecast",
            "Optimize outdoor activities",
            "Schedule indoor alternatives",
            "Plan weather-dependent tasks",
            "Create flexible schedule"
        ]
    }
}

# Performance Metrics
PERFORMANCE_METRICS = {
    "planning_accuracy_target": 0.85,  # 85% accuracy
    "planning_efficiency_target": 0.8,  # 80% efficiency
    "user_satisfaction_target": 0.8,  # 80% satisfaction
    "planning_time_target": 30  # seconds per plan
}

# Error Handling
ERROR_HANDLING = {
    "max_planning_retries": 3,
    "planning_retry_delay": 2.0,  # seconds
    "fallback_planning": "Use conservative weather planning",
    "timeout_planning": "Use basic weather planning"
}

# Logging Configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = "react_weather_agent.log"

# Debug Settings
DEBUG_MODE = False
VERBOSE_LOGGING = False
SHOW_PLANNING_STEPS = True
SHOW_REASONING_PROCESS = True
