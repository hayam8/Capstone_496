
class Parser:

    def __init__(self, fileName, validKeystrokes):
        self._output = fileName
        #self._parsed = open('parsedInput', 'w+')
        self._keystrokes = validKeystrokes
        self._parsedList = []

    def getParsedList(self):
        return self._parsedList

    def parse(self):
        index = 0
        with open(self._output, 'r') as f:
            for keys in f:
                # remove any trailing characters, such as '\n'
                keys = keys.strip()
                # for key in line:
                if(keys in self._keystrokes):
                    self._parsedList.append(keys)

"""
file = 'user_output.txt'
validList = ['Win S', 'Ctrl V', 'Ctrl A']
test = Parser(file, validList)
test.parse()
print(test.getParsedList())
"""