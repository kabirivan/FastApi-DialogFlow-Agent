
from pydantic import BaseModel
from typing import Any, Optional, Sequence
from google.cloud import dialogflow_v2


class IPart(BaseModel):
    text: Optional[str]
    entity_type: Optional[str]
    alias: Optional[str]
    user_defined: Optional[bool]


class ITrainingPhrases(BaseModel):
    name: Optional[str]
    type_: Optional[dialogflow_v2.types.Intent.TrainingPhrase.Type]
    parts: Optional[IPart]
    times_added_count: Optional[int]


class IContext(BaseModel):
    name: Optional[str]
    lifespan_count: Optional[int]
    parameters: Optional[Any]


class IParameter(BaseModel):
    name: Optional[str]
    display_name: Optional[str]
    value: Optional[str]
    default_value: Optional[str]
    entity_type_display_name: Optional[str]
    mandatory: Optional[bool]
    prompts:Optional[Sequence[str]]
    is_list: Optional[bool]


class IIntent(BaseModel):
    name: Optional[str]
    display_name: Optional[str]
    webhook_state:  Optional[dialogflow_v2.types.Intent.WebhookState]
    priority: Optional[int]
    is_fallback: Optional[bool]
    ml_disabled: Optional[bool]
    live_agent_handoff: Optional[bool]
    end_interaction: Optional[bool]
    input_context_names: Optional[Sequence[str]]
    events: Optional[Sequence[str]]
    training_phrases: Optional[ITrainingPhrases]
    action: Optional[str]
    output_contexts: Optional[IContext]
    reset_contexts: Optional[bool]
    parameters: Optional[IParameter]
    messages: Optional[dialogflow_v2.types.Intent.Message]
    default_response_platforms: Optional[dialogflow_v2.types.Intent.Message.Platform]
    root_followup_intent_name: Optional[str]
    parent_followup_intent_name: Optional[str]
    followup_intent_info: Optional[dialogflow_v2.types.Intent.FollowupIntentInfo]



