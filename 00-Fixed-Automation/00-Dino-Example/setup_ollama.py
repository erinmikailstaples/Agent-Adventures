#!/usr/bin/env python3
"""
Setup script for Ollama integration with the Fixed Automation Weather Agent.

This script helps users set up Ollama for enhanced report generation.
"""

import subprocess
import sys
import requests
import time
import os


def check_ollama_installed():
    """Check if Ollama is installed."""
    try:
        result = subprocess.run(['ollama', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Ollama is installed: {result.stdout.strip()}")
            return True
        else:
            print("❌ Ollama is not installed or not in PATH")
            return False
    except FileNotFoundError:
        print("❌ Ollama is not installed or not in PATH")
        return False


def check_ollama_running():
    """Check if Ollama is running."""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            print("✅ Ollama is running on localhost:11434")
            return True
        else:
            print("❌ Ollama is not responding on localhost:11434")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Ollama is not running on localhost:11434")
        return False


def start_ollama():
    """Start Ollama service."""
    print("Starting Ollama service...")
    try:
        # Try to start Ollama in the background
        subprocess.Popen(['ollama', 'serve'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("✅ Ollama service started")
        
        # Wait a moment for it to start
        time.sleep(3)
        
        # Check if it's running
        if check_ollama_running():
            return True
        else:
            print("❌ Ollama failed to start properly")
            return False
            
    except Exception as e:
        print(f"❌ Error starting Ollama: {e}")
        return False


def check_model_available(model_name):
    """Check if a specific model is available."""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=10)
        if response.status_code == 200:
            models = response.json().get('models', [])
            for model in models:
                if model_name in model.get('name', ''):
                    print(f"✅ Model {model_name} is available")
                    return True
            print(f"❌ Model {model_name} is not available")
            return False
        else:
            print("❌ Could not check available models")
            return False
    except Exception as e:
        print(f"❌ Error checking models: {e}")
        return False


def download_model(model_name):
    """Download a model using Ollama."""
    print(f"Downloading model {model_name}...")
    print("This may take several minutes depending on your internet connection...")
    
    try:
        # Use subprocess to run ollama pull
        process = subprocess.Popen(
            ['ollama', 'pull', model_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            universal_newlines=True
        )
        
        # Stream the output
        for line in process.stdout:
            print(line.strip())
        
        process.wait()
        
        if process.returncode == 0:
            print(f"✅ Model {model_name} downloaded successfully")
            return True
        else:
            print(f"❌ Failed to download model {model_name}")
            return False
            
    except Exception as e:
        print(f"❌ Error downloading model: {e}")
        return False


def test_model(model_name):
    """Test if the model works."""
    print(f"Testing model {model_name}...")
    
    try:
        # Test with a simple prompt
        test_payload = {
            "model": model_name,
            "prompt": "Hello, how are you?",
            "stream": False
        }
        
        response = requests.post(
            "http://localhost:11434/api/generate",
            json=test_payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Model test successful: {result.get('response', '')[:100]}...")
            return True
        else:
            print(f"❌ Model test failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing model: {e}")
        return False


def main():
    """Main setup function."""
    print("=" * 60)
    print("OLLAMA SETUP FOR FIXED AUTOMATION WEATHER AGENT")
    print("=" * 60)
    print()
    
    print("This setup will enhance your Fixed Automation agent with:")
    print("✅ AI-generated weather summaries")
    print("✅ More natural language descriptions")
    print("✅ Enhanced report quality")
    print("✅ Local processing (no API costs)")
    print()
    
    # Step 1: Check if Ollama is installed
    print("Step 1: Checking if Ollama is installed...")
    if not check_ollama_installed():
        print()
        print("Please install Ollama first:")
        print("1. Visit https://ollama.ai/")
        print("2. Download and install Ollama for your operating system")
        print("3. Run this setup script again")
        return False
    
    print()
    
    # Step 2: Check if Ollama is running
    print("Step 2: Checking if Ollama is running...")
    if not check_ollama_running():
        print("Starting Ollama service...")
        if not start_ollama():
            print("Failed to start Ollama. Please start it manually:")
            print("  ollama serve")
            return False
    
    print()
    
    # Step 3: Check if the required model is available
    model_name = "llama3.2"
    print(f"Step 3: Checking if model {model_name} is available...")
    if not check_model_available(model_name):
        print(f"Model {model_name} not found. Downloading...")
        if not download_model(model_name):
            print("Failed to download model. Please try manually:")
            print(f"  ollama pull {model_name}")
            return False
    
    print()
    
    # Step 4: Test the model
    print("Step 4: Testing the model...")
    if not test_model(model_name):
        print("Model test failed. Please check your Ollama installation.")
        return False
    
    print()
    print("=" * 60)
    print("SETUP COMPLETE!")
    print("=" * 60)
    print()
    print("✅ Ollama is installed and running")
    print(f"✅ Model {model_name} is available and working")
    print()
    print("Your Fixed Automation Weather Agent will now generate:")
    print("  • AI-enhanced weather summaries")
    print("  • More natural language descriptions")
    print("  • Better report quality")
    print()
    print("You can now run the Fixed Automation Dino Agent:")
    print("  python dino_agent.py")
    print("  python run_example.py")
    print()
    print("The agent will use Ollama for enhanced report generation!")
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
