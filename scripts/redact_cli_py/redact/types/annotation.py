

from dataclasses import dataclass
from typing import List


@dataclass
class Annotation:
    bounding_box: List[float]
    page: int
    field: str
    text: str
