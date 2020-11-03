import re



class TireNode():
    def __init__(self):
        self.isWord=False
        self.isRectify=False
        self.next=[None]*26
        self.count=0


class TireTree():
    def __init__(self):
        self.root=TireNode()


    def extract_words(list):
        rlist=[]
        for line in list:
            matchobj = re.findall(r'[a-zA-Z][a-zA-Z]+ ', str(line).lower())
            print(matchobj)
            if(matchobj):
                rlist.append(matchobj)
        return rlist

    def add(self,list):
        lines = TireTree.extract_words(list)
        for line in lines:
            for word in line:
                step = self.root
                for letter in word:
                    index = ord(letter) - ord('a')
                    if step.next[index] != None:
                        step.next[index]=TireNode()
                    step = step.next[index]
                step.isWord=True


