from TireTree import TireTree,TireNode


def corrector():
    pass

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
    root.load_words()
    print(len(root.words))



if __name__ == "__main__":
    main()

