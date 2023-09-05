
def production(string):
    A = "+BF-AFA-FB+"
    B = "-AF+BFB+FA-"
    new_string = ""
    for character in string:
        if character == "A":
            new_string += A
        elif character == "B":
            new_string += B
        else:
            new_string += character
    return new_string

def main():
    iterations = int(input("how many iterations would you like: "))
    string = "A"
    for i in range(iterations):
        string = production(string)
    print(string)    
if __name__ == "__main__":
    main()