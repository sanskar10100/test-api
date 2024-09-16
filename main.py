from typing import Union, List
from datetime import datetime
import json

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Meeting(BaseModel):
    start_time: str
    end_time: str
    description: str
    participants: List[str]

@app.get("/meetings", response_model=List[Meeting])
async def get_meetings(date: str):
    """
    Function to handle API endpoint logic.
    """
    try:
        # Parse the date from the query parameter (assuming format "dd/MM/yyyy").
        parsed_date = datetime.strptime(date, "%d/%m/%Y").date()
    except ValueError:
        return [] # Return empty list if date format is invalid

    day_number = (parsed_date - datetime(2024, 9, 16).date()).days + 1

    if 1 <= day_number <= 14:
        file_path = f"{day_number}.json"  # Construct the file path
        try:
            with open(file_path, "r") as f:
                result = json.load(f)
        except FileNotFoundError:
            result = []  # Return empty list if file not found
    else:
        result = []  # Default response if the date is outside the range

    return result
