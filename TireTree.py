import re



class TireNode():
    def __init__(self,layer):
        self.isWord=False
        self.isRectify=False
        self.next=[None]*26
        self.layer=0


class TireTree():
    words=[]
    def __init__(self):
        self.root=TireNode(0)


    def extract_words(list):
        rlist=[]
        for line in list:
            matchobj = re.findall(r'[a-zA-Z][a-zA-Z]+ ', str(line).lower())
            if(matchobj):
                matchobj= [word.strip() for word in matchobj]
                rlist.append(matchobj)
        return rlist

    def add(self,list):
        lines = TireTree.extract_words(list)
        for line in lines:
            for word in line:
                step = self.root
                current_layer=0
                for letter in word:
                    index = ord(letter) - ord('a')
                    current_layer+=1
                    if step.next[index] == None:
                        step.next[index]=TireNode(current_layer)
                    step = step.next[index]
                step.isWord=True

    def load_one_word(self,start,word):
        if start.isWord == True:
            TireTree.words.append(''.join(word))


        for i in range(0,26):
            if start.next[i] != None:
                if len(word)!=start.layer:
                    word=[word[i] for i in range(0,start.layer)]
                word.append(chr(97+i))
                TireTree.load_one_word(self,start.next[i],word)





    def load_words(self):
        word=[]
        return TireTree.load_one_word(self,self.root,word)


