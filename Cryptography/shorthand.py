import sys
import random
import string

from rewriting import ReWriter

symbols = list(string.printable)

def sum_str(symbols:list):
    output_string = str()

    for i in symbols:
        output_string += i

    return output_string    

def encrypt(text:str):

    text = text.lower()

    output_string = str()

    words = [word.strip(string.punctuation) for word in text.split()]

    for i in range(len(words)):
        output_string += sum_str([symbols[random.randint(0, 99)] for k in range(4)])
        output_string += words[i]
        output_string += sum_str([symbols[random.randint(0, 99)] for k in range(4)])

    return output_string

input_file = sys.argv[1]

rewriter = ReWriter(encrypt)
rewriter.write_to_file(input_file, 'output_steganography_file.txt') 