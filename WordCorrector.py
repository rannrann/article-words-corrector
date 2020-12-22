import re
from collections import Counter


class TireNode():
    def __init__(self,layer):
        self.next=[None]*26
        self.layer=layer # used in load_one_word function
        self.lines=[]


class TireTree():
    words=[] #all words in TireTree
    word=[] #letter
    def __init__(self):
        self.root=TireNode(0)


    def extract_words(list):
        rlist=[]
        for line in list:
            matchobj = re.findall(r'([a-zA-Z][a-zA-Z]+[\sa-z\s]*).*\((.*)\)', str(line).lower())
            if(matchobj):
                tmp = ''
                for group in matchobj[0]:
                    tmp += group
                matchobj = [tmp]

                matchobj= [i.strip() for i in matchobj]
                #print(matchobj)
                row = re.findall(r'[0-9]*$', matchobj[0])
                row = row[0]
                matchobj.append(row)
                matchobj[0]=matchobj[0].replace(row,'')
                rlist.append(matchobj)
        return rlist

    def add(self,list):
        lines = TireTree.extract_words(list)
        for line in lines:
            for word in line[0].split():
                step = self.root
                current_layer=0
                for letter in word:
                    index = ord(letter) - ord('a')
                    current_layer+=1
                    if step.next[index] == None:
                        step.next[index]=TireNode(current_layer)
                    step = step.next[index]
                step.lines.append(line[1])

    def load_one_word(self,start):
        if start.lines:
            TireTree.words.append(''.join(TireTree.word))
        #the loop needs to be optimized
        for i in range(0,len(start.next)):
            if start.next[i]:# if there is any letter after the 'start' letter
                break
            if i==len(start.next)-1: #there is no letter after the 'start' letter
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

    def get_lines(self,word):
        step=self.root
        for letter in word:
            index = ord(letter) - ord('a')
            step=step.next[index]
        return step.lines

    def rectify(self,rectified_word,original_text):
        if len(rectified_word)==0:
            return None
        else:
            word_location={}
            for wrong_word,correct_word in rectified_word.items():
                word_location[wrong_word]=[int(i) for i in self.get_lines(wrong_word)]
            # print(word_location)
            #有没有考虑过同一错误单词在同一行出现多次这种情况
            for wrong_word,location in word_location.items():
                for time in location:
                    original_text[time]=original_text[time].replace(wrong_word,rectified_word[wrong_word])
            for i in range(0,len(original_text)):# 注意：使用for i in original_text是不行的
                temp = re.findall(r'\(.*\)',original_text[i])
                original_text[i] = original_text[i].replace(temp[0],'')
            return original_text

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
        return ( WordCorrector.known([word]) or WordCorrector.known(WordCorrector.edits1(word)) or WordCorrector.known(WordCorrector.edits2(word)) or [word])

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
