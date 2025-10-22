#!/usr/bin/env python3
"""
Run example for the ReAct Weather Planning Agent.

This script demonstrates the capabilities of the ReAct agent.
"""

import requests
import time
from config import OLLAMA_BASE_URL, OLLAMA_MODEL


def check_ollama_availability():
    """Check if Ollama is available for enhanced planning."""
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get('models', [])
            model_names = [model['name'] for model in models]
            
            if OLLAMA_MODEL in model_names:
                print("✅ Ollama is available - strategic planning will be enhanced")
                return True
            else:
                print(f"⚠️  Ollama is running but model {OLLAMA_MODEL} is not available")
                print(f"Available models: {', '.join(model_names)}")
                print("Run 'python setup_ollama.py' to download the required model")
                return False
        else:
            print("⚠️  Ollama is not responding properly")
            return False
    except Exception as e:
        print(f"⚠️  Ollama is not available: {e}")
        print("Install Ollama from https://ollama.ai/ for enhanced planning")
        return False


def run_react_agent():
    """Run the ReAct Weather Planning Agent."""
    print("ReAct Weather Planning Agent Example")
    print("=" * 50)
    print()
    
    # Check Ollama availability
    ollama_available = check_ollama_availability()
    print()
    
    if not ollama_available:
        print("Running with basic planning capabilities...")
        print("For enhanced strategic planning, set up Ollama first.")
        print()
    
    # Import and run the agent
    try:
        from react_weather_agent import ReActWeatherAgent
        
        print("Starting ReAct Weather Planning Agent...")
        print("This agent demonstrates Level 1: ReAct capabilities")
        print()
        
        # Create agent
        agent = ReActWeatherAgent()
        
        # Example planning tasks
        example_tasks = [
            "Plan a weekend outdoor activity based on weather conditions",
            "Create a travel itinerary considering weather forecasts", 
            "Optimize my daily schedule based on weather patterns",
            "Plan a garden project considering seasonal weather trends",
            "Create a weather-based exercise routine"
        ]
        
        print("ReAct Agent Capabilities:")
        print("- Strategic thinking and planning")
        print("- Multi-step decision making")
        print("- Dynamic problem solving")
        print("- Task decomposition")
        print("- Adaptive planning")
        print()
        
        for i, task in enumerate(example_tasks, 1):
            print(f"{'='*60}")
            print(f"Planning Task {i}: {task}")
            print('='*60)
            
            try:
                # Plan the activity
                plan = agent.plan_weather_activity(task)
                
                print(f"\nPlanning completed!")
                print(f"Status: {plan.get('status', 'Unknown')}")
                print(f"Confidence: {plan.get('confidence', 0):.1%}")
                print(f"Steps completed: {len(plan.get('completed_steps', []))}")
                
                # Show plan summary
                if plan.get('summary'):
                    print(f"\nPlan Summary:")
                    print(plan['summary'])
                
                # Show planning history
                history = agent.get_planning_history()
                if history:
                    print(f"\nPlanning History:")
                    for j, iteration in enumerate(history):
                        print(f"  Iteration {j+1}: {iteration.get('action_result', {}).get('status', 'Unknown')}")
                
            except Exception as e:
                print(f"Error planning task: {e}")
            
            print()
        
        print("=" * 60)
        print("ReAct Weather Planning Agent demonstration completed!")
        print("This shows the power of strategic thinking and multi-step planning!")
        print()
        print("ReAct Agent Characteristics Demonstrated:")
        print("✅ Strategic thinking and planning")
        print("✅ Multi-step decision making")
        print("✅ Dynamic problem solving")
        print("✅ Task decomposition")
        print("✅ Adaptive planning")
        print()
        print("ReAct Agent Limitations:")
        print("❌ Cannot access real-time external data")
        print("❌ Cannot learn from past interactions")
        print("❌ Cannot integrate with external systems")
        print("❌ Cannot perform physical actions")
        print("❌ Limited to reasoning and planning")
        print("=" * 60)
        
    except ImportError as e:
        print(f"❌ Error importing ReAct agent: {e}")
        print("Make sure all dependencies are installed:")
        print("  pip install -r requirements.txt")
    except Exception as e:
        print(f"❌ Error running ReAct agent: {e}")


def main():
    """Main function."""
    print("ReAct Weather Planning Agent - Run Example")
    print("This demonstrates Level 1: ReAct capabilities")
    print()
    
    # Run the agent
    run_react_agent()
    
    print()
    print("For more information, see the README.md file.")
    print("To set up Ollama for enhanced planning, run:")
    print("  python setup_ollama.py")


if __name__ == "__main__":
    main()
