
from ast import alias
from pydoc import text
from google.cloud.dialogflow_v2 import EntityTypesAsyncClient, ListEntityTypesRequest, AgentsAsyncClient
from pprint import pprint
from fastapi import Body, APIRouter, HTTPException, Query
from typing import Any, List, Sequence
from app.schemas.common import IGetResponseBase
from ....schemas.intent import IIntent, ITrainingPhrases
from ....schemas.common import IDeleteResponseBase, IPostResponseBase

from google.protobuf.json_format import MessageToDict

router = APIRouter()

@router.get("/intent/list/{project_id}", response_model=IGetResponseBase)
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
    response = await entity_agent_client.list_intents(request=request)
    print('response', response)

    # intent_output = []
    # for intent in intents:
    #     new_intent = MessageToDict(intent._pb)
    #     intent_output.append(new_intent)
        

    # return IGetResponseBase(data=intent_output)


