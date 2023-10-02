import re

def extract_numbers(sentence):
    pattern = r'\d+'
    numbers = re.findall(pattern, sentence)
    return numbers

sen1 = "I am a 44computer 32scientist"
sen2 = "The life 454 i chose it 2335 what i like7652"

print(extract_numbers(sen1))
print(extract_numbers(sen2))
