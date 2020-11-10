import re
from collections import Counter


class TireNode():
    def __init__(self,layer):
        self.isWord=False
        self.isRectify=False
        self.next=[None]*26
        self.layer=layer
        self.lines=[]


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
        for i in range(0,len(start.next)):
            if start.next[i]:
                break
            if i==len(start.next):
                return

        for i in range(0,26):
            if start.next[i] != None:
                if start.layer<len(TireTree.word):
                    TireTree.word = [TireTree.word[i] for i in range(0, start.layer)]
                TireTree.word.append(chr(97+i))
                TireTree.load_one_word(self,start.next[i])

    def load_words(self):
        TireTree.load_one_word(self,self.root)
        return TireTree.words


class WordCorrector:
    words_counter = None
    text = open('big.txt').read()
    def __init__(self,words):
        self.original_words=words

    @classmethod
    def generate_words_counter(cls):
        cls.words_counter=Counter(re.findall(r'\w+',cls.text.lower()))
        if cls.words_counter:
            return True
        else:
            return False

    def known(words):
        return set(w for w in words if w in WordCorrector.words_counter)

    def edits1(word):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        inserts = [L + c + R for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def edits2(word):
        return (e2 for e1 in WordCorrector.edits1(word) for e2 in WordCorrector.edits1(e1))

    def candidates(word):
        return ( WordCorrector.known([word]) or WordCorrector.edits1(word) or WordCorrector.edits2(word) or [word])

    @classmethod
    def P(cls,word):
        N = sum(cls.words_counter.values())
        return cls.words_counter[word] / N

    def correction(self):
        ret = {}
        for word in self.original_words:
            new_word = max(WordCorrector.candidates(word), key=WordCorrector.P)
            if new_word != word:
                ret[word] = new_word
        return ret
