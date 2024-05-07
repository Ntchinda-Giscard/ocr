import json

def read_file_and_stack_sentences(file_path):
    sentences = []
    with open(file_path, 'r') as file:
        text = file.read()
        # Split the text into sentences based on new line characters
        sentences = [sentence.strip() for sentence in text.split('\n') if sentence.strip()]
    return sentences


def find_sub_sentence_indices(original_sentence, sub_sentence):

    if sub_sentence not in original_sentence:
        return -1, -1
    
    start_index = original_sentence.find(sub_sentence)
    end_index = start_index + len(sub_sentence)

    return start_index, end_index

def remove_none_values(data):
    cleaned_data = []
    for item in data:
        text, annotations = item
        cleaned_annotations = [anno for anno in annotations if anno is not None]
        cleaned_data.append((text, cleaned_annotations))
    return cleaned_data
def filter(s, data):
    if s > 0:
        return data
    else:
        pass


def find_in_all(tag_list, sentence):

    for tag in tag_list:
        if tag in sentence:
            start, end = find_sub_sentence_indices(sentence, tag)
            break
        else:
            start, end = -1, -1
    return start, end
# Example usage:
front_cni_file_path = 'FRONT_CNI_DATA.txt'  # Replace 'example.txt' with the path to your text file
f_names_file_path = 'fnames.txt'
l_names_file_path = 'lnames.txt'
serial_file_path = 'serial.txt'
dob_file_path = 'DOB.txt'
sentences = read_file_and_stack_sentences(front_cni_file_path)
fnames = read_file_and_stack_sentences(f_names_file_path)
lnames = read_file_and_stack_sentences(l_names_file_path)
serial = read_file_and_stack_sentences(serial_file_path)
dob = read_file_and_stack_sentences(dob_file_path)
print(len(sentences))
print(len(fnames))
print(len(lnames))

training_data = []
for i in range(len(sentences)):
    sentence = sentences[i]
    s1, e1 = find_in_all(fnames, sentence)
    s2, e2 = find_in_all(lnames, sentence)
    s3, e3 = find_in_all(serial, sentence)
    s4, e4 = find_in_all(dob, sentence)
    training_data.append((sentence, [
       filter( s1, (s1, e1 , 'fnames'))
        ,filter(s2, (s2, e2, "lnames")) , filter(s3, (s3, e3, "serial")) , filter(s4, (s4, e4, "DOB")) ]))

training_data = remove_none_values(training_data)


print(training_data)

# import secrets

# # Generate a random API key
# api_key = secrets.token_urlsafe(32)
# print(api_key)