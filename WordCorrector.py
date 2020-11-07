import re
from collections import Counter


class TireNode():
    def __init__(self,layer):
        self.isWord=False
        self.isRectify=False
        self.next=[None]*26
        self.layer=layer


class TireTree():
    words=[]
    word=[]
    def __init__(self):
        self.root=TireNode(0)


    def extract_words(list):
        rlist=[]
        for line in list:
            matchobj = re.findall(r'[a-zA-Z][a-zA-Z]+[\sa-z\s]*', str(line).lower())
            if(matchobj):
                matchobj= [i.strip() for i in matchobj]
                rlist.append(matchobj)

        for i in range(0,len(rlist)):
            rlist[i]=rlist[i][0].split()
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

    def load_one_word(self,start):
        if start.isWord == True:
            TireTree.words.append(''.join(TireTree.word))
            TireTree.word = [TireTree.word[i] for i in range(0, start.layer)]


        for i in range(0,26):
            if start.next[i] != None:
                if start.layer<len(TireTree.word):
                    TireTree.word=[]
                TireTree.word.append(chr(97+i))
                TireTree.load_one_word(self,start.next[i])

    def load_words(self):
        TireTree.load_one_word(self,self.root)
        return TireTree.words


class WordCorrector:
    def __init__(self,words,dir):
        self.original_words=words
        self.dir = dir
        self.text = open(dir).read()
        self.words_counter=None
    def generate_words_counter(self):
        self.words_counter=Counter(re.findall(r'\w+',self.text.lower()))
        if self.words_counter:
            return True
        else:
            return False
    def known(self,word):
        return set(w for w in word if w in self.words_counter)

    def edits1(self,word):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        inserts = [L + c + R for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def edits2(self,word):
        return (e2 for e1 in WordCorrector.edits1(word) for e2 in WordCorrector.edits1(e1))

    def candidates(word):
        return (WordCorrector.known([word]) or WordCorrector.known(WordCorrector.edits1(word)) or WordCorrector.known(WordCorrector.edits2(word)) or [word])

    def P(self,word):
        N = sum(self.words_counter.values())
        return self.words_counter[word] / N

    def correction(self):
        if WordCorrector.generate_words_counter(self):
            ret={}
            for word in self.original_words:
                new_word=max(WordCorrector.candidates(word), key=WordCorrector.P)
                if new_word != word:
                    ret[word]=new_word
            return ret
        else:
            return "The words counter can't be generated."