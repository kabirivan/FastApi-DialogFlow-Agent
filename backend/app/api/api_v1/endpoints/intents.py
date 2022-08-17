
from google.cloud.dialogflow_v2 import IntentsAsyncClient, Intent, SearchAgentsRequest, TrainAgentRequest, Agent, DeleteAgentRequest
from fastapi import Body, APIRouter, HTTPException
from typing import Any, List
from app.schemas.common import IGetResponseBase

router = APIRouter()

@router.post("/intent/create/{project_id}", response_model=IGetResponseBase)
async def create_intent(
    project_id: str = "mybotivantest", 
) -> Any:
    # Create a client
    agent_client = IntentsAsyncClient()
    parent = agent_client.common_project_path(project_id)

    # Initialize request argument(s)
    intent = Intent()
    intent.display_name = "display_name_value"

    request = dialogflow_v2.CreateIntentRequest(
        parent="parent_value",
        intent=intent,
    )

    # Make the request
    response = await client.create_intent(request=request)

    # Handle the response
    print(response)