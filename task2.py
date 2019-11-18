input_words = input()
word_list = input_words.split(' ')
sorted_list = sorted(word_list, key = len)
print(' '.join(sorted_list))
# sorte
# for i in range(len(word_list)):
#     for j in range(len(word_list)):
#         if word_list[i] < word_list[j]:

    

# print(' '.join(input_words.split(' ')))
