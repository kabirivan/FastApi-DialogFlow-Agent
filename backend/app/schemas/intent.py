
from pydantic import BaseModel
from typing import Optional, Sequence
from google.cloud import dialogflow_v2


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
    training_phrases: Optional[dialogflow_v2.types.Intent.TrainingPhrase]
    action: Optional[str]
    output_contexts: Optional[dialogflow_v2.types.Context]
    reset_contexts: Optional[bool]
    parameters: Optional[dialogflow_v2.types.Intent.Parameter]
    messages: Optional[dialogflow_v2.types.Intent.Message]
    default_response_platforms: Optional[dialogflow_v2.types.Intent.Message.Platform]
    root_followup_intent_name: Optional[str]
    parent_followup_intent_name: Optional[str]
    followup_intent_info: Optional[dialogflow_v2.types.Intent.FollowupIntentInfo]
