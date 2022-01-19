# Imports
from typing import Optional
from pydantic import BaseModel, Field


# Model for creating new MCQ
class NewQuestionModel(BaseModel):
    question: str = Field(...)
    optionOne: str = Field(...)
    optionTwo: str = Field(...)
    optionThree: str = Field(...)
    answer: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "question": "What is the capital of India?",
                "optionOne": "Mumbai",
                "optionTwo": "Kolkata",
                "optionThree": "Delhi",
                "answer": "Chennai",
            }
        }


# Model with optional fields to update only specific values
# Model used in routes.update_question()
class UpdateQuestionModel(BaseModel):
    question: Optional[str]
    optionOne: Optional[str]
    optionTwo: Optional[str]
    optionThree: Optional[str]
    answer: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "question": "What is the capital of India?",
                "optionOne": "Mumbai",
                "optionTwo": "Bangalore",
                "optionThree": "Delhi",
                "answer": "Chennai",
            }
        }


# Returned when 200 response status
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


# Returned when 404 response status
def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
