# imports

import motor.motor_asyncio
from bson.objectid import ObjectId

client = motor.motor_asyncio.AsyncIOMotorClient(" ") # Insert Mongo URI
database = client.mcqDB # initialise database
mcqCollection = database.get_collection("mcqCollection") # Create collection


# dictionary initialized from Objects key,value pair
# used in readQuestions() and createQuestion()
def mcqDict(mcqdb) -> dict:
    return {
        "id": str(mcqdb["_id"]),
        "question": mcqdb["question"],
        "optionOne": mcqdb["optionOne"],
        "optionTwo": mcqdb["optionTwo"],
        "optionThree": mcqdb["optionThree"],
        "answer": mcqdb["answer"],
    }


# Create, Read, Update, Delete operations on documents from mcqCollection in mcqDB(mongo databas)

# Read all Mcq(s) present in the database
async def readQuestions():
    mcqList = []
    # Creating list of all documents in collection and appending to mcqList
    async for quests in mcqCollection.find():
        mcqList.append(mcqDict(quests))
    return mcqList


# Create a new Mcq in the collection 
async def createQuestion(mcq: dict) -> dict:
    newQuestion = await mcqCollection.insert_one(mcq)
    newQuestionID = await mcqCollection.find_one({"_id": newQuestion.inserted_id})
    return mcqDict(newQuestionID)


# Update a Mcq in collection by finding and matching ID
async def updateQuestion(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    # Find if given ID is present in the Database
    isFound = await mcqCollection.find_one({"_id": ObjectId(id)})
    # If ID present update
    if isFound:
        isUpdated = await mcqCollection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        # If MCQ updated
        if isUpdated:
            return True
        return False


# Delete a Mcq from the collection by finding and matching ID
async def deleteQuestion(id: str):
    # Find if given ID is present in the Database
    isDelFound = await mcqCollection.find_one({"_id": ObjectId(id)})
    # If ID present delete
    if isDelFound:
        await mcqCollection.delete_one({"_id": ObjectId(id)})
        return True
