#!/usr/bin/env python3
"""
LLM-Enhanced Agent Example: Natural Language Weather Assistant

This is a Level 0 LLM-Enhanced agent that demonstrates:
- Contextual understanding of natural language
- Handling ambiguous inputs and variations
- Operating within strict boundaries
- High-volume processing of varied queries
- Natural language generation

The agent can understand natural language weather queries and provide
contextual responses while maintaining safety boundaries.
"""

import requests
import json
import datetime
import re
from typing import Dict, List, Optional, Tuple
from config import (
    OLLAMA_BASE_URL,
    OLLAMA_MODEL, 
    WEATHER_API_KEY, 
    DEFAULT_CITY,
    ALLOWED_DOMAINS,
    SAFETY_CONSTRAINTS,
    RESPONSE_TEMPLATES,
    OLLAMA_TIMEOUT,
    OLLAMA_STREAM,
    OLLAMA_KEEP_ALIVE
)


class LLMWeatherAgent:
    """
    An LLM-enhanced agent that can understand natural language weather queries.
    
    This agent demonstrates Level 0 characteristics:
    - Contextual understanding of natural language
    - Handles ambiguous inputs and variations
    - Operates within strict boundaries
    - High-volume processing of varied queries
    - Natural language generation
    """
    
    def __init__(self):
        self.ollama_base_url = OLLAMA_BASE_URL
        self.model = OLLAMA_MODEL
        self.weather_api_key = WEATHER_API_KEY
        self.default_city = DEFAULT_CITY
        self.allowed_domains = ALLOWED_DOMAINS
        self.safety_constraints = SAFETY_CONSTRAINTS
        
        # Initialize conversation history for context
        self.conversation_history = []
        
        # Weather data cache (simple in-memory cache)
        self.weather_cache = {}
    
    def process_natural_language_query(self, user_query: str) -> str:
        """
        Process a natural language weather query using LLM.
        
        This method demonstrates LLM-Enhanced capabilities:
        - Understands context and intent
        - Handles variations in phrasing
        - Operates within strict boundaries
        - Generates contextual responses
        """
        print(f"Processing query: '{user_query}'")
        
        # Step 1: Analyze query with LLM
        query_analysis = self._analyze_query_with_llm(user_query)
        
        # Step 2: Check if query is within allowed domains
        if not self._is_query_allowed(query_analysis):
            return self._generate_boundary_error_response(user_query)
        
        # Step 3: Extract weather information needs
        weather_needs = self._extract_weather_needs(query_analysis)
        
        # Step 4: Generate contextual response
        response = self._generate_contextual_response(user_query, weather_needs)
        
        # Step 5: Apply safety filters
        filtered_response = self._apply_safety_filters(response)
        
        # Step 6: Update conversation history
        self._update_conversation_history(user_query, filtered_response)
        
        return filtered_response
    
    def _analyze_query_with_llm(self, user_query: str) -> Dict:
        """
        Use LLM to analyze the user query and extract intent.
        
        This demonstrates LLM-Enhanced capabilities:
        - Natural language understanding
        - Intent extraction
        - Context analysis
        """
        prompt = f"""
        Analyze this weather-related query and extract the following information:
        
        Query: "{user_query}"
        
        Please provide a JSON response with:
        - intent: What the user wants to know about weather
        - location: Any specific location mentioned (if any)
        - time_frame: When they want weather info (today, tomorrow, weekend, etc.)
        - weather_type: What type of weather info (temperature, rain, wind, etc.)
        - confidence: How confident you are in the analysis (0-1)
        
        Respond only with valid JSON.
        """
        
        try:
            # Use Ollama API instead of OpenAI
            response = self._call_ollama_api(prompt, system_prompt="You are a weather query analyzer. Respond only with valid JSON.")
            
            analysis = json.loads(response)
            print(f"Query analysis: {analysis}")
            return analysis
            
        except Exception as e:
            print(f"Error analyzing query: {e}")
            return {
                "intent": "unknown",
                "location": None,
                "time_frame": "current",
                "weather_type": "general",
                "confidence": 0.0
            }
    
    def _is_query_allowed(self, query_analysis: Dict) -> bool:
        """
        Check if the query is within allowed domains and safety constraints.
        
        This demonstrates LLM-Enhanced boundary enforcement:
        - Domain restrictions
        - Safety constraints
        - Content filtering
        """
        # Check if query is weather-related
        if query_analysis.get("intent") == "unknown":
            return False
        
        # Check confidence level
        if query_analysis.get("confidence", 0) < 0.3:
            return False
        
        # Check for safety constraints
        for constraint in self.safety_constraints:
            if constraint.lower() in query_analysis.get("intent", "").lower():
                return False
        
        return True
    
    def _extract_weather_needs(self, query_analysis: Dict) -> Dict:
        """
        Extract what weather information is needed based on the analysis.
        
        This demonstrates LLM-Enhanced information extraction:
        - Intent-based information needs
        - Context-aware data requirements
        - User preference understanding
        """
        needs = {
            "location": query_analysis.get("location") or self.default_city,
            "time_frame": query_analysis.get("time_frame", "current"),
            "weather_type": query_analysis.get("weather_type", "general"),
            "intent": query_analysis.get("intent", "general_weather")
        }
        
        return needs
    
    def _call_ollama_api(self, prompt: str, system_prompt: str = None) -> str:
        """
        Call the Ollama API to get LLM responses.
        
        This method demonstrates LLM-Enhanced capabilities:
        - Local LLM processing
        - Cost-effective AI inference
        - Privacy-preserving AI
        """
        try:
            # Prepare the request payload
            payload = {
                "model": self.model,
                "prompt": prompt,
                "stream": OLLAMA_STREAM,
                "options": {
                    "temperature": 0.7,
                    "top_p": 0.9,
                    "num_predict": 300
                }
            }
            
            # Add system prompt if provided
            if system_prompt:
                payload["system"] = system_prompt
            
            # Make the API call
            response = requests.post(
                f"{self.ollama_base_url}/api/generate",
                json=payload,
                timeout=OLLAMA_TIMEOUT
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get("response", "")
            else:
                raise Exception(f"Ollama API error: {response.status_code} - {response.text}")
                
        except requests.exceptions.ConnectionError:
            raise Exception("Cannot connect to Ollama. Make sure Ollama is running on localhost:11434")
        except requests.exceptions.Timeout:
            raise Exception("Ollama request timed out. The model might be too slow or not loaded.")
        except Exception as e:
            raise Exception(f"Error calling Ollama API: {e}")
    
    def _generate_contextual_response(self, user_query: str, weather_needs: Dict) -> str:
        """
        Generate a contextual response based on the weather needs.
        
        This demonstrates LLM-Enhanced response generation:
        - Contextual understanding
        - Natural language generation
        - User intent fulfillment
        """
        # Create a prompt for generating the response
        prompt = f"""
        You are a helpful weather assistant. The user asked: "{user_query}"
        
        Based on their query, they want:
        - Location: {weather_needs['location']}
        - Time frame: {weather_needs['time_frame']}
        - Weather type: {weather_needs['weather_type']}
        - Intent: {weather_needs['intent']}
        
        Generate a helpful, contextual response that:
        1. Acknowledges their specific question
        2. Provides relevant weather information
        3. Uses natural, conversational language
        4. Stays within weather-related topics only
        
        Keep the response concise and helpful.
        """
        
        try:
            # Use Ollama API instead of OpenAI
            response = self._call_ollama_api(
                prompt, 
                system_prompt="You are a helpful weather assistant. Provide accurate, helpful weather information in a conversational tone."
            )
            
            return response.strip()
            
        except Exception as e:
            print(f"Error generating response: {e}")
            return "I'm sorry, I couldn't generate a response. Please try again."
    
    def _apply_safety_filters(self, response: str) -> str:
        """
        Apply safety filters to ensure the response is appropriate.
        
        This demonstrates LLM-Enhanced safety measures:
        - Content filtering
        - Boundary enforcement
        - Safety constraints
        """
        # Check for inappropriate content
        for constraint in self.safety_constraints:
            if constraint.lower() in response.lower():
                return "I can only provide weather-related information. Please ask about weather conditions."
        
        # Check response length
        if len(response) > 500:
            response = response[:500] + "..."
        
        return response
    
    def _generate_boundary_error_response(self, user_query: str) -> str:
        """
        Generate a response when the query is outside allowed boundaries.
        
        This demonstrates LLM-Enhanced boundary enforcement:
        - Graceful boundary handling
        - Helpful error messages
        - User guidance
        """
        return f"I can only help with weather-related questions. Your query '{user_query}' seems to be outside my area of expertise. Please ask about weather conditions, temperatures, or weather forecasts."
    
    def _update_conversation_history(self, user_query: str, response: str):
        """
        Update the conversation history for context.
        
        This demonstrates LLM-Enhanced context awareness:
        - Conversation memory
        - Context tracking
        - User interaction history
        """
        self.conversation_history.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "user_query": user_query,
            "agent_response": response
        })
        
        # Keep only last 10 interactions
        if len(self.conversation_history) > 10:
            self.conversation_history = self.conversation_history[-10:]
    
    def get_conversation_history(self) -> List[Dict]:
        """
        Get the conversation history.
        
        This demonstrates LLM-Enhanced context awareness:
        - Conversation tracking
        - User interaction history
        - Context management
        """
        return self.conversation_history
    
    def clear_conversation_history(self):
        """
        Clear the conversation history.
        
        This demonstrates LLM-Enhanced memory management:
        - Context reset
        - Memory clearing
        - Fresh start capability
        """
        self.conversation_history = []
        print("Conversation history cleared.")
    
    def run_interactive_session(self):
        """
        Run an interactive session with the user.
        
        This demonstrates LLM-Enhanced capabilities in action:
        - Natural language interaction
        - Contextual responses
        - Boundary enforcement
        - User guidance
        """
        print("=" * 60)
        print("LLM-Enhanced Weather Assistant")
        print("=" * 60)
        print()
        print("This agent demonstrates Level 0: LLM-Enhanced capabilities:")
        print("✅ Contextual understanding of natural language")
        print("✅ Handles ambiguous inputs and variations")
        print("✅ Operates within strict boundaries")
        print("✅ High-volume processing of varied queries")
        print("✅ Natural language generation")
        print()
        print("Ask me about weather! (Type 'quit' to exit)")
        print()
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("Goodbye! Thanks for using the LLM-Enhanced Weather Assistant.")
                    break
                
                if not user_input:
                    continue
                
                # Process the query
                response = self.process_natural_language_query(user_input)
                print(f"Assistant: {response}")
                print()
                
            except KeyboardInterrupt:
                print("\nGoodbye! Thanks for using the LLM-Enhanced Weather Assistant.")
                break
            except Exception as e:
                print(f"Error: {e}")
                print("Please try again.")
                print()


def main():
    """
    Main function to run the LLM-Enhanced Weather Agent.
    
    This demonstrates the capabilities and limitations of Level 0 agents:
    - Natural language understanding
    - Contextual responses
    - Boundary enforcement
    - High-volume processing
    """
    print("LLM-Enhanced Weather Agent Example")
    print("This demonstrates Level 0: LLM-Enhanced capabilities")
    print()
    
    # Check if Ollama is running
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        if response.status_code != 200:
            raise Exception("Ollama not responding")
    except Exception as e:
        print("⚠️  WARNING: Ollama is not running!")
        print("   Please start Ollama and ensure it's running on localhost:11434")
        print("   Install Ollama from: https://ollama.ai/")
        print("   Then run: ollama pull llama3.2")
        print()
        return False
    
    # Create and run the agent
    agent = LLMWeatherAgent()
    
    print("Starting LLM-Enhanced Weather Agent...")
    print("This agent can understand natural language weather queries!")
    print()
    
    # Run interactive session
    agent.run_interactive_session()
    
    return True


if __name__ == "__main__":
    main()
