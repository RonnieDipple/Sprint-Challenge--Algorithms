'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
#This is actuall the hardest to understans
def count_th(word):
    count = 0 #Counts the amount of times th appears
    def th_counter(word, i):
        if i > 0: #if i is above 0 so not at the end of a backwards count
            #to_match equals i 2 back from i basically it is going back every 2 letters
            to_match = word[i-2:i]
            print(to_match) #Just a print statement
            if to_match == "th": #if to_match equals "th"
                #then it uses nonlocal which is similar to global to increase the count by 1
                nonlocal count
                count += 1
            th_counter(word, i-1) #recursion as it is calling itself with i set back one space

    th_counter(word, len(word))#recursion again as it calls itelf and inputs the word and in this case len(word)
    #is the iterator above
    return count #returns the count
