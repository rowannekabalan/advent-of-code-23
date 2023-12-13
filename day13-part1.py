all_notes = dict()

def parse_input():
    i = 0
    with open('input.txt', 'r') as file:
        data = file.read()
        notes = data.strip().split('\n\n')
        for note in notes:
            all_notes[i] = note.split('\n')
            i += 1
    return all_notes

def find_mirror(note):
    mirror = find_mirror_horizontal(note)
    if mirror:
        return mirror * 100
    else:
        transposed = list(map(''.join, zip(*note)))
        return find_mirror_horizontal(transposed)

def find_mirror_horizontal(note):
    mirror = 0
    for i in range(0, len(note)-1):
        next = i + 1
        pre = note[:next]
        post = note[next:]
        if pre == list(reversed(note[next:next + len(pre)])) or post == list(reversed(note[next-len(post):next])):
            mirror = next
    return mirror
  
def sum_all():
    return sum(find_mirror(all_notes[note]) for note in all_notes)






