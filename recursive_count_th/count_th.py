'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
globalcount = 0
def count_th(word):
    if word == "":
        return globalcount

    if word[-2:] == "th":
        globalcount + 1
