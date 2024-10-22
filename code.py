class Code:
    def __init__(self):
        self.comps={
            '0':'101010',
            '1':'111111',
            '-1':'111010',
            'D':'001100',
            'A':'110000',
            '!D':'001101',
            '!A':'110001',
            '-D':'001111',
            '-A':'110011',
            'D+1':'011111',
            'A+1':'110111',
            'D-1':'001110',
            'A-1':'110010',
            'D+A':'000010',
            'D-A':'010011',
            'A-D':'000111',
            'D&A':'000000',
            'D|A':'010101'
        }
        self.jmps={
            None:"000",
            "JGT":"001",
            "JEQ":"010",
            "JGE":"011",
            "JLT":"100",
            "JNE":"101",
            "JLE":"110",
            "JMP":"111",
        }
        self.dests={
            None:"000",
            "M":"001",
            "D":"010",
            "MD":"011",
            "A":"100",
            "AM":"101",
            "AD":"110",
            "AMD":"111",
        }
        self.symbols={
            "SCREEN":16384,
            "KBD":24576,
            "SP":0,
            "LCL":1,
            "ARG":2,
            "THIS":3,
            "THAT":4,
        }
        for i in range(16):
            self.symbols["R"+str(i)]=i
        
        self.addedL=0
        self.addedV=0
    def addL(self, l, v):
        self.symbols[l]=v
        self.addedL+=1
    def addV(self, l, v):
        self.symbols[l]=v
        self.addedV+=1

    def value(self,v):
        if not v.isdigit():
            print(v, self.symbols[v])
        if v.isdigit():
            vv = format(int(v), '016b')
        else:
            vv=format(int(self.symbols[v]), '016b')
        return vv

    def dest(self,d):
        return self.dests[d]
    def comp(self, c):
        a= "M" in c 
        c=c.replace("M", "A")
        cc=self.comps[c]
        return str(int(a))+cc
    def jmp(self, j):
        return self.jmps[j]