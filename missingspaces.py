import os

from symspellpy.symspellpy import SymSpell  # import the module

def main():
    max_edit_distance_dictionary = 2
    prefix_length = 7
    # create object
    sym_spell = SymSpell(max_edit_distance_dictionary, prefix_length)
    
    if not sym_spell.create_dictionary('training_data.txt',encoding = "ISO-8859-1"):
        print("Corpus file not found")
        return
    dictlist=[]
    for key, count in sym_spell.words.items():
        print("{} {}\n".format(key, count))
        dictlist.append("{} {}\n".format(key, count))
        # save Dictionary 

    with open("dict.txt", "a+",encoding = "ISO-8859-1") as text_file:
         text_file.write(str(dictlist))
    print('Saved Dic')
     # load dictionary
    dictionary_path = os.path.join(os.path.dirname('./'),"dict.txt")
    print(dictionary_path)
    term_index = 0  # column of the term in the dictionary text file
    count_index = 1  # column of the term frequency in the dictionary text file
    if not sym_spell.load_dictionary(dictionary_path, term_index, count_index):
        print("Dictionary file not found")
        return
    # a sentence without any spaces
    data=''
    with open('missing_spaces.txt', 'r',encoding = "utf8") as myfile:
        data = myfile.read()
 
    splitline=data.split(',')
#        for line in splitline:
#            data.append(splitline[line])
    for indx in range(0,(len(splitline)-1)):
        try:
            strval=splitline[indx]
    #        print(strval)
            result = sym_spell.word_segmentation(strval,max_edit_distance_dictionary,prefix_length)
            # display suggestion term, term frequency, and edit distance
            print("{}".format(result.corrected_string))
        except :
             print('out of index')  


if __name__ == "__main__":
    main()