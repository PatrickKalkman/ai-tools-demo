from typing import List
from pydantic import BaseModel
from openai import OpenAI
from .data_types import TranscriptAnalysis

client = OpenAI()

def analyze_transcript(transcript: str, word_count: dict) -> TranscriptAnalysis:
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant analyzing transcripts.",
            },
            {"role": "user", "content": f"{transcript}\n\nWord Count: {word_count}"},
        ],
        response_format=TranscriptAnalysis,
    )

    message = completion.choices[0].message
    if message.parsed:
        return message.parsed
    else:
        raise ValueError("Failed to parse the response")
