import asyncio
from dataclasses import Field

from google.cloud.dialogflow_v2 import SetAgentRequest, AgentsAsyncClient, SearchAgentsRequest, TrainAgentRequest, Agent, DeleteAgentRequest
from fastapi import Body, APIRouter, HTTPException
from typing import Any, List
from pprint import pprint

from app.schemas.common import IGetResponseBase
from app.schemas.common import IDeleteResponseBase
from app.schemas.agent import IAgent

router = APIRouter()



@router.post("/chatbot/create", response_model=IGetResponseBase)
async def create_agent(
    project_id: str = Body(default="mybotivantest"), 
    display_name: str = Body(...)
) -> Any:

    agent_client = AgentsAsyncClient()

    parent = agent_client.common_project_path(project_id)

    print(agent_client)

    agent = Agent(
        parent=parent,
        display_name=display_name,
        default_language_code="en",
        time_zone="America/Los_Angeles",
    )

    request = SetAgentRequest(
        agent=agent,
    )

    # Make the request
    response = await agent_client.set_agent(request=request)
    print('response', response)

    new_agent: IAgent = IAgent(
            parent=response.parent, 
            display_name=response.display_name, 
            default_language_code=response.default_language_code, 
            time_zone=response.time_zone, 
            enable_logging=response.enable_logging,
            match_mode=response.match_mode,
            classification_threshold=response.classification_threshold,
            api_version=response.api_version,
            tier=response.tier
            )

    return IGetResponseBase(data=new_agent)


async def printHello():
    await asyncio.sleep(1)  # do something
    print('hello')

@router.get("/chatbot/{project_id}", response_model=IGetResponseBase[List[IAgent]])
async def search_agents(
    project_id: str = "mybotivantest", 
) -> Any:

    agent_client = AgentsAsyncClient()
    parent = agent_client.common_project_path(project_id)

    # Initialize request argument(s)
    request = SearchAgentsRequest(
        parent=parent,
    )

    # Make the request
    response = await agent_client.search_agents(request=request)
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


@router.post("/chatbot/train/{project_id}", response_model=IGetResponseBase)
async def train_agent(
    project_id: str = "mybotivantest", 
) -> Any:
    # Create a client
    agent_client = AgentsAsyncClient()
    parent = agent_client.common_project_path(project_id)

    # Initialize request argument(s)
    request = TrainAgentRequest(
        parent=parent,
    )

    # Make the request
    operation = await agent_client.train_agent(request=request)    

    response = await operation.done()

    if response:
        message = "The agent has been trained"
    else:
        message = "Something went wrong. Review your agent again."

    return IGetResponseBase(message=message)



@router.delete("/chatbot/delete/{project_id}", response_model=IDeleteResponseBase)
async def delete_agent(
    project_id: str = "mybotivantest", 
) -> Any:
    # Create a client
    agent_client = AgentsAsyncClient()
    parent = agent_client.common_project_path(project_id)

    print('parent', parent)

    request = SearchAgentsRequest(
            parent=parent,
        )
    response = await agent_client.search_agents(request=request)

    if len(response.agents) == 0:
        raise HTTPException(status_code=400, detail="It doesn't exist an agent.")
    
    else:
        # Initialize request argument(s)
        request = DeleteAgentRequest(
            parent=parent,
        )

        # Make the request
        response = await agent_client.delete_agent(request=request)

    return IDeleteResponseBase()