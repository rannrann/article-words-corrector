from WordCorrector import TireTree,WordCorrector


def corrector(words):
    wc = WordCorrector(words,'big.txt')
    return wc.correction()

def extract_sentence():
    list = []
    with open('text', 'r') as f:
        for line in f.readlines():
            list.append(line)
    return list

def main():
    root=TireTree()
    list = extract_sentence()
    root.add(list)
    original_words=root.load_words()
    print(original_words)
    print(len(original_words))
    #print(corrector(original_words))



if __name__ == "__main__":
    main()

