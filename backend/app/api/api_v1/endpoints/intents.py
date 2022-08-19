
from google.cloud.dialogflow_v2 import IntentsAsyncClient, Intent, GetAgentRequest, AgentsAsyncClient, CreateIntentRequest, types
from fastapi import Body, APIRouter, HTTPException
from typing import Any, List
from app.schemas.common import IGetResponseBase
from ....schemas.intent import IIntent
from ....schemas.common import IPostResponseBase

from google.protobuf.json_format import MessageToDict

router = APIRouter()

@router.post("/intent/create/{project_id}", response_model=IPostResponseBase)
async def create_intent(
    project_id: str = "mybotivantest",
    display_name: str = Body(default="greet") 
) -> Any:
    # Create a client
    agent_client = AgentsAsyncClient()
    parent = agent_client.common_project_path(project_id)

     # Initialize request argument(s)
    request = GetAgentRequest(
        parent=parent,
    )

    # Make the request
    response = await agent_client.get_agent(request=request)

    if response:
        intent_agent_client = IntentsAsyncClient()

        print(intent_agent_client.common_project_path(project_id)) 

        # Initialize request argument(s)
        intent = Intent()
        intent.display_name = display_name

        request = CreateIntentRequest(
            parent=f"projects/{project_id}/agent",
            intent=intent,
        )

        # Make the request
        response = await intent_agent_client.create_intent(request=request)
        new_response = MessageToDict(response._pb)

    return IPostResponseBase(data=new_response)