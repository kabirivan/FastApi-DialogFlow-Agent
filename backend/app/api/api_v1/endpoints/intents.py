
from ast import alias
from pydoc import text
from google.cloud.dialogflow_v2 import IntentsAsyncClient, Intent, GetAgentRequest, AgentsAsyncClient, CreateIntentRequest, GetIntentRequest, ListIntentsRequest
from pprint import pprint
from fastapi import Body, APIRouter, HTTPException, Query
from typing import Any, List, Sequence
from app.schemas.common import IGetResponseBase
from ....schemas.intent import IIntent, ITrainingPhrases
from ....schemas.common import IPostResponseBase

from google.protobuf.json_format import MessageToDict

router = APIRouter()

@router.post("/intent/list/{project_id}", response_model=IGetResponseBase)
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
            part = Intent.TrainingPhrase.Part(text=training_phrases_part.parts[0].text, entity_type=training_phrases_part.parts[0].entity_type, alias=training_phrases_part.parts[0].alias, user_defined=training_phrases_part.parts[0].user_defined)
            training_phrase = Intent.TrainingPhrase(parts=[part])
            training_phrases.append(training_phrase)

        # print('training_phrases', training_phrases)

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
    intent_id:  str = Query(default="211e670d-7944-43eb-9aed-a41beab1ba2b", description="ID Intent"),
) -> Any:

    # Create a client
    intent_agent_client = IntentsAsyncClient()

    # Initialize request argument(s)
    request = GetIntentRequest(
        name=f"projects/{project_id}/agent/intents/{intent_id}",
    )

    # Make the request
    response = await intent_agent_client.get_intent(request=request)
    new_response = MessageToDict(response._pb)

    # Handle the response
    return IGetResponseBase(data=new_response)

