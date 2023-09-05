"""
    Please implement functions named:  reset, basicOps, geneSeqDP, timeComplexity, spaceComplexity; details follow.

    You don't have to, but you might want to, add a main function and code/test this in your
    favorite Python IDE.
"""

count = 0

""" reset, resets basic op counter to 0 """
def reset():
    global count
    count = 0

""" basicOps returns the number of basic operations """
def basicOps():
    return count


""" 
    geneSeqDP, implement Genetic Sequence Alignment algorithm Dynamic Programming Solution.
    Please do implement it using CS3310Lect9a_GeneSequencing_DP.pdf, which can be found at
        https://uvu.instructure.com/files/107764916/download?download_frd=1
    
    
"""
def geneSeqDP(s1, s2):
    # m is length of string 1, i is offset into m (the row #)
    # n is length of string 2, j is offest into n (the column #)
    # allocate and zero-full an array s of size (m + 1) x (n + 1) // +1 to initialize first rows and columns indel values
    #
    #
    # use Needleman/Wunsch constants:
    #    penalty for match is -3
    #    penalty for subst is 1
    #    penalty for indel is 5
    #
    # 
    # initialize rows
    # for i in 1...m+1:  S[i][0] = i*indel
    #
    # initialize columns
    # for j in 1...n+1:  S[0][j] = j*indel
    #
    #
    # calculate the best alignment
    # for i in 1..m+1:
    #         for j in 1..n+1:
    #                 dist = s1[i-1] == s2[j-1] ? match : subst // -1 since i and j are one-based
    #                 Score of (i,j)th characters is the minimum of: // remember the first row and column are initialized to indel
    #                         S[i-1][j-1] + dist // -1 since checking the previous cells value diaganolly + distance
    #                         S[i-1][j] + indel // moving to next j but previous i (insertion in s
    #                         S[i][j-1] + indel // moving to next i but previous j
    #
    # return s[m][n]

    m = len(s1)
    n = len(s2)
    match = -3
    subst = 1
    indel = 5

    s = []
    #creating the matrix
    for i in range(m+1):
        s.append([])
        for y in range(n+1):
            s[i].append(0)
    

    for i in range(1, m+1):
        s[i][0] = i * indel
        

    for j in range(1, n+1):
        s[0][j] = j * indel

    s[i][0] = i*indel
    for j in range( 1,n + 1):
        s[0][j]= j*indel
    for i in range(1, m+1):
        for j in range(1,n+1):
            if s1[i - 1]== s2[j - 1]:
                dist = match
            else:
                dist = subst
            s[i][j] = min(s[i-1][j-1]+ dist,s[i-1][j] + indel ,s[i][j-1]+ indel)
    return s[m][n]