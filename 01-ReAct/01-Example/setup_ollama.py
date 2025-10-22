#!/usr/bin/env python3
"""
Setup script for the ReAct Weather Planning Agent.

This script helps you set up Ollama and download the required model
for the ReAct agent to work properly.
"""

import requests
import json
import time
import subprocess
import sys
from config import OLLAMA_BASE_URL, OLLAMA_MODEL


def check_ollama_installed():
    """Check if Ollama is installed on the system."""
    try:
        result = subprocess.run(['ollama', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Ollama is installed: {result.stdout.strip()}")
            return True
        else:
            print("❌ Ollama is not installed")
            return False
    except FileNotFoundError:
        print("❌ Ollama is not installed")
        return False


def check_ollama_running():
    """Check if Ollama server is running."""
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        if response.status_code == 200:
            print("✅ Ollama server is running")
            return True
        else:
            print("❌ Ollama server is not responding")
            return False
    except Exception as e:
        print(f"❌ Ollama server is not running: {e}")
        return False


def start_ollama_server():
    """Start the Ollama server."""
    print("Starting Ollama server...")
    try:
        # Start Ollama server in the background
        subprocess.Popen(['ollama', 'serve'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("✅ Ollama server started")
        return True
    except Exception as e:
        print(f"❌ Failed to start Ollama server: {e}")
        return False


def check_model_available():
    """Check if the required model is available."""
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
            print("❌ Failed to check available models")
            return False
    except Exception as e:
        print(f"❌ Error checking models: {e}")
        return False


def download_model():
    """Download the required model."""
    print(f"Downloading model {OLLAMA_MODEL}...")
    print("This may take several minutes depending on your internet connection...")
    
    try:
        # Use ollama pull command to download the model
        result = subprocess.run(['ollama', 'pull', OLLAMA_MODEL], 
                              capture_output=True, text=True, timeout=1800)  # 30 minute timeout
        
        if result.returncode == 0:
            print(f"✅ Model {OLLAMA_MODEL} downloaded successfully")
            return True
        else:
            print(f"❌ Failed to download model: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print("❌ Model download timed out")
        return False
    except Exception as e:
        print(f"❌ Error downloading model: {e}")
        return False


def test_model():
    """Test if the model is working correctly."""
    print("Testing model...")
    
    try:
        payload = {
            "model": OLLAMA_MODEL,
            "prompt": "Hello, this is a test. Please respond with 'Model is working correctly.'",
            "stream": False
        }
        
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            model_response = result.get("response", "")
            print(f"✅ Model test successful: {model_response}")
            return True
        else:
            print(f"❌ Model test failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Model test failed: {e}")
        return False


def main():
    """Main setup function."""
    print("ReAct Weather Planning Agent - Ollama Setup")
    print("=" * 50)
    print()
    
    # Step 1: Check if Ollama is installed
    print("Step 1: Checking Ollama installation...")
    if not check_ollama_installed():
        print("\n❌ Ollama is not installed!")
        print("Please install Ollama from https://ollama.ai/")
        print("Then run this script again.")
        return False
    print()
    
    # Step 2: Check if Ollama server is running
    print("Step 2: Checking Ollama server...")
    if not check_ollama_running():
        print("Starting Ollama server...")
        if not start_ollama_server():
            print("❌ Failed to start Ollama server")
            return False
        
        # Wait for server to start
        print("Waiting for Ollama server to start...")
        time.sleep(5)
        
        if not check_ollama_running():
            print("❌ Ollama server failed to start")
            return False
    print()
    
    # Step 3: Check if model is available
    print("Step 3: Checking model availability...")
    if not check_model_available():
        print("Model not available, downloading...")
        if not download_model():
            print("❌ Failed to download model")
            return False
    print()
    
    # Step 4: Test the model
    print("Step 4: Testing model...")
    if not test_model():
        print("❌ Model test failed")
        return False
    print()
    
    print("✅ Setup completed successfully!")
    print(f"Your ReAct Weather Planning Agent is ready to use with {OLLAMA_MODEL}")
    print()
    print("You can now run:")
    print("  python react_weather_agent.py")
    print()
    print("For more information, see the README.md file.")
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
