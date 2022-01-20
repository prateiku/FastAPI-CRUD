# FastAPI-CRUD
CRUD web app api using FastAPI framework
- Install dependencies:
  ` pip install -r requirements.txt `
- Add Mongo URI to `client = motor.motor_asyncio.AsyncIOMotorClient("Insert Mongo URI")` in database.py.
- Run FastAPI crud app by going in the directory and executing following command:
 `uvicorn main:app --reload`
- Open your browser and access `http://127.0.0.1:8000/docs` to test the api.

## Running test cases 
- NOTE: you need pytest to run test cases. Install pytest using `pip install pytest`.
- Add the existing ID and non-existing ID in `id = " "` and `non_existing_id = " "` in `test.py`.
- To run test cases, in testCases directory open command prompt and run `pytest test.py`.
#
![FastAPI docs](https://github.com/prateiku/FastAPI-CRUD/blob/main/docs.png)
