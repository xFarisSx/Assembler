import re
class Parser:
    def __init__(self):
        self.lines = []
        self.parsedLines = []
        self.curLine=None
        self.curI=0
        self.curType=None
        self.lineCount=0
        self.curLineCount=0

    def parseFile(self, file):
        with open(file, 'r') as file:
            self.lines = [line.strip() for line in file.readlines() if line.strip() != '']
            
            print(self.lines)

            for line in self.lines:
                parsed = self.parseLine(line)
                self.parsedLines.append(parsed)
            print(self.parsedLines)
            self.curLine = self.parsedLines[self.curI]
            self.curType=self.curLine[0]

    def next(self):
        if self.curI >= len(self.parsedLines)-1:
            return True 
        self.curI+=1
        self.curLine=self.parsedLines[self.curI]
        self.curType=self.curLine[0]
        if self.curType !="L":
            self.curLineCount+=1

    def parseLine(self, line):
        self.lineCount+=1
        if line.startswith("@"):
            return ["A", line[0], line[1:]]
        elif line.startswith("("):
            self.lineCount-=1
            return ["L", line[1:-1], len(self.parsedLines)]

        else:
            newLine = ["C", "D", "C", "J"]
            istherec = line.find("=")   
            istherej = line.find("J")
            newLine= re.split(r'[=;]', line)
            newLine.insert(0, "C")
            if istherec==-1:
                newLine.insert(1, None)
            if istherej==-1:
                newLine.append(None)
            print(newLine)
            
            return newLine

    def value(self):
        return self.curLine[2]

    def label(self):
        return self.curLine[1]

    def dest(self):
        return self.curLine[1]
    def comp(self):
        return self.curLine[2]
    def jmp(self):
        return self.curLine[3]