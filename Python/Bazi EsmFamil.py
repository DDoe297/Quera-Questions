"""
--------------------------------------------------
Name    : Bazi EsmFamil
Author  : Danial Khorasanizadeh
Link    : quera.ir/problemset/technology/87182
Date    : 13/Jun/2021
--------------------------------------------------
"""
import csv


class Participant:
    def __init__(self, name, answers):
        self.name = name
        self.answers = answers
        self.score = 0

    def getField(self, field):
        return self.answers.get(field)

    def getScore(self):
        return self.score

    def addScore(self, num):
        self.score += num


participants = []
data = {
    'esm': [],
    'famil': [],
    'keshvar': [],
    'rang': [],
    'ashia': [],
    'ghaza': [],
}


def ready_up():
    with open('esm_famil_data.csv', encoding='utf-8') as dataset:
        reader = csv.DictReader(dataset)
        for column in reader:
            data['esm'].append(column['esm'].replace(" ", ""))
            data['famil'].append(column['famil'].replace(" ", ""))
            data['keshvar'].append(column['keshvar'].replace(" ", ""))
            data['rang'].append(column['rang'].replace(" ", ""))
            data['ashia'].append(column['ashia'].replace(" ", ""))
            data['ghaza'].append(column['ghaza'].replace(" ", ""))


def add_participant(participant, answers):
    for answer in answers.keys():
        answers[answer] = answers[answer].replace(" ", "")
        if answers[answer] == "":
            answers[answer] = None
    participants.append(Participant(participant, answers))


def uniqe(participant, check):
    return list(check.values()).count(check[participant.name]) == 1


def valid(participant, check, fieldName):
    return check[participant.name] in data[fieldName]


def calculate_all():
    for field in data.keys():
        check = {}
        for participant in participants:
            check[participant.name] = participant.getField(field)
        if None in check.values():
            baseScore = 15
        else:
            baseScore = 10
        for participant in participants:
            if uniqe(participant, check) and valid(participant, check, field):
                participant.addScore(baseScore)
            elif valid(participant, check, field):
                participant.addScore(baseScore-5)
    scores = {}
    for participant in participants:
        scores[participant.name] = participant.getScore()
    return scores
