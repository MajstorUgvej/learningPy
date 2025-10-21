#! /usr/bin/python3
import random
europe = {
    "Albania": "Tirana",
    "Andorra": "Andorra la Vella",
    "Austria": "Vienna",
    "Belarus": "Minsk",
    "Belgium": "Brussels",
    "Bosnia and Herzegovina": "Sarajevo",
    "Bulgaria": "Sofia",
    "Croatia": "Zagreb",
    "Cyprus": "Nicosia",
    "Czech Republic": "Prague",
    "Denmark": "Copenhagen",
    "Estonia": "Tallinn",
    "Finland": "Helsinki",
    "France": "Paris",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Hungary": "Budapest",
    "Iceland": "Reykjavik",
    "Ireland": "Dublin",
    "Italy": "Rome",
    "Kosovo": "Pristina",
    "Latvia": "Riga",
    "Liechtenstein": "Vaduz",
    "Lithuania": "Vilnius",
    "Luxembourg": "Luxembourg",
    "Malta": "Valletta",
    "Moldova": "Chisinau",
    "Monaco": "Monaco",
    "Montenegro": "Podgorica",
    "Netherlands": "Amsterdam",
    "North Macedonia": "Skopje",
    "Norway": "Oslo",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Romania": "Bucharest",
    "Russia": "Moscow",
    "San Marino": "San Marino",
    "Serbia": "Belgrade",
    "Slovakia": "Bratislava",
    "Slovenia": "Ljubljana",
    "Spain": "Madrid",
    "Sweden": "Stockholm",
    "Switzerland": "Bern",
    "Ukraine": "Kyiv",
    "United Kingdom": "London"
}

Tests = int(input("Enter how many test would you like to create: "))
Questions = min(int(input("Enter number of questions on each test(up to 45): ")), 45)

for i in range(0,Tests):
    # Kreate new file for a test
    name = 'test' + str(i+1) + '.txt'
    file = open(name, 'w')

    # shuffle and go through keys for as many questions as the user requested
    randomKeys = list(europe)
    random.shuffle(randomKeys)
    j = 1
    question = ""
    for key in randomKeys:
        question += str(j) + ') What is the capital of ' + key + ':\n'
        
        # create 3 false, and 1 true answer
        answers = {europe[key]} # using set so random would not repeat
        while len(answers) != 4:
            answers.add(europe[randomKeys[random.randint(0,44)]])
        answers = list(answers)
        random.shuffle(answers)

        # add answers to question
        for answer in answers:
            if(answer == europe[key]):
                question += '(TRUE) '
            question += answer + '\n'
        question+='\n'

        # break if we have enough questions
        if j == Questions:
            break
        j+=1
    file.write(question) 
    file.close()

print("Success!!!")