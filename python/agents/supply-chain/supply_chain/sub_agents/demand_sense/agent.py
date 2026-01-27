# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Demand Sense Agent: gets power consumption demand forecasting"""

import time
import warnings
from google.genai import types
from google.adk.planners import BuiltInPlanner
from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool

from ...config import config
from . import prompts
from ...tools.demand_forecast import get_demand_forecast

warnings.filterwarnings("ignore", category=UserWarning)

demand_sense_agent = LlmAgent(
    model=config.model_name,
    name="DemandSenseAgent",
    description="Get demand forecasting of power consumption using Demand forecast tool based on the user question.",
    instruction=prompts.DEMAND_SENSE_AGENT_PROMPT,
    generate_content_config=types.GenerateContentConfig(
        temperature=config.temperature,
        top_p=config.top_p,
    ),
    planner=BuiltInPlanner(
        thinking_config=config.thinking_config
    ),
    tools=[
       FunctionTool(func=get_demand_forecast)
    ],
    output_key="demand_sense_report"
)
