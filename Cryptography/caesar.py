import sys
import string

from rewriting import ReWriter

symbols = list(string.printable)

def activation(input_:int, intercept:int):
    return (input_ + intercept) % 100

def encrypt(text:str):

    intercept = 5

    output_string = str()

    for i in text:
        input_ = symbols.index(i)
        output = activation(input_, intercept)
        output_string += symbols[output]

    return output_string 

input_file = sys.argv[1]

rewriter = ReWriter(encrypt)
rewriter.write_to_file(input_file, 'output_caesar_file.txt')  
