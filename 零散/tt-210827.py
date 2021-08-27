from typing import List


def can_jump_to_end(l: List):
    longest_index = 0
    for i in l:
        if l.index(i) > longest_index:
            return False
        if l.index(i)+i > longest_index:
            longest_index = l.index(i)+i
    return True


if __name__ == "__main__":
    can_jump_to_end([3, 2, 1, 0, 4])
