from typing import Dict, List
from pydantic import BaseModel

class WordCounts(BaseModel):
    count_to_word_map: Dict[str, int]

class TranscriptAnalysis(BaseModel):
    quick_summary: str
    bullet_point_highlights: List[str]
    sentiment_analysis: str
    keywords: List[str]
