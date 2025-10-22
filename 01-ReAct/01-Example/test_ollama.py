#!/usr/bin/env python3
"""
Test script for the ReAct Weather Planning Agent.

This script tests if Ollama is working correctly with the ReAct agent.
"""

import requests
import json
import time
from config import OLLAMA_BASE_URL, OLLAMA_MODEL


def test_ollama_connection():
    """Test if Ollama is running and accessible."""
    print("Testing Ollama connection...")
    
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        if response.status_code == 200:
            print("✅ Ollama is running and accessible")
            return True
        else:
            print(f"❌ Ollama returned status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Cannot connect to Ollama: {e}")
        return False


def test_model_availability():
    """Test if the required model is available."""
    print(f"Testing model {OLLAMA_MODEL} availability...")
    
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=10)
        if response.status_code == 200:
            models = response.json().get('models', [])
            model_names = [model['name'] for model in models]
            
            if OLLAMA_MODEL in model_names:
                print(f"✅ Model {OLLAMA_MODEL} is available")
                return True
            else:
                print(f"❌ Model {OLLAMA_MODEL} is not available")
                print(f"Available models: {', '.join(model_names)}")
                return False
        else:
            print(f"❌ Failed to get model list: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error checking models: {e}")
        return False


def test_model_response():
    """Test if the model can generate responses."""
    print("Testing model response generation...")
    
    try:
        payload = {
            "model": OLLAMA_MODEL,
            "prompt": "Hello, this is a test for the ReAct Weather Planning Agent. Please respond with 'ReAct model is working correctly.'",
            "stream": False,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9,
                "num_predict": 100
            }
        }
        
        print("Sending test prompt to model...")
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            model_response = result.get("response", "")
            print(f"✅ Model response received: {model_response}")
            return True
        else:
            print(f"❌ Model request failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error testing model: {e}")
        return False


def test_react_planning():
    """Test ReAct planning capabilities."""
    print("Testing ReAct planning capabilities...")
    
    try:
        # Test strategic thinking prompt
        planning_prompt = """
        You are a ReAct agent planning a weather activity. 
        Analyze this task: "Plan a weekend outdoor activity based on weather conditions"
        
        Provide a JSON response with:
        - task_type: Type of planning
        - weather_requirements: What weather is needed
        - confidence: Your confidence level (0-1)
        
        Respond only with valid JSON.
        """
        
        payload = {
            "model": OLLAMA_MODEL,
            "prompt": planning_prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9,
                "num_predict": 200
            }
        }
        
        print("Testing strategic thinking...")
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            model_response = result.get("response", "")
            print(f"✅ ReAct planning test successful")
            print(f"Response: {model_response}")
            return True
        else:
            print(f"❌ ReAct planning test failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error testing ReAct planning: {e}")
        return False


def test_weather_planning():
    """Test weather-specific planning."""
    print("Testing weather planning capabilities...")
    
    try:
        weather_prompt = """
        You are a weather planning agent. 
        Create a plan for: "Plan a garden project considering seasonal weather trends"
        
        Provide a JSON response with:
        - task_type: Type of weather planning
        - weather_requirements: Weather conditions needed
        - time_horizon: Planning timeframe
        - confidence: Confidence level (0-1)
        
        Respond only with valid JSON.
        """
        
        payload = {
            "model": OLLAMA_MODEL,
            "prompt": weather_prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9,
                "num_predict": 200
            }
        }
        
        print("Testing weather planning...")
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            model_response = result.get("response", "")
            print(f"✅ Weather planning test successful")
            print(f"Response: {model_response}")
            return True
        else:
            print(f"❌ Weather planning test failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error testing weather planning: {e}")
        return False


def main():
    """Main test function."""
    print("ReAct Weather Planning Agent - Ollama Test")
    print("=" * 50)
    print()
    
    tests = [
        ("Ollama Connection", test_ollama_connection),
        ("Model Availability", test_model_availability),
        ("Model Response", test_model_response),
        ("ReAct Planning", test_react_planning),
        ("Weather Planning", test_weather_planning)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"Running {test_name} test...")
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name} test passed")
            else:
                print(f"❌ {test_name} test failed")
        except Exception as e:
            print(f"❌ {test_name} test failed with error: {e}")
        print()
    
    print("=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✅ All tests passed! Your ReAct Weather Planning Agent is ready!")
        print()
        print("You can now run:")
        print("  python react_weather_agent.py")
    else:
        print("❌ Some tests failed. Please check the setup.")
        print()
        print("Try running:")
        print("  python setup_ollama.py")
    
    return passed == total


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
