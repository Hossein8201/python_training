def words_check(text):
    good_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer_dict = {}
    text = text.split()
    for word in text:
        number = len(word)
        good_word = ''
        for letter in range(number):
            if(word[letter] in good_letters):
                good_word += word[letter]
        if(len(good_word) > number/2):
            good_word = good_word.title()
            if(good_word in answer_dict.keys()):
                answer_dict[good_word] += 1
            else:
                answer_dict.update({good_word : 1})
    answer_dict = {val[0] : val[1] for val in sorted(answer_dict.items(), key = lambda x: (-x[1], x[0]))}
    return answer_dict

                 

