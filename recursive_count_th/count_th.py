'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# O(n)
def count_th(word):
    count = 0
    def count_substring_occurences(string):
        if "th" in string:
            nonlocal count
            count += 1
            newStr = string.replace("th", "00", 1)
            count_substring_occurences(newStr)
    
    count_substring_occurences(word)
    return count
