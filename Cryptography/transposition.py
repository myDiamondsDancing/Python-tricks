import sys

from rewriting import ReWriter

def sum_str(symbols:list):
    output_string = str()

    for i in symbols:
        output_string += i

    return output_string    

def encrypt(text:str):
    text = list(text)

    i = 0

    while True:
        try:
            text[i], text[i + 1], text[i + 2] = text[i + 2], text[i + 1], text[i]
        except IndexError:
            break

        i += 3

    return sum_str(text)

input_file = sys.argv[1]

rewriter = ReWriter(encrypt)
rewriter.write_to_file(input_file, 'output_transposition_file.txt') 