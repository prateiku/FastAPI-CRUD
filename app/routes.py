from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from database import (
    createQuestion,
    readQuestions,
    updateQuestion,
    deleteQuestion,
)
from model import (
    ErrorResponseModel,
    ResponseModel,
    NewQuestionModel,
    UpdateQuestionModel,
)

router = APIRouter()  # For creating seperate path for API


# Route for creating resource
@router.post("/create")
async def create_question(quest_set: NewQuestionModel = Body(...)):
    questAdd = jsonable_encoder(quest_set)
    questCreate = await createQuestion(questAdd)
    # Successfully created MCQ
    return ResponseModel(questCreate, "MCQ added successfully to the database collection.")


# Route for reading created resource
@router.get("/read")
async def read_all_questions():
    isRead = await readQuestions()
    if isRead:
        # Success
        return ResponseModel(isRead, "All MCQ(s) read successfully")
    # Error
    return ResponseModel(isRead, "Empty MCQ list returned")


# Route for updating resource by its ID
@router.put("/update/{id}")
async def update_question(id: str, req: UpdateQuestionModel = Body(...)):
    # req is a dictionary that contains the fields which were updated by user
    # Eg. if user updates only question and optionOne res will have that value in key value pair
    req = {k: v for k, v in req.dict().items() if v is not None}
    isQuesUpdated = await updateQuestion(id, req)
    if isQuesUpdated:
        # If question successfully updated
        return ResponseModel(
            f"Mcq with ID: {id} updated",
            "Mcq updated successfully",
        )
    # If error 404 encountered
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating MCQ.",
    )


# Route for deleting resource by its ID
@router.delete("/delete/{id}")
async def delete_question(id: str):
    isDeleted = await deleteQuestion(id)
    if isDeleted:
        # If mcq deleted successfully
        return ResponseModel(
            f"MCQ with ID: {id} removed", "MCQ deleted successfully"
        )
    # If error 404 encountered
    return ErrorResponseModel(
        "An error occurred", 404, f"MCQ with id {id} doesn't exist"
    )
