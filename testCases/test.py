import requests
import json

id = " " # Put the id of the Mcq created or id of existing mcq form database
non_existing_id = " " # Put the id in " " which does not exist in the database to check tests for non existing content

def test_create_question():  # Test for successful creation of MCQ
    response = requests.post(url = "http://127.0.0.1:8000/create", json={
    "question": "What is the capital of India?",
    "optionOne": "Mumbai",
    "optionTwo": "Kolkata",
    "optionThree": "Bangalore",
    "answer": "Chennai"
    })
    returned_content = json.loads(response.text)   # Convert String in Json
    assert returned_content["message"] == "MCQ added successfully to the database collection."
    assert response.status_code == 200

# test /read
def test_read_question():
    response = requests.get(url = "http://127.0.0.1:8000/read")
    returned_content = json.loads(response.text)
    assert returned_content["code"] == response.status_code # Test the response code sent by the read_all_question() against actual status code
    assert returned_content["message"] == "All MCQ(s) read successfully"
    assert response.headers.get('content-Length') != 0  # Test if length of content is not zero

#test /update
def test_update_question():
    response = requests.put(url = f"http://127.0.0.1:8000/update/{id}", json={
    "question": "What is the capital of India?",
    "optionOne": "Delhi",
    })
    returned_content = json.loads(response.text)
    assert returned_content["message"] == "Mcq updated successfully"
    assert returned_content["code"] == response.status_code # Test the response code sent by the update_question() against actual status code


# Update error testing
def test_error_update_question():
    response = requests.put(url = f"http://127.0.0.1:8000/update/{non_existing_id}", json={
    "question": "What is the capital of India?",
    "optionOne": "New york",
    })
    returned_content = json.loads(response.text)
    assert returned_content["message"] == "There was an error updating MCQ."
    assert returned_content["code"] == 404

# Test /delete
def test_delete_question():
    response = requests.delete(url = f"http://127.0.0.1:8000/delete/{id}")
    returned_content = json.loads(response.text)
    assert returned_content["message"] == "MCQ deleted successfully"
    assert returned_content["code"] == response.status_code

# Test error for /delete
def test_error_delete_question():
    response = response = requests.delete(url = f"http://127.0.0.1:8000/delete/{non_existing_id}")
    returned_content = json.loads(response.text)
    assert returned_content["message"] == f"MCQ with id {non_existing_id} doesn't exist"
    assert returned_content["code"] == 404