import requests
import time

def interpretingResults(results):
    if len(results) == 1:
        print("Apologies, but the request was not formed properly.")
        return
    else:
        numCorrect = results['correctAnswers']
        numTotal = results['totalQuestions']
        percentageCorrect = results['overallScore']
        streak = results['longestStreak']
        grade = results['finalGrade']
        print("There were a total of " + str(numTotal) + " questions.")
        print("You got " + str(numCorrect) + " or " + str(percentageCorrect) + "%" + " correct.")
        print("Your best streak was " + str(streak) + " questions correct in a row.")
        print("You get a final grade of: " + grade + ".")
        return


sampleDict = '{"1": true,"2": true,"3": false,"4": true,"5": false,"6": false,"7": true,"8": true,"9": true,"10": true}'
sampleDict2 = '{"1": true,"2": true,"3": false,"4": true,"5": false}'
sampleDict3 = '{"1": true,"2": true,"3": false,"4": true,"5": false,"6": false,"7": true,"8": true,"9": true,"10": true, "11": false,"12": false,"13": false,"14": true,"15": false}'
sampleDict4 = '{"1": 42,"2": true,"3": false,"4": true,"5": false}'

requestOne = requests.post('http://127.0.0.1:8000/stats/', data=sampleDict)
print("Requesting first statistics ...")
requestOne = requestOne.json()
time.sleep(1)

interpretingResults(requestOne)
time.sleep(1)

requestTwo = requests.post('http://127.0.0.1:8000/stats/', data=sampleDict2)
print("Requesting second statistics ...")
requestTwo = requestTwo.json()
time.sleep(1)

interpretingResults(requestTwo)
time.sleep(1)

requestThree = requests.post('http://127.0.0.1:8000/stats/', data=sampleDict3)
print("Requesting third statistics ...")
requestThree = requestThree.json()
time.sleep(1)

interpretingResults(requestThree)
time.sleep(1)

requestFour = requests.post('http://127.0.0.1:8000/stats/', data=sampleDict4)
print("Requesting fourth statistics ...")
time.sleep(1)
requestFour = requestFour.json()

interpretingResults(requestFour)
time.sleep(1)

print("Test finished.")