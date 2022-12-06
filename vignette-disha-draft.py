

import random
import gzip, json
all_lines = []
for line in open("poetry_poe.ndjson"):
    all_lines.append(json.loads(line.strip()))
print(len(all_lines))

print(random.sample(all_lines, 10))

import re
import markovify

# train model
poem = '\n'.join([line['s'] for line in random.sample(all_lines, 13455)])
model = markovify.NewlineText(poem)


flower_lines = [line['s'] for line in all_lines if re.search(r'\bflower\b', line['s'],re.I)]
print(len(flower_lines))

flower_big_poem = '\n'.join([line for line in random.sample(flower_lines, 20)])
print(flower_big_poem)

#generate poem 
for i in range(20):
    print(model.make_sentence())
    
