#!/usr/bin/env python3
"""
ReAct Agent Example: Intelligent Weather Planner

This is a Level 1 ReAct agent that demonstrates:
- Strategic thinking and planning
- Multi-step decision making
- Dynamic problem solving
- Task decomposition
- Adaptive planning

The agent can plan complex weather-related activities using reasoning and action.
"""

import requests
import json
import datetime
import time
from typing import Dict, List, Optional, Tuple
from config import (
    OLLAMA_BASE_URL,
    OLLAMA_MODEL,
    WEATHER_API_KEY,
    DEFAULT_CITY,
    MAX_PLANNING_ITERATIONS,
    PLANNING_CONFIDENCE_THRESHOLD,
    ADAPTIVE_PLANNING_ENABLED,
    STRATEGIC_THINKING_DEPTH,
    WEATHER_PLANNING_HORIZON,
    ACTIVITY_CATEGORIES,
    PLANNING_STRATEGIES,
    PLANNING_TEMPLATES
)


class ReActWeatherAgent:
    """
    A ReAct agent that can plan and execute complex weather-related tasks.
    
    This agent demonstrates Level 1 characteristics:
    - Strategic thinking and planning
    - Multi-step decision making
    - Dynamic problem solving
    - Task decomposition
    - Adaptive planning
    """
    
    def __init__(self):
        self.ollama_base_url = OLLAMA_BASE_URL
        self.model = OLLAMA_MODEL
        self.weather_api_key = WEATHER_API_KEY
        self.default_city = DEFAULT_CITY
        
        # Planning state
        self.current_plan = None
        self.planning_iteration = 0
        self.planning_history = []
        
        # Weather data cache
        self.weather_cache = {}
    
    def plan_weather_activity(self, task_description: str) -> Dict:
        """
        Plan a weather-related activity using ReAct methodology.
        
        This method demonstrates ReAct capabilities:
        - Strategic thinking and planning
        - Multi-step decision making
        - Dynamic problem solving
        - Task decomposition
        """
        print(f"Planning weather activity: '{task_description}'")
        
        # Step 1: Analyze the task
        task_analysis = self._analyze_task(task_description)
        
        # Step 2: Create initial plan
        initial_plan = self._create_initial_plan(task_analysis)
        
        # Step 3: Execute planning iterations
        final_plan = self._execute_planning_iterations(initial_plan, task_analysis)
        
        # Step 4: Finalize plan
        finalized_plan = self._finalize_plan(final_plan)
        
        return finalized_plan
    
    def _analyze_task(self, task_description: str) -> Dict:
        """
        Analyze the weather planning task to understand requirements.
        
        This demonstrates ReAct strategic thinking:
        - Problem decomposition
        - Requirement analysis
        - Context understanding
        """
        print("Analyzing task requirements...")
        
        prompt = f"""
        Analyze this weather planning task and extract the following information:
        
        Task: "{task_description}"
        
        Please provide a JSON response with:
        - task_type: Type of weather planning (outdoor_activity, travel_planning, daily_schedule, etc.)
        - weather_requirements: What weather conditions are needed
        - time_horizon: How far ahead to plan (days)
        - location: Specific location if mentioned
        - constraints: Any limitations or requirements
        - success_criteria: How to measure success
        - confidence: How confident you are in the analysis (0-1)
        
        Respond only with valid JSON.
        """
        
        try:
            response = self._call_ollama_api(prompt, "You are a weather planning analyst. Respond only with valid JSON.")
            analysis = json.loads(response)
            print(f"Task analysis: {analysis}")
            return analysis
        except Exception as e:
            print(f"Error analyzing task: {e}")
            return {
                "task_type": "general_weather_planning",
                "weather_requirements": "moderate_conditions",
                "time_horizon": 3,
                "location": self.default_city,
                "constraints": "none",
                "success_criteria": "successful_activity_completion",
                "confidence": 0.5
            }
    
    def _create_initial_plan(self, task_analysis: Dict) -> Dict:
        """
        Create an initial plan based on task analysis.
        
        This demonstrates ReAct planning capabilities:
        - Strategic planning
        - Plan generation
        - Template-based planning
        """
        print("Creating initial plan...")
        
        task_type = task_analysis.get("task_type", "general_weather_planning")
        
        # Get planning template
        template = PLANNING_TEMPLATES.get(task_type, PLANNING_TEMPLATES["outdoor_activity"])
        
        # Create plan structure
        plan = {
            "task_type": task_type,
            "status": "planning",
            "steps": template["steps"].copy(),
            "current_step": 0,
            "completed_steps": [],
            "weather_conditions": {},
            "activities": [],
            "contingency_plans": [],
            "confidence": task_analysis.get("confidence", 0.5),
            "created_at": datetime.datetime.now().isoformat()
        }
        
        print(f"Initial plan created with {len(plan['steps'])} steps")
        return plan
    
    def _execute_planning_iterations(self, plan: Dict, task_analysis: Dict) -> Dict:
        """
        Execute planning iterations with reasoning and action.
        
        This demonstrates ReAct core methodology:
        - Iterative planning
        - Reasoning about next steps
        - Action execution
        - Plan updates
        """
        print("Executing planning iterations...")
        
        self.planning_iteration = 0
        
        while self.planning_iteration < MAX_PLANNING_ITERATIONS:
            print(f"\n--- Planning Iteration {self.planning_iteration + 1} ---")
            
            # Step 1: Reason about current state
            reasoning = self._reason_about_current_state(plan, task_analysis)
            
            # Step 2: Determine next action
            next_action = self._determine_next_action(plan, reasoning)
            
            # Step 3: Execute action
            action_result = self._execute_action(next_action, plan, task_analysis)
            
            # Step 4: Update plan based on result
            plan = self._update_plan_based_on_result(plan, action_result)
            
            # Step 5: Check if planning is complete
            if self._is_planning_complete(plan):
                print("Planning completed successfully!")
                break
            
            self.planning_iteration += 1
        
        return plan
    
    def _reason_about_current_state(self, plan: Dict, task_analysis: Dict) -> Dict:
        """
        Reason about the current planning state.
        
        This demonstrates ReAct reasoning capabilities:
        - State analysis
        - Problem identification
        - Solution generation
        """
        print("Reasoning about current state...")
        
        prompt = f"""
        Analyze the current planning state and provide reasoning:
        
        Current Plan: {json.dumps(plan, indent=2)}
        Task Analysis: {json.dumps(task_analysis, indent=2)}
        
        Provide a JSON response with:
        - current_status: Current planning status
        - issues_identified: Any problems or gaps
        - next_priorities: What should be addressed next
        - reasoning: Your reasoning process
        - confidence: Confidence in current state (0-1)
        
        Respond only with valid JSON.
        """
        
        try:
            response = self._call_ollama_api(prompt, "You are a strategic planning analyst. Respond only with valid JSON.")
            reasoning = json.loads(response)
            print(f"Reasoning: {reasoning}")
            return reasoning
        except Exception as e:
            print(f"Error in reasoning: {e}")
            return {
                "current_status": "planning_in_progress",
                "issues_identified": [],
                "next_priorities": ["continue_planning"],
                "reasoning": "Basic planning continuation",
                "confidence": 0.5
            }
    
    def _determine_next_action(self, plan: Dict, reasoning: Dict) -> Dict:
        """
        Determine the next action to take.
        
        This demonstrates ReAct decision-making:
        - Action selection
        - Priority determination
        - Strategic decision making
        """
        print("Determining next action...")
        
        # Get current step
        current_step = plan["current_step"]
        total_steps = len(plan["steps"])
        
        if current_step < total_steps:
            next_step = plan["steps"][current_step]
            action = {
                "type": "execute_step",
                "step": next_step,
                "step_index": current_step,
                "priority": "high"
            }
        else:
            # Plan is complete, finalize
            action = {
                "type": "finalize_plan",
                "priority": "high"
            }
        
        print(f"Next action: {action}")
        return action
    
    def _execute_action(self, action: Dict, plan: Dict, task_analysis: Dict) -> Dict:
        """
        Execute the determined action.
        
        This demonstrates ReAct action execution:
        - Step execution
        - Result generation
        - Action outcomes
        """
        print(f"Executing action: {action['type']}")
        
        if action["type"] == "execute_step":
            result = self._execute_planning_step(action, plan, task_analysis)
        elif action["type"] == "finalize_plan":
            result = self._finalize_planning(plan)
        else:
            result = {"status": "unknown_action", "success": False}
        
        print(f"Action result: {result}")
        return result
    
    def _execute_planning_step(self, action: Dict, plan: Dict, task_analysis: Dict) -> Dict:
        """
        Execute a specific planning step.
        
        This demonstrates ReAct step execution:
        - Step-specific logic
        - Weather data integration
        - Activity planning
        """
        step = action["step"]
        step_index = action["step_index"]
        
        print(f"Executing step: {step}")
        
        # Execute step-specific logic
        if "weather" in step.lower():
            result = self._execute_weather_step(plan, task_analysis)
        elif "activity" in step.lower():
            result = self._execute_activity_step(plan, task_analysis)
        elif "contingency" in step.lower():
            result = self._execute_contingency_step(plan, task_analysis)
        else:
            result = self._execute_general_step(step, plan, task_analysis)
        
        # Update plan with step completion
        plan["completed_steps"].append({
            "step": step,
            "step_index": step_index,
            "result": result,
            "completed_at": datetime.datetime.now().isoformat()
        })
        
        plan["current_step"] = step_index + 1
        
        return result
    
    def _execute_weather_step(self, plan: Dict, task_analysis: Dict) -> Dict:
        """
        Execute weather analysis step.
        
        This demonstrates ReAct weather integration:
        - Weather data analysis
        - Condition assessment
        - Weather-based planning
        """
        print("Executing weather analysis step...")
        
        # Get weather data (mock for now)
        weather_data = self._get_weather_data(task_analysis.get("location", self.default_city))
        
        # Analyze weather conditions
        weather_analysis = self._analyze_weather_conditions(weather_data)
        
        # Update plan with weather information
        plan["weather_conditions"] = weather_analysis
        
        return {
            "status": "weather_analyzed",
            "success": True,
            "weather_conditions": weather_analysis,
            "message": "Weather conditions analyzed successfully"
        }
    
    def _execute_activity_step(self, plan: Dict, task_analysis: Dict) -> Dict:
        """
        Execute activity planning step.
        
        This demonstrates ReAct activity planning:
        - Activity selection
        - Weather-appropriate activities
        - Activity optimization
        """
        print("Executing activity planning step...")
        
        # Get weather conditions
        weather_conditions = plan.get("weather_conditions", {})
        
        # Select appropriate activities
        activities = self._select_weather_appropriate_activities(weather_conditions, task_analysis)
        
        # Update plan with activities
        plan["activities"] = activities
        
        return {
            "status": "activities_planned",
            "success": True,
            "activities": activities,
            "message": "Activities planned successfully"
        }
    
    def _execute_contingency_step(self, plan: Dict, task_analysis: Dict) -> Dict:
        """
        Execute contingency planning step.
        
        This demonstrates ReAct contingency planning:
        - Backup plans
        - Alternative activities
        - Risk mitigation
        """
        print("Executing contingency planning step...")
        
        # Create contingency plans
        contingency_plans = self._create_contingency_plans(plan, task_analysis)
        
        # Update plan with contingencies
        plan["contingency_plans"] = contingency_plans
        
        return {
            "status": "contingencies_planned",
            "success": True,
            "contingency_plans": contingency_plans,
            "message": "Contingency plans created successfully"
        }
    
    def _execute_general_step(self, step: str, plan: Dict, task_analysis: Dict) -> Dict:
        """
        Execute a general planning step.
        
        This demonstrates ReAct general step execution:
        - Generic step handling
        - Plan updates
        - Step completion
        """
        print(f"Executing general step: {step}")
        
        # Simulate step execution
        time.sleep(1)  # Simulate processing time
        
        return {
            "status": "step_completed",
            "success": True,
            "message": f"Step '{step}' completed successfully"
        }
    
    def _update_plan_based_on_result(self, plan: Dict, action_result: Dict) -> Dict:
        """
        Update the plan based on action results.
        
        This demonstrates ReAct adaptive planning:
        - Plan updates
        - Result integration
        - Adaptive adjustments
        """
        print("Updating plan based on results...")
        
        # Update plan status
        if action_result.get("success", False):
            plan["status"] = "planning_in_progress"
        else:
            plan["status"] = "planning_failed"
        
        # Update confidence
        if action_result.get("success", False):
            plan["confidence"] = min(plan["confidence"] + 0.1, 1.0)
        else:
            plan["confidence"] = max(plan["confidence"] - 0.1, 0.0)
        
        # Store planning history
        self.planning_history.append({
            "iteration": self.planning_iteration,
            "action_result": action_result,
            "plan_state": plan.copy(),
            "timestamp": datetime.datetime.now().isoformat()
        })
        
        return plan
    
    def _is_planning_complete(self, plan: Dict) -> bool:
        """
        Check if planning is complete.
        
        This demonstrates ReAct completion criteria:
        - Plan completeness
        - Success criteria
        - Quality thresholds
        """
        # Check if all steps are completed
        all_steps_completed = plan["current_step"] >= len(plan["steps"])
        
        # Check confidence threshold
        confidence_met = plan["confidence"] >= PLANNING_CONFIDENCE_THRESHOLD
        
        # Check if plan has required components
        has_weather = "weather_conditions" in plan and plan["weather_conditions"]
        has_activities = "activities" in plan and plan["activities"]
        has_contingencies = "contingency_plans" in plan and plan["contingency_plans"]
        
        components_complete = has_weather and has_activities and has_contingencies
        
        return all_steps_completed and confidence_met and components_complete
    
    def _finalize_plan(self, plan: Dict) -> Dict:
        """
        Finalize the planning process.
        
        This demonstrates ReAct plan finalization:
        - Plan completion
        - Final validation
        - Result preparation
        """
        print("Finalizing plan...")
        
        # Mark plan as complete
        plan["status"] = "completed"
        plan["completed_at"] = datetime.datetime.now().isoformat()
        
        # Add final summary
        plan["summary"] = self._generate_plan_summary(plan)
        
        # Store final plan
        self.current_plan = plan
        
        return plan
    
    def _generate_plan_summary(self, plan: Dict) -> str:
        """
        Generate a summary of the completed plan.
        
        This demonstrates ReAct result generation:
        - Plan summarization
        - Key highlights
        - User-friendly output
        """
        summary = f"""
Weather Planning Summary
=======================
Task Type: {plan.get('task_type', 'Unknown')}
Status: {plan.get('status', 'Unknown')}
Confidence: {plan.get('confidence', 0):.1%}
Steps Completed: {len(plan.get('completed_steps', []))}

Weather Conditions: {plan.get('weather_conditions', {})}
Planned Activities: {plan.get('activities', [])}
Contingency Plans: {plan.get('contingency_plans', [])}

Plan created at: {plan.get('created_at', 'Unknown')}
Plan completed at: {plan.get('completed_at', 'Unknown')}
        """
        
        return summary.strip()
    
    def _get_weather_data(self, location: str) -> Dict:
        """
        Get weather data for the location.
        
        This demonstrates ReAct data integration:
        - Weather data retrieval
        - Data processing
        - Information extraction
        """
        # Mock weather data for demonstration
        mock_weather = {
            "location": location,
            "temperature": 22,
            "humidity": 65,
            "wind_speed": 10,
            "description": "partly cloudy",
            "forecast": [
                {"day": "today", "temp": 22, "condition": "partly cloudy"},
                {"day": "tomorrow", "temp": 25, "condition": "sunny"},
                {"day": "day_after", "temp": 20, "condition": "rainy"}
            ]
        }
        
        return mock_weather
    
    def _analyze_weather_conditions(self, weather_data: Dict) -> Dict:
        """
        Analyze weather conditions for planning.
        
        This demonstrates ReAct analysis capabilities:
        - Weather interpretation
        - Condition assessment
        - Planning implications
        """
        analysis = {
            "overall_condition": weather_data.get("description", "unknown"),
            "temperature_range": f"{weather_data.get('temperature', 0)}°C",
            "humidity": f"{weather_data.get('humidity', 0)}%",
            "wind_conditions": f"{weather_data.get('wind_speed', 0)} km/h",
            "planning_recommendation": "suitable_for_outdoor_activities" if weather_data.get("temperature", 0) > 15 else "consider_indoor_alternatives"
        }
        
        return analysis
    
    def _select_weather_appropriate_activities(self, weather_conditions: Dict, task_analysis: Dict) -> List[str]:
        """
        Select activities appropriate for weather conditions.
        
        This demonstrates ReAct activity selection:
        - Weather-activity matching
        - Activity optimization
        - User preference consideration
        """
        condition = weather_conditions.get("overall_condition", "unknown")
        recommendation = weather_conditions.get("planning_recommendation", "")
        
        if "outdoor" in recommendation:
            activities = ["hiking", "picnic", "outdoor_photography", "gardening"]
        else:
            activities = ["indoor_museum", "cooking", "reading", "indoor_exercise"]
        
        return activities
    
    def _create_contingency_plans(self, plan: Dict, task_analysis: Dict) -> List[str]:
        """
        Create contingency plans for weather changes.
        
        This demonstrates ReAct contingency planning:
        - Backup plans
        - Alternative scenarios
        - Risk mitigation
        """
        contingencies = [
            "Indoor alternative activities",
            "Weather-appropriate clothing recommendations",
            "Flexible timing for outdoor activities",
            "Emergency weather response plan"
        ]
        
        return contingencies
    
    def _call_ollama_api(self, prompt: str, system_prompt: str = None) -> str:
        """
        Call the Ollama API to get LLM responses.
        
        This method demonstrates ReAct LLM integration:
        - Local LLM processing
        - Strategic reasoning
        - Planning assistance
        """
        try:
            # Prepare the request payload
            payload = {
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "top_p": 0.9,
                    "num_predict": 500
                }
            }
            
            # Add system prompt if provided
            if system_prompt:
                payload["system"] = system_prompt
            
            # Make the API call
            response = requests.post(
                f"{self.ollama_base_url}/api/generate",
                json=payload,
                timeout=60
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
    
    def get_planning_history(self) -> List[Dict]:
        """
        Get the planning history.
        
        This demonstrates ReAct planning tracking:
        - Planning iterations
        - Decision history
        - Learning potential
        """
        return self.planning_history
    
    def get_current_plan(self) -> Optional[Dict]:
        """
        Get the current plan.
        
        This demonstrates ReAct plan access:
        - Current plan state
        - Plan details
        - Planning status
        """
        return self.current_plan


def main():
    """
    Main function to run the ReAct Weather Planning Agent.
    
    This demonstrates the capabilities and limitations of Level 1 agents:
    - Strategic thinking and planning
    - Multi-step decision making
    - Dynamic problem solving
    - Task decomposition
    - Adaptive planning
    """
    print("ReAct Weather Planning Agent Example")
    print("This demonstrates Level 1: ReAct capabilities")
    print()
    
    # Check if Ollama is running
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        if response.status_code == 200:
            print("✅ Ollama is available - strategic planning will be enhanced")
        else:
            print("⚠️  Ollama not responding - using basic planning")
    except Exception as e:
        print("⚠️  Ollama not available - using basic planning")
        print("   Install Ollama from https://ollama.ai/ for enhanced planning")
    
    print()
    
    # Create and run the agent
    agent = ReActWeatherAgent()
    
    print("Starting ReAct Weather Planning Agent...")
    print("This agent can plan complex weather-related activities!")
    print()
    
    # Example planning tasks
    example_tasks = [
        "Plan a weekend outdoor activity based on weather conditions",
        "Create a travel itinerary considering weather forecasts",
        "Optimize my daily schedule based on weather patterns"
    ]
    
    for task in example_tasks:
        print(f"\n{'='*60}")
        print(f"Planning Task: {task}")
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
            
        except Exception as e:
            print(f"Error planning task: {e}")
    
    print(f"\n{'='*60}")
    print("ReAct Weather Planning Agent demonstration completed!")
    print("This shows the power of strategic thinking and multi-step planning!")
    print('='*60)


if __name__ == "__main__":
    main()
