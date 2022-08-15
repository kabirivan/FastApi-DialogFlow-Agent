from google.cloud.dialogflow_v2 import Agent
from google.cloud.dialogflow_v2 import AgentsClient
from fastapi import Body, APIRouter
from typing import Any

from app.schemas.common import IGetResponseBase

router = APIRouter()



@router.post("/chatbot/create", response_model=IGetResponseBase)
async def create_agent(
    project_id: str = Body(...), 
    display_name: str = Body(...)
) -> Any:

    agents_client = AgentsClient()

    parent = agents_client.common_project_path(project_id)

    agent = Agent(
        parent=parent,
        display_name=display_name,
        default_language_code="en",
        time_zone="America/Los_Angeles",
    )

    response = agents_client.set_agent(request={"agent": agent})

    return IGetResponseBase(data=response)
