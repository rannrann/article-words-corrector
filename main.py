from WordCorrector import TireTree,WordCorrector


def corrector(words):
    if not WordCorrector.generate_words_counter():
        print("The words counter can't be generated.")
        return
    else:
        wc = WordCorrector(words)
        return wc.correction()

def extract_sentence():
    list = [] #every line
    with open('text', 'r') as f:
        for line in f.readlines():
            list.append(line)

    for i in range(0,len(list)):
        head,mid,tail = list[i].partition('\n')
        list[i]=head+'('+str(i)+')'+mid
    print(list)
    return list

def main():
    root=TireTree()
    list = extract_sentence()
    root.add(list)
    original_words=root.load_words()
    rectified_words = corrector(original_words) # dict
    #print(rectified_words)
    rectified_list = root.rectify(rectified_words,list)
    if rectified_list:
        print(rectified_list)
    else:
        pass



if __name__ == "__main__":
    main()

