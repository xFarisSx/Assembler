from parser import Parser
from code import Code

class Main:
    def __init__(self):
        self.inputFile=input("Enter Your File Name In example.asm Form Please: ")
        self.parser = Parser() 
        self.code = Code() 
        self.filename = self.inputFile[0:-3]+'hack'
    
        

    def run(self):
        finish=False
        lastVC = 16
        self.parser.parseFile(self.inputFile)
        for line in self.parser.parsedLines:
            if line[0] == "L":
                self.code.addL(line[1], line[2]-self.code.addedL)
        for line in self.parser.parsedLines:
            if line[0] == "A" and not line[2][0].isdigit() and not line[2] in self.code.symbols.keys():
                self.code.addV(line[2], lastVC)
                lastVC+=1
        with open(self.filename, 'w') as file:
            file.write("")
            while not finish:

                if self.parser.curType == "C":
                    c=self.parser.comp()
                    d=self.parser.dest()
                    j=self.parser.jmp()

                    cc=self.code.comp(c)
                    dd=self.code.dest(d)
                    jj=self.code.jmp(j)

                    file.write("111"+cc+dd+jj + '\n')
                elif self.parser.curType == "A":
                    val=self.parser.value()
                    vv=self.code.value(val)
                    file.write(vv + '\n')
                
                isfin=self.parser.next()
                if isfin:
                    finish=True

                


            print(f"Lines appended to {self.filename}.")




if "__main__" in __name__:
    main = Main()
    main.run()