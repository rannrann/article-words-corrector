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
    #print(list)
    return list

def main():
    root=TireTree()
    list = extract_sentence()
    root.add(list)
    original_words=root.load_words()
    rectified_words = corrector(original_words) # dict
    rectified_list = root.rectify(rectified_words,list)
    if rectified_list:
        with open('rectified_text', 'w') as f:
            for line in rectified_list:
                f.write(line)
    else:
        print("All of words in the essay are correct!")

    # 告诉用户
    for wrong_word, correct_word in rectified_words.items():
        print("单词：",wrong_word," 改为",correct_word)





if __name__ == "__main__":
    main()

