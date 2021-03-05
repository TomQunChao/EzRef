
import sys

def error(s):
    sys.stderr.write(s+"\n")

class EzRefParser:
    format = ""
    pass
class EzRefFormat:
    name=""
    parsers = {}
    def addFormat(self,format:str):
        l = len(format)
        typ = ""
        
        pass
    '''
    @param format: 一行一个格式
    '''
    def parseFormat(self,format:str):
        lines = format.split('\n',-1)
        
        for line in lines:
            self.addFormat(line)
    def __init__(self,format):
        self.parseFormat(format)
    def parse(self,s):
        if len(self.parsers)==0:
            error("There is no parser(s),did you read format?")
        

def readData(file):

    pass