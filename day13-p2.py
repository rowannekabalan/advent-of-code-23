all_notes = dict()

def parse_input():
    with open('input.txt', 'r') as file:
        data = file.read()
        return [note.split('\n') for note in data.strip().split('\n\n')]
    
def diff_lists(list1, list2):
    diff = []
    for i, val in enumerate(list1):
        if list1[i] != list2[i]:
            diff.append(list1[i])
            diff.append(list2[i])
    return diff


def new_mirrors(note):
    transposed = list(map(''.join, zip(*note)))
    return sum(find_smudged_mirrors(transposed)) + sum(find_smudged_mirrors(note) * 100)


def find_smudged_mirrors(note):
    mirrors = []
    for i in range(0, len(note) - 1):
        if is_smudged_mirror(i + 1, note):
            mirrors.append(i + 1)
    return mirrors


def is_smudged_mirror(next, note):
    pre = note[:next]
    post = note[next:]
    pre_mirrored = list(reversed(note[next:next + len(pre)]))
    post_mirrored = list(reversed(note[next - len(post):next]))

    def off_by_one(reflection):
        if len(reflection) == 2:
            char_diff = diff_lists(reflection[0], reflection[1])
            if len(char_diff) == 2 and '.' in char_diff and '#' in char_diff:
                return True

    def process_mirror_lists(original, mirrored):
        if len(original) == len(mirrored):
            broken_reflection = diff_lists(original, mirrored)
            return off_by_one(broken_reflection)

    return process_mirror_lists(pre, pre_mirrored) or process_mirror_lists(post, post_mirrored)


def sum_all_smudged():
    return sum(new_mirrors(all_notes[note]) for note in all_notes)

