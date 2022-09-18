from typing import Optional
import aiohttp
from dataclasses import dataclass
from pydantic import BaseModel, EmailStr


@dataclass
class iCountDocItem:
    description: str
    unitprice_incvat: int
    quantity: int
    tax_exempt: Optional[bool]
