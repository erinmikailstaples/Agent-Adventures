#!/usr/bin/env python3
"""
Fixed Automation Agent Example: Weather Reporter

This is a Level -1 Fixed Automation agent that demonstrates:
- Rigid, pre-programmed behavior
- No decision-making capabilities
- No adaptation to unexpected inputs
- High efficiency for repetitive tasks
- Predictable, scripted behavior

The agent fetches weather data and generates a simple report.
"""

import requests
import json
import datetime
import os
from config import (
    OLLAMA_BASE_URL, 
    OLLAMA_MODEL, 
    WEATHER_API_KEY, 
    CITY, 
    OUTPUT_DIR,
    OLLAMA_TIMEOUT,
    OLLAMA_STREAM,
    OLLAMA_KEEP_ALIVE
)


class WeatherReporterAgent:
    """
    A fixed automation agent that fetches weather data and generates reports.
    
    This agent demonstrates Level -1 characteristics:
    - Follows exact, predetermined steps
    - Cannot adapt to unexpected inputs
    - Fails when encountering unplanned scenarios
    - High efficiency for repetitive tasks
    """
    
    def __init__(self):
        self.ollama_base_url = OLLAMA_BASE_URL
        self.model = OLLAMA_MODEL
        self.api_key = WEATHER_API_KEY
        self.city = CITY
        self.output_dir = OUTPUT_DIR
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        
        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)
    
    def fetch_weather_data(self):
        """
        Fetch weather data from OpenWeatherMap API.
        
        This method demonstrates fixed automation:
        - Makes a single API call
        - No retry logic or error handling
        - Fails if API is unavailable
        - No adaptation to different response formats
        """
        print(f"Fetching weather data for {self.city}...")
        
        # Fixed parameters - no adaptation possible
        params = {
            'q': self.city,
            'appid': self.api_key,
            'units': 'metric'  # Fixed to metric units
        }
        
        # Single API call - no retry mechanism
        response = requests.get(self.base_url, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            # Fixed error handling - just raise exception
            raise Exception(f"API request failed with status {response.status_code}")
    
    def parse_weather_data(self, weather_data):
        """
        Parse weather data into a fixed format.
        
        This method demonstrates fixed automation:
        - Assumes specific data structure
        - No validation of data quality
        - Fails if data structure changes
        - No adaptation to different data formats
        """
        print("Parsing weather data...")
        
        # Fixed parsing - assumes specific JSON structure
        # Will fail if API response format changes
        parsed_data = {
            'city': weather_data['name'],
            'country': weather_data['sys']['country'],
            'temperature': weather_data['main']['temp'],
            'feels_like': weather_data['main']['feels_like'],
            'humidity': weather_data['main']['humidity'],
            'pressure': weather_data['main']['pressure'],
            'description': weather_data['weather'][0]['description'],
            'wind_speed': weather_data['wind']['speed'],
            'timestamp': datetime.datetime.now().isoformat()
        }
        
        return parsed_data
    
    def _call_ollama_api(self, prompt: str, system_prompt: str = None) -> str:
        """
        Call the Ollama API to get LLM responses.
        
        This method demonstrates Fixed Automation with LLM enhancement:
        - Local LLM processing for report generation
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
    
    def generate_report(self, parsed_data):
        """
        Generate a fixed-format weather report with Ollama enhancement.
        
        This method demonstrates fixed automation with LLM enhancement:
        - Uses predetermined template structure
        - Enhances descriptions with Ollama
        - No decision-making about report content
        - Fixed output format with AI-generated insights
        """
        print("Generating weather report...")
        
        # Try to enhance the report with Ollama
        try:
            # Create a prompt for Ollama to generate weather insights
            weather_prompt = f"""
            Based on this weather data, provide a brief, friendly weather summary:
            
            Temperature: {parsed_data['temperature']}°C
            Feels Like: {parsed_data['feels_like']}°C
            Humidity: {parsed_data['humidity']}%
            Pressure: {parsed_data['pressure']} hPa
            Description: {parsed_data['description']}
            Wind Speed: {parsed_data['wind_speed']} m/s
            Location: {parsed_data['city']}, {parsed_data['country']}
            
            Provide a brief, friendly weather summary in 2-3 sentences.
            """
            
            # Get AI-generated weather summary
            ai_summary = self._call_ollama_api(
                weather_prompt,
                system_prompt="You are a friendly weather reporter. Provide brief, helpful weather summaries."
            )
            
            # Fixed report template with AI enhancement
            report = f"""
WEATHER REPORT
==============
City: {parsed_data['city']}, {parsed_data['country']}
Date: {parsed_data['timestamp']}

Current Conditions:
- Temperature: {parsed_data['temperature']}°C
- Feels Like: {parsed_data['feels_like']}°C
- Humidity: {parsed_data['humidity']}%
- Pressure: {parsed_data['pressure']} hPa
- Description: {parsed_data['description'].title()}
- Wind Speed: {parsed_data['wind_speed']} m/s

AI Weather Summary:
{ai_summary.strip()}

Report generated by Fixed Automation Weather Agent (Enhanced with Ollama)
"""
            
        except Exception as e:
            print(f"Ollama enhancement failed: {e}")
            print("Falling back to basic report format...")
            
            # Fallback to basic report if Ollama fails
            report = f"""
WEATHER REPORT
==============
City: {parsed_data['city']}, {parsed_data['country']}
Date: {parsed_data['timestamp']}

Current Conditions:
- Temperature: {parsed_data['temperature']}°C
- Feels Like: {parsed_data['feels_like']}°C
- Humidity: {parsed_data['humidity']}%
- Pressure: {parsed_data['pressure']} hPa
- Description: {parsed_data['description'].title()}
- Wind Speed: {parsed_data['wind_speed']} m/s

Report generated by Fixed Automation Weather Agent
"""
        
        return report
    
    def save_report(self, report):
        """
        Save report to a file with fixed naming convention.
        
        This method demonstrates fixed automation:
        - Fixed file naming pattern
        - No organization by date or weather type
        - No decision-making about where to save
        - Overwrites previous reports
        """
        print("Saving weather report...")
        
        # Fixed filename pattern
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"weather_report_{timestamp}.txt"
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w') as f:
            f.write(report)
        
        print(f"Report saved to: {filepath}")
        return filepath
    
    def run(self):
        """
        Execute the fixed automation workflow.
        
        This method demonstrates the rigid, step-by-step nature of fixed automation:
        - Follows exact sequence of steps
        - No branching or decision-making
        - Fails on any error
        - No recovery mechanisms
        """
        print("Starting Fixed Automation Weather Agent...")
        print("=" * 50)
        
        try:
            # Step 1: Fetch weather data (fixed step)
            weather_data = self.fetch_weather_data()
            
            # Step 2: Parse weather data (fixed step)
            parsed_data = self.parse_weather_data(weather_data)
            
            # Step 3: Generate report (fixed step)
            report = self.generate_report(parsed_data)
            
            # Step 4: Save report (fixed step)
            filepath = self.save_report(report)
            
            print("=" * 50)
            print("Fixed Automation Weather Agent completed successfully!")
            print(f"Report saved to: {filepath}")
            
        except Exception as e:
            # Fixed error handling - just print and exit
            print(f"Error: {e}")
            print("Fixed Automation Agent failed - no recovery possible")
            return False
        
        return True


def main():
    """
    Main function to run the fixed automation weather agent.
    
    This demonstrates the simplicity and rigidity of fixed automation:
    - No configuration options
    - No user interaction
    - No decision-making
    - Just execute the predetermined workflow
    """
    print("Fixed Automation Agent Example: Weather Reporter")
    print("This agent demonstrates Level -1 characteristics:")
    print("- Rigid, pre-programmed behavior")
    print("- No decision-making capabilities")
    print("- No adaptation to unexpected inputs")
    print("- High efficiency for repetitive tasks")
    print("- Enhanced with Ollama for better report generation")
    print()
    
    # Check if Ollama is running (optional enhancement)
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        if response.status_code == 200:
            print("✅ Ollama is available - reports will be enhanced with AI")
        else:
            print("⚠️  Ollama not responding - using basic report format")
    except Exception as e:
        print("⚠️  Ollama not available - using basic report format")
        print("   Install Ollama from https://ollama.ai/ for enhanced reports")
    
    print()
    
    # Create and run the agent
    agent = WeatherReporterAgent()
    success = agent.run()
    
    if success:
        print("\n✅ Agent completed successfully!")
    else:
        print("\n❌ Agent failed - this is expected behavior for fixed automation")
        print("   when encountering unexpected inputs or API failures")


if __name__ == "__main__":
    main()
