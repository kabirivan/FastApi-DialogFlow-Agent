
from ast import alias
from pydoc import text
from google.cloud.dialogflow_v2 import IntentsAsyncClient, Intent, GetAgentRequest, AgentsAsyncClient, CreateIntentRequest, GetIntentRequest, ListIntentsRequest
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
    request = ListIntentsRequest(
        parent=parent,
    )

    # Make the request
    intent_agent_client = IntentsAsyncClient()
    response = await intent_agent_client.list_intents(request=request)
    intents = response._response.intents

    intent_output = []
    for intent in intents:
        new_intent = MessageToDict(intent._pb)
        intent_output.append(new_intent)
        

    return IGetResponseBase(data=intent_output)


@router.post("/intent/create/{project_id}", response_model=IPostResponseBase)
async def create_intent(
    project_id: str = "mybotivantest",
    display_name: str = Body(default="greet"),
    training_phrases_parts: Sequence[ITrainingPhrases] = Body(...)
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

        print(training_phrases_parts)

        training_phrases = []
        for training_phrases_part in training_phrases_parts:
            print(training_phrases_part.parts[0])
            parts = training_phrases_part.parts
            new_parts = []
            for part in parts:
                new_part = Intent.TrainingPhrase.Part(text=part.text, entity_type=part.entity_type, alias=part.alias, user_defined=part.user_defined)
                new_parts.append(new_part)
            training_phrase = Intent.TrainingPhrase(parts=new_parts)
            training_phrases.append(training_phrase)

        print('training_phrases', training_phrases)

        # Initialize request argument(s)
        intent = Intent()
        intent.display_name = display_name
        intent.training_phrases = training_phrases

        request = CreateIntentRequest(
            parent=f"projects/{project_id}/agent",
            intent=intent,
        )

        # Make the request
        response = await intent_agent_client.create_intent(request=request)
        new_response = MessageToDict(response._pb)

    return IPostResponseBase(data=new_response)


@router.get("/intent/{project_id}", response_model=IGetResponseBase)
async def get_intent(
    project_id: str = "mybotivantest",
    intent_id:  str = Query(default="cf62c5d8-2099-46aa-a0a0-9ccdec85ab81", description="ID Intent"),
) -> Any:

    # Create a client
    intent_agent_client = IntentsAsyncClient()

    # Initialize request argument(s)
    request = GetIntentRequest(
        name=f"projects/{project_id}/agent/intents/{intent_id}",
    )

    # Make the request
    response = await intent_agent_client.get_intent(request=request)
    print('response', response.training_phrases)
    new_response = MessageToDict(response._pb)

    # Handle the response
    return IGetResponseBase(data=new_response)


@router.delete("/intent/{project_id}", response_model=IDeleteResponseBase)
async def delete_intent(
    project_id: str = "mybotivantest",
    intent_id:  str = Query(default="cf62c5d8-2099-46aa-a0a0-9ccdec85ab81", description="ID Intent")
) -> Any:
    """Delete intent with the given intent type and intent value."""

    intent_agent_client = IntentsAsyncClient()

    intent_path = intent_agent_client.intent_path(project_id, intent_id)
    print('intent_path', intent_path)

    response = await intent_agent_client.delete_intent(request={"name": intent_path})

    print('response', response)