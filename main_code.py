import json
import difflib
from difflib import get_close_matches

class Dictionary:
    def __init__(self):
        self.data = json.load(open('data.json'))
    # print((data['man']))
    def translate(self):
        try:

            arg = input('Please enter a word to know its meaning: ')

            if(arg in self.data):
                for i in self.data[arg]:
                    print(i)
            else:
                new_arg = get_close_matches(arg.lower(), (self.data.keys()), n=1, cutoff=.8)[0]
                if (new_arg != arg):
                    decesion = input('Did you mean ' + str(new_arg) + ' ??, press Y for YES and N for NO !!')
                    if (decesion.upper() == 'N'):
                        new_arg = arg
                else:
                    print('SORRY !! no such word exists in dictionary, Please double check')
        except Exception as e:
            print('ERROR!!! ',e,type(e))


if __name__ == '__main__':
    dictionary = Dictionary()
    dictionary.translate()