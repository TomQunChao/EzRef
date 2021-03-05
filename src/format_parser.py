
import sys

def error(s):
    sys.stderr.write(s+"\n")
class RefReader:

    pass
class EzRefFormater:
    format = ""
    def __init__(self,format:list):
        self.format=format
    def format(data):

        pass
    def __str__(self):
        return str(self.format)
class EzRefFormat:
    name=""
    formaters = {}
    def addFormat(self,format:str):
        l = len(format)
        typ = ""
        fmt = [] # 使用list存储format
        cnt = 0
        # skip blank space
        while cnt<l and format[cnt]==' ':cnt+=1
        # get type
        if cnt<l and format[cnt]=='[':
            cnt+=1
            while format[cnt]!=']':
                typ+=format[cnt]
                cnt+=1
        cnt+=1 # skip ]
        while cnt<l and format[cnt]==' ':cnt+=1
        while cnt<l:
            if format[cnt]=='{':
                cnt+=1
                itemName = '{'
                while cnt<l and format[cnt]!='}':
                    itemName+=format[cnt]
                    cnt+=1
                itemName+='}'
                fmt.append(itemName)
                cnt+=1
                symb = ''
                while cnt<l and format[cnt]!='{':
                    symb+=format[cnt]
                    cnt+=1
                fmt.append(symb)
                cnt-=1
            cnt+=1
        self.formaters[typ]=EzRefFormater(fmt)
    '''
    @param format: 一行一个格式
    '''
    def parseFormat(self,format:str):
        lines = format.split('\n',-1)
        for line in lines:
            if line:
                self.addFormat(line)
    '''
    @param format:带有名称的格式
    '''
    def parseFormatName(self,format:str):
        cnt = 0
        l = len(format)
        while cnt<l and format[cnt]==' ' or format [cnt]=='\n':cnt+=1
        if format[cnt]=='-':
            self.name=''
            cnt+=1
            while cnt<l and format[cnt]!='\n':
                self.name+=format[cnt]
                cnt+=1
            cnt+=1
        return self.name,format[cnt:]
    def __init__(self,format,parseName=False,name=""):
        if not parseName and not name:
            error("no name")
            exit(-1)
        if parseName:
            self.name,format=self.parseFormatName(format)
        else:self.name=name
        self.parseFormat(format)
    def setName(self,name):
        self.name=name
    '''
    将参考文献按自己的格式输出
    '''
    def formatOne(self,refData:dict,type):

        pass
    def formatAll(self,refData:list,type:list):
        res = []
        for i in refData:
            res.append(self.formatOne(i))
        return res
    def __str__(self):
        return str(self.formaters)
def preProcess(s:str):

    return s
def parseAll(s:str):
    s = preProcess(s)
    fmts = {}
    fmtsstr = s.split('--\n')
    for fmtstr in fmtsstr:
        fmt = EzRefFormat(fmtstr,True)
        fmts[fmt.name]=fmt
    return fmts

'''
@param data: 要转化的参考文献，应该是一个字典列表
@param format: 格式要求，如果长度为1,则都采用同一个格式
'''
def formatAll(data,format:list):
    res = []
    if len(format)==1:
        for i in data:
            res.append()
if __name__=='__main__':
    with open('format.txt','r') as f:
        fmts = parseAll(f.read())
        print(fmts)
        for i in fmts.keys():
            print(fmts[i])
            for j in fmts[i].parsers.keys():
                print(j,fmts[i].parsers[j])