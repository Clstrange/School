def pancake_sorting_on_strings(string):
    head_found = False
    target = sortString(string)
    # convert string into a list
    # string = convert(string)

    for char in target:
        # location to move the next character to
        index = target.index(char)

        # finding index of next character to move
        if string[index] == char:
            continue
        for i in range(index,len(string)):
            if string[i] == char:
                char_index = i
                break
        
        # flip the string at the target index
        string = flipString(string, char_index)
        if head_found == False:
            head_found = True
            continue
        else:
            head_location = char_index
        target_index = head_location - index
        string = flipString(string, target_index)
        string = flipString(string, head_location)
    return string

def convert(string):
    list1 = []
    list1[:0] = string
    return list1

def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1

def sortString(string):
    string = convert(string)
    string.sort()
    string = listToString(string)
    return string

def flipString(string, index):
    sub1 = string[index::-1]
    sub2 = string[index+1:]
    new_string = sub1 +sub2
    return new_string

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

print(pancake_sorting_on_strings(""))

string = "zabdcb"

print(find_nth(string, 'b', 2))

