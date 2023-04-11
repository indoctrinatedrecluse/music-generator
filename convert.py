import random
from music21 import converter

candidates = []
candidates += [chr(letter) for letter in range(ord('a'), ord('g')+1)]
candidates += [chr(letter) for letter in range(ord('A'), ord('G')+1)]

def process(letter):
    # generate random 3-shingle using the letter as seed
    random.seed(ord(letter))
    return random.choice(candidates)+random.choice(candidates)+random.choice(candidates)

def generate():
    with open('input.txt') as file:
        data = file.read().replace('\n', ' ').rstrip().replace(' ', '')
        file.close()
        
    notes = []
    for letter in data:
        notes.append(process(letter))
    
    suc_count, line_count, flag = 0, 0, 0
    output = ''
    for shingle in notes:
        if (flag % 2 == 0):
            output += (shingle + ' ')
            suc_count += 1
            line_count += 1
            if (suc_count == 2 and line_count < 8):
                output += ('| ')
                suc_count = 0
            elif (suc_count == 2 and line_count == 8):
                output += ('|\n')
                suc_count = 0
                line_count = 0
                flag += 1
            elif line_count == 8:
                output += ('|\n')
                suc_count = 0
                line_count = 0
                flag += 1
        else:
            output += (shingle + ' ')
            suc_count += 1
            line_count += 1
            if (suc_count == 2 and line_count < 6):
                output += ('| ')
                suc_count = 0
            elif (suc_count == 2 and line_count == 6):
                output += ('|1 ')
                suc_count = 0
            elif (suc_count == 2 and line_count == 8):
                output += (':|2 ')
                suc_count = 0
            elif (suc_count == 2 and line_count == 10):
                output += ('|:\n')
                suc_count = 0
                line_count = 0
                flag += 1
            elif (line_count == 10):
                output += ('|:\n')
                suc_count = 0
                line_count = 0
                flag += 1
    
    temp = list(output)
    
    if (temp[-1] == ':'):
        temp[-1] = ']'
    elif (temp[-1] == '\n' and temp[-2] == ':'):
        temp = temp[:-1]
        temp[-1] = ']'
    else:
        temp.append(']')
        
    output = ''.join(temp)
    
    return output
    
def print_file(data):
    output = ''
    #output += '<score lang="ABC">\n'
    output += 'X:1\n'
    output += 'T:Random Noise\n'
    output += 'M:6/8\n'
    output += 'L:1/8\n'
    output += 'R:jig\n'
    output += ('K:' + random.choice([chr(letter) for letter in range(ord('A'), ord('G')+1)]) + '\n')
    output += data
    #output += '\n</score>'
    
    with open('output.abc', 'w') as file:
        file.write(output)
        file.close()
        
    pass
    
def convert_to_midi():
    midi = converter.parse('output.abc')
    midi.write('midi', fp='output.mid')
    # midi.show('midi')
    pass

if __name__ == "__main__":
    print_file(generate())
    convert_to_midi()