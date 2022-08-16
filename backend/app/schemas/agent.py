
from pydantic import BaseModel
from typing import Optional, Sequence
from google.cloud import dialogflow_v2


class IAgent(BaseModel):
    parent: str
    display_name: str
    default_language_code:  str
    supported_language_codes: Optional[Sequence[str]]
    time_zone: str
    description: Optional[str]
    avatar_uri: Optional[str]
    enable_logging: bool
    match_mode: dialogflow_v2.types.Agent.MatchMode
    classification_threshold: float
    api_version: dialogflow_v2.types.Agent.ApiVersion
    tier: dialogflow_v2.types.Agent.Tier