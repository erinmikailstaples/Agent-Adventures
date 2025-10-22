#!/usr/bin/env python3
"""
Example runner for the Fixed Automation Weather Agent.

This script demonstrates how to use the weather agent and shows
the characteristics of Level -1 Fixed Automation.
"""

import os
import sys
import time
from dino_agent import DinosaurReporterAgent
from config import *

def demonstrate_fixed_automation():
    """
    Demonstrate the characteristics of fixed automation.
    
    This function shows:
    - Rigid, predetermined behavior
    - No decision-making capabilities
    - No adaptation to unexpected inputs
    - High efficiency for repetitive tasks
    """
    print("=" * 60)
    print("FIXED AUTOMATION AGENT DEMONSTRATION")
    print("=" * 60)
    print()
    
    print("Level -1: Fixed Automation Characteristics:")
    print("✅ Follows exact, predetermined steps")
    print("✅ High efficiency for repetitive tasks")
    print("✅ Predictable, consistent behavior")
    print("❌ Cannot adapt to unexpected inputs")
    print("❌ Cannot make decisions")
    print("❌ Cannot learn from experience")
    print("❌ Fails when encountering unplanned scenarios")
    print()
    
    print("This agent will:")
    print("1. Fetch weather data from API")
    print("2. Parse the data into a fixed format")
    print("3. Generate a simple report")
    print("4. Save the report to a file")
    print("5. Exit (no further processing)")
    print()
    
    # Check if API key is set
    if WEATHER_API_KEY == "your_openweathermap_api_key_here":
        print("⚠️  WARNING: Weather API key not set!")
        print("   Please set your OpenWeatherMap API key in config.py")
        print("   Get a free API key at: https://openweathermap.org/api")
        print("   Note: The agent will use mock data if no API key is provided")
        print()
    
    # Check if Ollama is available (optional enhancement)
    try:
        import requests
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        if response.status_code == 200:
            print("✅ Ollama is available - reports will be enhanced with AI")
        else:
            print("⚠️  Ollama not responding - using basic report format")
    except Exception as e:
        print("⚠️  Ollama not available - using basic report format")
        print("   Install Ollama from https://ollama.ai/ for enhanced reports")
    
    # Create and run the agent
    agent = DinosaurReporterAgent()
    
    print("Starting Fixed Automation Weather Agent...")
    print("-" * 40)
    
    start_time = time.time()
    success = agent.run()
    end_time = time.time()
    
    print("-" * 40)
    print(f"Execution time: {end_time - start_time:.2f} seconds")
    
    if success:
        print("✅ Agent completed successfully!")
        print()
        print("Fixed Automation Results:")
        print("- Weather data fetched and processed")
        print("- Report generated and saved")
        print("- Agent completed its predetermined workflow")
        print("- No further processing or decision-making")
    else:
        print("❌ Agent failed!")
        print()
        print("This demonstrates a key limitation of fixed automation:")
        print("- Cannot recover from errors")
        print("- Cannot adapt to unexpected situations")
        print("- Fails when encountering unplanned scenarios")
    
    return success

def show_limitations():
    """
    Show the limitations of fixed automation.
    """
    print("=" * 60)
    print("FIXED AUTOMATION LIMITATIONS")
    print("=" * 60)
    print()
    
    print("What this agent CANNOT do:")
    print("❌ Make decisions based on weather conditions")
    print("❌ Adapt to different weather scenarios")
    print("❌ Learn from past interactions")
    print("❌ Handle API failures gracefully")
    print("❌ Customize output based on user preferences")
    print("❌ Integrate with other systems")
    print("❌ Provide personalized recommendations")
    print("❌ Retry failed operations")
    print("❌ Handle unexpected data formats")
    print()
    
    print("What this agent CAN do:")
    print("✅ Execute predetermined workflows efficiently")
    print("✅ Process data in a fixed format")
    print("✅ Generate consistent, predictable outputs")
    print("✅ Handle high-volume, repetitive tasks")
    print("✅ Run on a fixed schedule")
    print("✅ Follow exact, predetermined steps")
    print()

def show_when_to_use():
    """
    Show when to use fixed automation vs. more advanced agents.
    """
    print("=" * 60)
    print("WHEN TO USE FIXED AUTOMATION")
    print("=" * 60)
    print()
    
    print("✅ Perfect for:")
    for use_case in SUITABLE_USE_CASES:
        print(f"   • {use_case}")
    print()
    
    print("❌ NOT suitable for:")
    for use_case in UNSUITABLE_USE_CASES:
        print(f"   • {use_case}")
    print()
    
    print("If you need more sophisticated capabilities, consider:")
    print("   • Level 0: LLM-Enhanced - For understanding natural language")
    print("   • Level 1: ReAct - For reasoning and decision-making")
    print("   • Level 2: ReAct + RAG - For accessing external knowledge")
    print("   • Level 3: Tool-Enhanced - For integrating multiple systems")
    print("   • Level 4: Self-Reflecting - For learning from mistakes")
    print("   • Level 5: Memory-Enhanced - For personalized experiences")
    print("   • Level 6: Environment Controllers - For real-time control")
    print("   • Level 7: Self-Learning - For autonomous improvement")

def main():
    """
    Main function to run the demonstration.
    """
    print("Fixed Automation Weather Agent Example")
    print("This demonstrates Level -1: Fixed Automation")
    print()
    
    # Show when to use fixed automation
    show_when_to_use()
    print()
    
    # Show limitations
    show_limitations()
    print()
    
    # Demonstrate the agent
    success = demonstrate_fixed_automation()
    print()
    
    # Show next steps
    print("=" * 60)
    print("NEXT STEPS")
    print("=" * 60)
    print()
    
    if success:
        print("✅ The agent completed successfully!")
        print("   This demonstrates the efficiency of fixed automation")
        print("   for simple, repetitive tasks.")
    else:
        print("❌ The agent failed!")
        print("   This demonstrates the limitations of fixed automation")
        print("   when encountering unexpected situations.")
    
    print()
    print("To explore more advanced agent types:")
    print("   • Check out the other agent examples in this repository")
    print("   • Read the comprehensive guide in Agent-Types.md")
    print("   • Learn about the AI Agent Hierarchy")
    print()
    print("Remember: Choose the right level of agent sophistication")
    print("for your specific needs. Not every problem needs a Level 7 agent!")

if __name__ == "__main__":
    main()
