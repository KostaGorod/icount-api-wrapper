import asyncio
from typing import Optional
import aiohttp
from dataclasses import dataclass
from pydantic import BaseModel, EmailStr


@dataclass
class SessionParams:
    sid: str = None
    company: str = None
    username: str = None
    password: str = None
    version: str = "v3"
    is_ssl: bool = False
    timeout: int = 30  # in seconds
    verify_ssl: bool = True
    user_agent: str = None
    query_string_auth: bool = False


@dataclass
class iCountDocItem:
    description: str
    unitprice_incvat: int
    quantity: int
    tax_exempt: Optional[bool]


@dataclass
class iCountDoc:
    email: Optional[EmailStr]
    doctype: str


@dataclass
class RequestParams:
    method: str = None
    endpoint: str = None
    data: aiohttp.FormData = None
    use_data: bool = False
    params: dict = None
