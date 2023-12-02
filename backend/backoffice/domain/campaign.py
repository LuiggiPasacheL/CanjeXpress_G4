from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Campaign:
    name: str
    discount: int
    start_date: str
    end_date: str
    brands: List[int]
    id: Optional[int] = None
