class ReWriter(object):
    def __init__(self, encrypt_function=lambda x: x):
        self.encrypt_function = encrypt_function

    def write_to_file(self, input_file, output_file):

        file_text = str()

        with open(input_file, 'r') as f:
            for line in f.readlines():
                file_text += line

        output_text = self.encrypt_function(file_text)

        with open(output_file, 'w') as f:
            f.write(output_text)  


