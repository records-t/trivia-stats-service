import json

from typing import Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Results(BaseModel):
    triviaResults: dict

@app.post("/stats/")
def read_results(userResults: dict):
    results = statsProcessing(userResults)
    if results == "Error":
        raise HTTPException(status_code=400, detail="Dictionary contains key value pair where value is not boolean, cannot be processed")
    print("Results processed. Now sending.")
    return results

def statsProcessing(userResults):
    numberTotal = 0
    numberCorrect = 0
    score = 0
    letterGrade = ""
    streak = 0
    longestStreak = 0
    
    for question, answer in userResults.items():
        
        if type(answer) != bool:
            return ("Error")
        
        numberTotal += 1
        
        if answer == True:
            numberCorrect += 1
            streak += 1
        
        if streak > longestStreak:
            longestStreak = streak
        
        if answer == False:
            streak = 0
    
    score = round(((numberCorrect/numberTotal) * 100), 1)
    
    if score >= 90:
        letterGrade = "A"
        
    if score <= 89 and score >= 80:
        letterGrade = "B"
    
    if score <= 79 and score >= 70:
        letterGrade = "C"
    
    if score <= 69 and score >= 60:
        letterGrade = "D"
    
    if score < 60:
        letterGrade = "F"
    
    newDict = {"correctAnswers": numberCorrect,
               "totalQuestions": numberTotal,
               "overallScore": score,
               "longestStreak": longestStreak,
               "finalGrade": letterGrade,}
    
    return newDict