import os
import sys
from dotenv import load_dotenv
from typing import List
from textwrap import dedent
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.exa import ExaTools
from agno.tools.duckduckgo import DuckDuckGoTools
from pydantic import BaseModel, Field
from rich.prompt import Prompt
from rich import print as rprint
from maps_tools import GoogleMapsTool
from prompts import system_prompt_travel_agent, expected_output, instructions

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
EXA_API_KEY = os.getenv('EXA_API_KEY')
MAPS_API_KEY = os.getenv('MAPS_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Check if required API keys are available
if not EXA_API_KEY:
    rprint("[bold red]ERROR: EXA_API_KEY not found in environment variables.[/bold red]")
    sys.exit(1)
    
if not MAPS_API_KEY:
    rprint("[bold red]ERROR: MAPS_API_KEY not found in environment variables.[/bold red]")
    sys.exit(1)
    
if not OPENAI_API_KEY:
    rprint("[bold red]ERROR: OPENAI_API_KEY not found in environment variables.[/bold red]")
    sys.exit(1)

# Print confirmation that keys were loaded
rprint(f"[green]✓ Environment variables loaded successfully[/green]")

# Define the Data Models
class MapURL(BaseModel):
    place_name: str = Field(None, description="The name of the place to search for")
    maps_url: str = Field(None, description="Google Maps URL for the place")

class MapURLs(BaseModel):
    urls: List[MapURL]

class Inputs(BaseModel):
    days: int = Field(None, description="Number of days for the trip")
    destination: str = Field(None, description="The destination of the trip")
    trip_date: str = Field(None, description="The date of the trip")
    budget: int = Field(None, description="The total budget for the trip")    

# Define the Agents
travel_planning_agent = Agent(
    name='Travel Planning Agent',
    model=OpenAIChat(id='gpt-4o-mini'),
    tools=[
        ExaTools(api_key=EXA_API_KEY),
    ],
    description=system_prompt_travel_agent,
    instructions=instructions,
    expected_output=expected_output,
    add_history_to_messages=True,
    add_datetime_to_instructions=True,
    debug_mode=False
)

map_agent = Agent(
    name='Google Map Agent',
    model=OpenAIChat(id='gpt-4o-mini'),
    description='You are equipped with Google Maps tools to extract place ID',
    tools=[GoogleMapsTool(api_key=MAPS_API_KEY)],
    show_tool_calls=False,
    debug_mode=False
)

duckduckgo_agent = Agent(
    name='DuckDuckGo Agent',
    model=OpenAIChat(id='gpt-4o-mini'),
    description='You are equipped with DuckDuckGo tools to help with searching business info on the web',
    tools=[DuckDuckGoTools()],
    show_tool_calls=False,
    debug_mode=False
)

team_agent = Agent(
    model=OpenAIChat(id='gpt-4o-mini'),
    team=[travel_planning_agent, map_agent, duckduckgo_agent],
    add_history_to_messages=True,
    description=dedent('''
    You are now connected to the **Travel Planning Agent**, the **Google Maps Agent**, and the **DuckDuckGo Agent**.

    The **Travel Planning Agent** will help you generate an initial itinerary based on your input.

    The **Google Maps Agent** will help you extract Google Maps URLs for accommodation and activities.

    The **DuckDuckGo Agent** will help you fill in any missing information about businesses and landmarks identified in the itinerary.
    '''),
    instructions=dedent('''
    # **Travel Planning Agent Instructions**

    ## 1. Generate the initial itinerary from travel planning agent based on the user's input.

    ## 2. Go through the itinerary and ensure that all locations and landmarks have a Google Maps URL included.

    ## 3. Use the DuckDuckGo Agent to fill any missing information about businesses and landmarks identified in the itinerary.
    '''),
    expected_output=expected_output,
    markdown=True,
    show_tool_calls=True,
)

if __name__ == '__main__':
    while True:
        user_prompt = Prompt.ask('User')
        if user_prompt == 'exit' or user_prompt == 'quit':
            sys.exit('Bye bye! 👋')

        team_agent.print_response(user_prompt, stream=True)