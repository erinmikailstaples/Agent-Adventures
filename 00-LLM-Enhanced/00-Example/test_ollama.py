#!/usr/bin/env python3
"""
Test script for Ollama integration with the LLM-Enhanced Weather Agent.

This script tests the Ollama setup and basic functionality.
"""

import requests
import json
import time
from config import OLLAMA_BASE_URL, OLLAMA_MODEL


def test_ollama_connection():
    """Test if Ollama is running and accessible."""
    print("Testing Ollama connection...")
    
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=10)
        if response.status_code == 200:
            print("✅ Ollama is running and accessible")
            return True
        else:
            print(f"❌ Ollama returned status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Ollama. Make sure it's running on localhost:11434")
        return False
    except Exception as e:
        print(f"❌ Error connecting to Ollama: {e}")
        return False


def test_model_availability():
    """Test if the required model is available."""
    print(f"Testing model availability for {OLLAMA_MODEL}...")
    
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=10)
        if response.status_code == 200:
            models = response.json().get('models', [])
            model_names = [model.get('name', '') for model in models]
            
            if any(OLLAMA_MODEL in name for name in model_names):
                print(f"✅ Model {OLLAMA_MODEL} is available")
                return True
            else:
                print(f"❌ Model {OLLAMA_MODEL} is not available")
                print(f"Available models: {model_names}")
                return False
        else:
            print(f"❌ Failed to get model list: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error checking models: {e}")
        return False


def test_simple_generation():
    """Test basic text generation with Ollama."""
    print("Testing basic text generation...")
    
    try:
        payload = {
            "model": OLLAMA_MODEL,
            "prompt": "Hello, how are you? Please respond briefly.",
            "stream": False,
            "options": {
                "temperature": 0.7,
                "num_predict": 50
            }
        }
        
        print("Sending request to Ollama...")
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json=payload,
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            generated_text = result.get('response', '')
            print(f"✅ Generation successful: {generated_text[:100]}...")
            return True
        else:
            print(f"❌ Generation failed: {response.status_code} - {response.text}")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ Request timed out. The model might be too slow.")
        return False
    except Exception as e:
        print(f"❌ Error during generation: {e}")
        return False


def test_weather_agent_integration():
    """Test the weather agent integration."""
    print("Testing weather agent integration...")
    
    try:
        from llm_weather_agent import LLMWeatherAgent
        
        # Create agent instance
        agent = LLMWeatherAgent()
        
        # Test a simple weather query
        test_query = "What's the weather like today?"
        print(f"Testing query: '{test_query}'")
        
        response = agent.process_natural_language_query(test_query)
        print(f"✅ Agent response: {response[:100]}...")
        
        return True
        
    except ImportError as e:
        print(f"❌ Cannot import weather agent: {e}")
        return False
    except Exception as e:
        print(f"❌ Error testing weather agent: {e}")
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("OLLAMA INTEGRATION TEST")
    print("=" * 60)
    print()
    
    tests = [
        ("Ollama Connection", test_ollama_connection),
        ("Model Availability", test_model_availability),
        ("Basic Generation", test_simple_generation),
        ("Weather Agent Integration", test_weather_agent_integration)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n--- {test_name} ---")
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
            results.append((test_name, False))
    
    print("\n" + "=" * 60)
    print("TEST RESULTS")
    print("=" * 60)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Ollama integration is working correctly.")
        print("You can now run the weather agent:")
        print("  python llm_weather_agent.py")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please check the setup.")
        print("Run 'python setup_ollama.py' to fix common issues.")
    
    return passed == total


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
