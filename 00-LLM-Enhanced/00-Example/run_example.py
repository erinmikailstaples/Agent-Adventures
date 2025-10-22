#!/usr/bin/env python3
"""
Example runner for the LLM-Enhanced Weather Agent.

This script demonstrates how to use the LLM-enhanced weather agent and shows
the characteristics of Level 0 LLM-Enhanced agents.
"""

import os
import sys
import time
from llm_weather_agent import LLMWeatherAgent
from config import *

def demonstrate_llm_enhanced_capabilities():
    """
    Demonstrate the capabilities of LLM-Enhanced agents.
    
    This function shows:
    - Contextual understanding of natural language
    - Handling ambiguous inputs and variations
    - Operating within strict boundaries
    - High-volume processing of varied queries
    - Natural language generation
    """
    print("=" * 60)
    print("LLM-ENHANCED AGENT DEMONSTRATION")
    print("=" * 60)
    print()
    
    print("Level 0: LLM-Enhanced Characteristics:")
    print("✅ Contextual understanding of natural language")
    print("✅ Handles ambiguous inputs and variations")
    print("✅ Operates within strict boundaries")
    print("✅ High-volume processing of varied queries")
    print("✅ Natural language generation")
    print("❌ Cannot make complex decisions")
    print("❌ Cannot access real-time data sources")
    print("❌ Cannot learn from past interactions")
    print("❌ Cannot integrate with external systems")
    print()
    
    print("This agent can handle queries like:")
    for query in EXAMPLE_QUERIES[:5]:
        print(f"  • '{query}'")
    print()
    
    print("But cannot handle queries like:")
    for query in UNSUITABLE_QUERIES[:5]:
        print(f"  • '{query}'")
    print()
    
    # Check if Ollama is running
    try:
        import requests
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
    print("-" * 40)
    
    # Test with example queries
    test_queries = [
        "What's the weather like today?",
        "Is it going to rain this weekend?",
        "How hot is it in London?",
        "Should I bring an umbrella?",
        "What's the temperature in Paris?"
    ]
    
    for query in test_queries:
        print(f"\nTesting query: '{query}'")
        start_time = time.time()
        
        try:
            response = agent.process_natural_language_query(query)
            end_time = time.time()
            
            print(f"Response: {response}")
            print(f"Processing time: {end_time - start_time:.2f} seconds")
            
        except Exception as e:
            print(f"Error: {e}")
    
    print("-" * 40)
    print("✅ LLM-Enhanced Agent demonstration completed!")
    print()
    print("LLM-Enhanced Results:")
    print("- Natural language queries processed")
    print("- Contextual responses generated")
    print("- Boundaries enforced")
    print("- High-volume processing demonstrated")
    print("- Natural language understanding shown")
    
    return True

def show_llm_enhanced_capabilities():
    """
    Show the capabilities of LLM-Enhanced agents.
    """
    print("=" * 60)
    print("LLM-ENHANCED AGENT CAPABILITIES")
    print("=" * 60)
    print()
    
    print("What this agent CAN do:")
    for capability in LLM_ENHANCED_CAPABILITIES:
        print(f"✅ {capability}")
    print()
    
    print("What this agent CANNOT do:")
    for limitation in LLM_ENHANCED_LIMITATIONS:
        print(f"❌ {limitation}")
    print()

def show_when_to_use_llm_enhanced():
    """
    Show when to use LLM-Enhanced agents vs. other agent types.
    """
    print("=" * 60)
    print("WHEN TO USE LLM-ENHANCED AGENTS")
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
    print("   • Level 1: ReAct - For reasoning and decision-making")
    print("   • Level 2: ReAct + RAG - For accessing external knowledge")
    print("   • Level 3: Tool-Enhanced - For integrating multiple systems")
    print("   • Level 4: Self-Reflecting - For learning from mistakes")
    print("   • Level 5: Memory-Enhanced - For personalized experiences")
    print("   • Level 6: Environment Controllers - For real-time control")
    print("   • Level 7: Self-Learning - For autonomous improvement")

def run_interactive_demo():
    """
    Run an interactive demonstration of the LLM-Enhanced agent.
    """
    print("=" * 60)
    print("INTERACTIVE LLM-ENHANCED AGENT DEMO")
    print("=" * 60)
    print()
    
    # Check if Ollama is running
    try:
        import requests
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
    
    print("Starting interactive LLM-Enhanced Weather Agent...")
    print("This agent can understand natural language weather queries!")
    print()
    
    # Run interactive session
    agent.run_interactive_session()
    
    return True

def show_agent_comparison():
    """
    Show comparison between different agent types.
    """
    print("=" * 60)
    print("AGENT TYPE COMPARISON")
    print("=" * 60)
    print()
    
    print("Level -1: Fixed Automation")
    print("  • Rigid, predetermined behavior")
    print("  • No decision-making capabilities")
    print("  • High efficiency for repetitive tasks")
    print("  • Fails when encountering unplanned scenarios")
    print()
    
    print("Level 0: LLM-Enhanced (This Agent)")
    print("  • Contextual understanding of natural language")
    print("  • Handles ambiguous inputs and variations")
    print("  • Operates within strict boundaries")
    print("  • High-volume processing of varied queries")
    print("  • Natural language generation")
    print()
    
    print("Level 1: ReAct")
    print("  • Strategic thinking and planning")
    print("  • Multi-step decision making")
    print("  • Dynamic problem solving")
    print("  • Task decomposition")
    print("  • Adaptive planning")
    print()
    
    print("Level 2: ReAct + RAG")
    print("  • All ReAct capabilities")
    print("  • Real-time knowledge access")
    print("  • Domain-specific expertise")
    print("  • Informed decision making")
    print("  • High-stakes task handling")
    print()

def main():
    """
    Main function to run the demonstration.
    """
    print("LLM-Enhanced Weather Agent Example")
    print("This demonstrates Level 0: LLM-Enhanced capabilities")
    print()
    
    # Show capabilities
    show_llm_enhanced_capabilities()
    print()
    
    # Show when to use
    show_when_to_use_llm_enhanced()
    print()
    
    # Show agent comparison
    show_agent_comparison()
    print()
    
    # Demonstrate capabilities
    success = demonstrate_llm_enhanced_capabilities()
    print()
    
    # Show next steps
    print("=" * 60)
    print("NEXT STEPS")
    print("=" * 60)
    print()
    
    if success:
        print("✅ The agent demonstrated LLM-Enhanced capabilities!")
        print("   This shows the power of natural language understanding")
        print("   and contextual responses within strict boundaries.")
    else:
        print("❌ The agent demonstration failed!")
        print("   This might be due to missing API keys or configuration.")
    
    print()
    print("To explore more advanced agent types:")
    print("   • Check out the other agent examples in this repository")
    print("   • Read the comprehensive guide in Agent-Types.md")
    print("   • Learn about the AI Agent Hierarchy")
    print()
    print("Remember: Choose the right level of agent sophistication")
    print("for your specific needs. LLM-Enhanced agents are perfect")
    print("for natural language understanding and contextual responses!")

if __name__ == "__main__":
    main()
