
from ast import alias
from pydoc import text
from google.cloud.dialogflow_v2 import EntityTypesAsyncClient, ListEntityTypesRequest, AgentsAsyncClient, EntityType, CreateEntityTypeRequest, GetEntityTypeRequest
from pprint import pprint
from fastapi import Body, APIRouter, HTTPException, Query
from typing import Any, List, Sequence
from app.schemas.common import IGetResponseBase
from ....schemas.intent import IIntent, ITrainingPhrases
from ....schemas.common import IDeleteResponseBase, IPostResponseBase

from google.protobuf.json_format import MessageToDict

router = APIRouter()

@router.get("/entity/list/{project_id}", response_model=IGetResponseBase)
async def get_intent_list(
    project_id: str = "mybotivantest",
) -> Any:

    # Create a client
    agent_client = AgentsAsyncClient()
    parent = agent_client.agent_path(project_id)

    # Initialize request argument(s)
    request = ListEntityTypesRequest(
        parent=parent,
    )

    # Make the request
    entity_agent_client = EntityTypesAsyncClient()
    response = await entity_agent_client.list_entity_types(request=request)
    entities = response._response.entity_types

    entity_output = []
    for entity in entities:
        new_entity = MessageToDict(entity._pb)
        entity_output.append(new_entity)
        print('new_entity', new_entity)
        

    return IGetResponseBase(data=entity_output)


@router.get("/entity/{project_id}", response_model=IGetResponseBase)
async def get_entity_type(
    project_id: str = "mybotivantest",
    entity_id:  str = Query(default="cf62c5d8-2099-46aa-a0a0-9ccdec85ab81", description="ID Intent"),
) -> Any:

    # Create a client
    client = EntityTypesAsyncClient()

    # Initialize request argument(s)
    request = GetEntityTypeRequest(
        name="name_value",
    )

    # Make the request
    response = await client.get_entity_type(request=request)

    # Handle the response
    print(response)



@router.post("/entity/create/{project_id}", response_model=IPostResponseBase)
async def create_entity_type(
    project_id: str = "mybotivantest",
    display_name: str = Body(default="color")
) -> Any:

     # Create a client
    agent_client = AgentsAsyncClient()
    parent = agent_client.agent_path(project_id)

    # Initialize request argument(s)
    entity_type = EntityType()
    entity_type.display_name = display_name
    entity_type.kind = "KIND_REGEXP"

    request = CreateEntityTypeRequest(
        parent=parent,
        entity_type=entity_type,
    )

    # Make the request
    entity_agent_client = EntityTypesAsyncClient()
    response = await entity_agent_client.create_entity_type(request=request)

    # Handle the response
    print(response)
