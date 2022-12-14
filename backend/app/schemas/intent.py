
from optparse import Option
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
    parts: Optional[Sequence[IPart]]
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


class IImage(BaseModel):
    image_uri: Optional[str]
    accessibility_text: Optional[str]

class IQuickReplies(BaseModel):
    title: Optional[str]
    quick_replies: Optional[Sequence[str]]

class IButton(BaseModel):
    text: Optional[str]
    postback: Optional[str]

class ICard(BaseModel):
    title: Optional[str]
    subtitle: Optional[Sequence[str]]
    image_uri: Optional[str]
    buttons: Optional[Sequence[IButton]]

class ISimpleResponse(BaseModel):
    text_to_speech: Optional[str]
    ssml: Optional[str]
    display_text: Optional[str]

class IBasicCard(BaseModel):
    title: Optional[str]
    subtitle: Optional[str]
    formatted_text: Optional[str]
    image: Optional[IImage]
    buttons: Optional[Sequence[IButton]]

class ISuggestion(BaseModel):
    title: Optional[str]

class ILinkOutSuggestion(BaseModel):
    destination_name: Optional[str]
    uri: Optional[str]

class IInfo(BaseModel):
    key: Optional[str]
    synonyms: Optional[Sequence[str]]

class IItem(BaseModel):
    info: Optional[IInfo]
    title: Optional[str]
    description: Optional[str]
    image: Optional[IImage]

class IListSelect(BaseModel):
    title: Optional[str]
    items: Optional[Sequence[IItem]]
    subtitle: Optional[str]

class ICarouselSelect(BaseModel):
    items: Optional[Sequence[IItem]]


class IOpenUrlAction(BaseModel):
    url: Optional[str]
    url_type_hint: Optional[dialogflow_v2.types.Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction.UrlTypeHint]

class IBrowseCarouselCardItem(BaseModel):
    open_uri_action: Optional[IOpenUrlAction]
    title: Optional[str]
    description: Optional[str]
    image: Optional[IImage]
    footer: Optional[str]

class IBrowseCarouselCard(BaseModel):
    items: Optional[Sequence[IBrowseCarouselCardItem]]
    image_display_options: Optional[dialogflow_v2.types.Intent.Message.BrowseCarouselCard.ImageDisplayOptions]


class IColumnProperties(BaseModel):
    header: Optional[str]
    horizontal_alignment: Optional[dialogflow_v2.types.Intent.Message.ColumnProperties.HorizontalAlignment]


class ITableCardCell(BaseModel):
    text: Optional[str]

class ITableCardRow(BaseModel):
    cells: Optional[Sequence[ITableCardCell]]
    divider_after: Optional[bool]

class ITableCard(BaseModel):
    title: Optional[str]
    subtitle: Optional[str]
    image: Optional[IImage]
    column_properties: Optional[Sequence[IColumnProperties]]
    rows: Optional[ITableCardRow]
    buttons: Optional[Sequence[IButton]]


class IResponseMediaObject(BaseModel):
    name: Optional[str]
    description: Optional[str]
    large_image: Optional[IImage]
    icon: Optional[IImage]
    content_url: Optional[str]

class IMediaContent(BaseModel):
    media_type: Optional[dialogflow_v2.types.Intent.Message.MediaContent.ResponseMediaType]
    media_objects: Optional[Sequence[IResponseMediaObject]]


class IMessage(BaseModel):
    text: Optional[Sequence[str]]
    image: Optional[IImage]
    quick_replies: Optional[IQuickReplies]
    card: Optional[ICard]
    payload: Optional[Any]
    simple_responses: Optional[ISimpleResponse]
    basic_card: Optional[IBasicCard]
    suggestions: Optional[Sequence[ISuggestion]]
    link_out_suggestion: Optional[ILinkOutSuggestion]
    list_select: Optional[IListSelect]
    carousel_select: Optional[ICarouselSelect]
    browse_carousel_card: Optional[IBrowseCarouselCardItem]
    table_card: Optional[ITableCard]
    media_content: Optional[IMediaContent]
    platform: Optional[dialogflow_v2.types.Intent.Message.Platform]

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
    messages: Optional[IMessage]
    default_response_platforms: Optional[dialogflow_v2.types.Intent.Message.Platform]
    root_followup_intent_name: Optional[str]
    parent_followup_intent_name: Optional[str]
    # followup_intent_info: Optional[dialogflow_v2.types.Intent.FollowupIntentInfo]



