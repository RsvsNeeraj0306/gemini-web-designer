"""This module contains the Pydantic models for the chat application, 
including message structures, code snippets, and chat details."""
from uuid import uuid4
from datetime import datetime
from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field

class Prompt(BaseModel):
    """Represents a prompt for the AI model to generate a response.

    Args:
        BaseModel: Pydantic's base class for data validation and settings management.

    Attributes:
        input (str): The input text for the AI model to generate a response.
    """
    input: str

class MessageType(str, Enum):
    """Represents the type of message in a chat.

    Args:
        str: The underlying data type for the message type, which is a string.
        Enum: The Enum base class allows defining distinct constant values.

    Attributes:
        AI: Represents messages generated by the AI.
        USER: Represents messages sent by the user.
    """
    AI = "ai"
    USER = "user"

class Message(BaseModel):
    """Represents a single message in a chat conversation.

    Args:
        BaseModel: Pydantic's base class for data validation and settings management.

    Attributes:
        id (str): Unique identifier for the message, generated as a UUID.
        type (MessageType): Type of the message, either from the user or the AI.
        content (str): The actual content of the message.
    """
    id: str = Field(default_factory=lambda: uuid4().hex)
    type: MessageType = Field(default=MessageType.USER)
    content: str = Field(default="")

class Code(BaseModel):
    """Represents code snippets (HTML, CSS, JS) that can be associated with a chat or response.

    Args:
        BaseModel: Pydantic's base class for data validation and settings management.

    Attributes:
        html (str): The HTML code snippet associated with the chat or response.
        css (str): The CSS code snippet associated with the chat or response.
        js (str): The JavaScript code snippet associated with the chat or response.
    """
    html: str = Field(default="")
    css: str = Field(default="")
    js: str = Field(default="")

class Chat(BaseModel):
    """Represents a chat session containing messages, code, and metadata.

    Args:
        BaseModel: Pydantic's base class for data validation and settings management.

    Attributes:
        userId (str): Identifier for the user participating in the chat.
        messages (List[Message]): List of messages exchanged in the chat.
        name (str): Name or title of the chat session.
        code (Optional[Code]): Optional code snippets (HTML, CSS, JS) attached to the chat.
        createdAt (datetime): Timestamp of when the chat was created.
    """
    userId: str
    messages: List[Message] = []
    name: str = Field(default="New Chat")
    code: Code = Field(default_factory=Code)
    createdAt: datetime = Field(default_factory=datetime.now)

class Response(Code):
    """Represents a response from the chat, inheriting code snippets and including an explanation.

    Args:
        Code: Inherits HTML, CSS, and JS fields from the Code model.

    Attributes:
        explanation (str): Textual explanation provided with the response, describing the 
        code or message.
    """
    explanation: str = Field(default="")
