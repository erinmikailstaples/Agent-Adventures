#!/usr/bin/env python3
"""
Fixed Automation Agent Example: Dinosaur Reporter

This is a Level -1 Fixed Automation agent that demonstrates:
- Rigid, pre-programmed behavior
- No decision-making capabilities
- No adaptation to unexpected inputs
- High efficiency for repetitive tasks
- Predictable, scripted behavior

The agent fetches dinosaur data and generates a simple report.
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
    OLLAMA_KEEP_ALIVE,
    NAME,
    DESCRIPTION
)


class DinosaurReporterAgent:
    """
    A fixed automation agent that fetches dinosaur data and generates reports.
    
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
        self.name = NAME
        self.description = DESCRIPTION
        self.output_dir = OUTPUT_DIR
        self.base_url = "https://dinosaur-facts-api.shultzlab.com/dinosaurs"
        
        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)
    
    def fetch_dino_data(self, name, description):
        """
        Fetch fetch dino data from the API.
        
        This method demonstrates fixed automation:
        - Makes a single API call
        - No retry logic or error handling
        - Fails if API is unavailable
        - No adaptation to different response formats
        """
        print(f"Fetching dinosaur data...")
        
        # Fixed parameters - no adaptation possible
        params = {
            'Name': name,
            'Description': description,
        }
        
        # Single API call - no retry mechanism
        response = requests.get(self.base_url, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            # Fixed error handling - just raise exception
            raise Exception(f"API request failed with status {response.status_code}")
    
    def parse_dino_data(self, dino_data):
        """
        Parse dinosaur data into a fixed format.
        
        This method demonstrates fixed automation:
        - Assumes specific data structure
        - No validation of data quality
        - Fails if data structure changes
        - No adaptation to different data formats
        """
        print("Parsing dinosaur data...")
        
        # Fixed parsing - assumes specific JSON structure
        # Will fail if API response format changes
        parsed_data = {
            'name': dino_data.get('name', 'Unknown'),
            'description': dino_data.get('description', 'No description available'),
            'period': dino_data.get('period', 'Unknown period'),
            'diet': dino_data.get('diet', 'Unknown diet'),
            'length': dino_data.get('length', 'Unknown length'),
            'weight': dino_data.get('weight', 'Unknown weight'),
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
        Generate a fixed-format dinosaur report with Ollama enhancement.
        
        This method demonstrates fixed automation with LLM enhancement:
        - Uses predetermined template structure
        - Enhances descriptions with Ollama
        - No decision-making about report content
        - Fixed output format with AI-generated insights
        """
        print("Generating dinosaur report...")
        
        # Try to enhance the report with Ollama
        try:
            # Create a prompt for Ollama to generate dinosaur insights
            dino_prompt = f"""
            Based on this dinosaur data, provide a brief, friendly dinosaur summary:
            
            Name: {parsed_data['name']}
            Description: {parsed_data['description']}
            
            Provide a brief, friendly dinosaur summary in 2-3 sentences.
            """
            
            # Get AI-generated dinosaur summary
            ai_summary = self._call_ollama_api(
                dino_prompt,
                system_prompt="You are Jeff Goldblum, respond as his character in Jurassic Park. Provide brief, interesting dinosaur summaries."
            )
            
            # Fixed report template with AI enhancement
            report = f"""
DINOSAUR REPORT
===============
Name: {parsed_data['name']}
Date: {parsed_data['timestamp']}

Dinosaur Information:
- Name: {parsed_data['name']}
- Description: {parsed_data['description']}


AI Dinosaur Summary:
{ai_summary.strip()}

Report generated by Fixed Automation Dinosaur Agent (Enhanced with Ollama)
"""
            
        except Exception as e:
            print(f"Ollama enhancement failed: {e}")
            print("Falling back to basic report format...")
            
            # Fallback to basic report if Ollama fails
            report = f"""
DINOSAUR REPORT
===============
Name: {parsed_data['name']}
Date: {parsed_data['timestamp']}

Dinosaur Information:
- Name: {parsed_data['name']}
- Description: {parsed_data['description']}


Report generated by Fixed Automation Dinosaur Agent
"""
        
        return report
    
    def save_report(self, report):
        """
        Save report to a file with fixed naming convention.
        
        This method demonstrates fixed automation:
        - Fixed file naming pattern
        - No organization by date or dinosaur type
        - No decision-making about where to save
        - Overwrites previous reports
        """
        print("Saving dinosaur report...")
        
        # Fixed filename pattern
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"dinosaur_report_{timestamp}.txt"
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
        print("Starting Fixed Automation Dinosaur Agent...")
        print("=" * 50)
        
        try:
            # Step 1: Fetch dinosaur data (fixed step)
            dino_data = self.fetch_dino_data("Tyrannosaurus", "Large carnivorous dinosaur")
            
            # Step 2: Parse dinosaur data (fixed step)
            parsed_data = self.parse_dino_data(dino_data)
            
            # Step 3: Generate report (fixed step)
            report = self.generate_report(parsed_data)
            
            # Step 4: Save report (fixed step)
            filepath = self.save_report(report)
            
            print("=" * 50)
            print("Fixed Automation Dinosaur Agent completed successfully!")
            print(f"Report saved to: {filepath}")
            
        except Exception as e:
            # Fixed error handling - just print and exit
            print(f"Error: {e}")
            print("Fixed Automation Agent failed - no recovery possible")
            return False
        
        return True


def main():
    """
    Main function to run the fixed automation dinosaur agent.
    
    This demonstrates the simplicity and rigidity of fixed automation:
    - No configuration options
    - No user interaction
    - No decision-making
    - Just execute the predetermined workflow
    """
    print("Fixed Automation Agent Example: Dinosaur Reporter")
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
    agent = DinosaurReporterAgent()
    success = agent.run()
    
    if success:
        print("\n✅ Agent completed successfully!")
    else:
        print("\n❌ Agent failed - this is expected behavior for fixed automation")
        print("   when encountering unexpected inputs or API failures")


if __name__ == "__main__":
    main()
