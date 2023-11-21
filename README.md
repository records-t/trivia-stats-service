# trivia-stats-service
Basic REST API microservice running on python Fast API and python Uvicorn for the web server. Takes statistics from a trivia app in JSON format to a POST endpoint and returns a JSON dictionary with the processed results. I am providing the main file and a sample client to demonstrate its functionality. If they are not installed already, you will need the Fast API package, the Uvicorn package (installed as part of Fast API depending on installation choice), and the requests package if you want to run the client.

Functionality is likely not fully finished; more features are likely to be implemented in the future.

Requests:
Currently only takes POST requests; will return a string that can be formatted to a JSON dictionary. Endpoint is currently (http://127.0.0.1:8000/stats/) but this will be changed once this is uploaded to a proper web server.

POST request must send a JSON object representing a dictionary {} where all values in the key:value pair must be boolean. It will send HTTP code 200 to indicate success, 400 if one of the values in the key:value pairs is not boolean, and 422 if the request is not a dictionary. 
(ex. Correct: '{"1": true,"2": true,"3": false,"4": true,"5": false}', Incorrect: '{"1": 42,"2": true,"3": false,"4": true,"5": false}')

Output will provide statistics in a dictionary in the format: {'correctAnswers': int, 'totalQuestions': int, 'overallScore': int, 'longestStreak': int, 'finalGrade': str}

correctAnswers is number of correct answers, totalQuestions is the total number of key:value pairs, overallScore is the percentage of questions correct, longestStreak is the 'streak' or the highest number correct in a row, and finalGrade is a letter representing the percentage (higher than 90: A, between 80 and 89: B, between 70  and 79: C, between 60 and 69: D, lower than 60: F).   

Implementation of call may vary depending on what format you are using to retrieve JSON data. I'll provide the python from the sample code here to demonstrate its functionality; implementation may look different in say, for instance, JavaScript.

As this is a POST call, sending and receiving is the same process: once sent to the POST endpoint, the data will also be received by the same request. Again, implementation may vary - usage of some API to handle promises in JavaScript, for instance, may be needed.

Sample Python call (using Requests package):

Input:

import requests

sampleDict = '{"1": true,"2": true,"3": false,"4": true,"5": false,"6": false,"7": true,"8": true,"9": true,"10": true}'
requestOne = requests.post('http://127.0.0.1:8000/stats/', data=sampleDict)
requestOne = requestOne.json()
print(requestOne)

Output:

Requesting first statistics ...
{'correctAnswers': 7, 'totalQuestions': 10, 'overallScore': 70.0, 'longestStreak': 4, 'finalGrade': 'C'}

UML Diagram:

![microserviceuml](https://github.com/records-t/trivia-stats-service/assets/148019253/225a46cb-3e4a-4956-ae01-873aa2588253)
