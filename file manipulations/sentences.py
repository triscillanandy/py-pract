import re

def remove_num(sentence):
  pattern = r'\d+'
  new_sentence = re.sub(pattern, repl="", string=sentence)
  
  return new_sentence


sen1 = "I am a 44computer 32scientist"
sen2 = "The life 454 i chose its 2335 what i like7652"

print(remove_num(sen1))
print(remove_num(sen2))
