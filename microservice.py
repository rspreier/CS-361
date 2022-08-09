from datetime import datetime


def writeJournalEntry(mood):
    today = datetime.now()
    date = today.strftime("%m/%d/%Y %H:%M:%S")
    #print("date =", date)
    file = open("log.txt", "a")
    file.write("\n" + date + " " + mood)
    file.close()

def getJournalEntry(date):
    idx = 0
    entries = []
    file = open("log.txt", "r")
    lines = file.readlines()
    for line in lines:
        if date in line:
            print(line)
            entries.insert(idx, line)
            idx += 1
    file.close()
    return entries
