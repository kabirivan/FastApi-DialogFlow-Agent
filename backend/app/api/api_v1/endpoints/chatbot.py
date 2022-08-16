import asyncio
from dataclasses import Field

from google.cloud import dialogflow_v2
from google.cloud.dialogflow_v2 import Agent
from google.cloud.dialogflow_v2 import AgentsClient, AgentsAsyncClient, SearchAgentsRequest
from fastapi import Body, APIRouter
from typing import Any, List
from pprint import pprint

from app.schemas.common import IGetResponseBase
from ....schemas.agent import IAgent

router = APIRouter()



@router.post("/chatbot/create", response_model=IGetResponseBase)
async def create_agent(
    project_id: str = Body(default="mybotivantest"), 
    display_name: str = Body(...)
) -> Any:

    agents_client = AgentsClient()

    parent = agents_client.common_project_path(project_id)

    pprint(vars(agents_client))

    agent = Agent(
        parent=parent,
        display_name=display_name,
        default_language_code="en",
        time_zone="America/Los_Angeles",
    )

    response = agents_client.set_agent(request={"agent": agent})

    return IGetResponseBase(data=response)


async def printHello():
    await asyncio.sleep(1)  # do something
    print('hello')

@router.get("/chatbot/{project_id}", response_model=IGetResponseBase[List[IAgent]])
async def search_agents(
    project_id: str = "mybotivantest", 
) -> Any:

    agents_client = AgentsAsyncClient()
    parent = agents_client.common_project_path(project_id)

    # Initialize request argument(s)
    request = SearchAgentsRequest(
        parent=parent,
    )

    # Make the request
    response = await agents_client.search_agents(request=request)

    print('response', response.agents)

    agent_output = []
    for agent in response.agents:
        new_agent: IAgent = IAgent(
            parent=agent.parent, 
            display_name=agent.display_name, 
            default_language_code=agent.default_language_code, 
            time_zone=agent.time_zone, 
            enable_logging=agent.enable_logging,
            match_mode=agent.match_mode,
            classification_threshold=agent.classification_threshold,
            api_version=agent.api_version,
            tier=agent.tier
            )
        agent_output.append(new_agent)

    return IGetResponseBase[List[IAgent]](data=agent_output)


# @router.get("/chatbot/{project_id}", response_model=IGetResponseBase)
# def train_agent():
#     # Create a client
#     client = dialogflow_v2.AgentsClient()

#     # Initialize request argument(s)
#     request = dialogflow_v2.TrainAgentRequest(
#         parent="parent_value",
#     )

#     # Make the request
#     operation = client.train_agent(request=request)

#     print("Waiting for operation to complete...")

#     response = operation.result()

#     # Handle the response
#     print(response)