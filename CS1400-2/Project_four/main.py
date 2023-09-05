"""
Name: Cody Strange
Project: Library of Congress
date: 3/25/2022
Disclaimer: This is 100% my own original work
"""
import sys

alg = []
ttl = []
woo = []
fmp = []
pnp = []
tsl = []

def separate_text(text):
    #Group text lines by their three-letter code
    for line in text:
        line = line.strip()
        temp = line.split("|")
        identifier = temp[2]
        if identifier == "ALG":
            alg.append(temp)
        elif identifier == "TTL":
            ttl.append(temp)
        elif identifier == "WOO":
            woo.append(temp)
        else:
            print("error")

def separate_text_two(text):
    #Group text lines by their three-letter code
    for line in text:
        line = line.strip()
        temp = line.split("|")
        identifier = temp[2]
        if identifier == "FMP":
            fmp.append(temp)
        elif identifier == "PNP":
            pnp.append(temp)
        elif identifier == "TSL":
            tsl.append(temp)
        else:
            print("else")

def sort_line(text):
    return int(text[1])

def line_length(text):
    #Determine longest line of a text and corresponding line number
    largest_len = ""

    for line in text:
        if largest_len == "":
            largest_len = line
        elif len(line[0]) > len(largest_len[0]):
            largest_len = line
        elif len(line[0]) == len(largest_len[0]):
            if int(line[1]) > int(largest_len[1]):
                largest_len = line
    return largest_len

def line_length_short(text):
    #Determine shortest line of a text and corresponding line number
    shortest_len = ""
    for line in text:
        if shortest_len == "":
            shortest_len = line
        elif len(line[0]) < len(shortest_len[0]):
            shortest_len = line
        elif len(line[0]) == len(shortest_len[0]):
            if int(line[1]) < int(shortest_len[1]):
                shortest_len = line
    return shortest_len

def avg_length(text):
    #Determine the average length of the lines in the entire text
    values = []
    for line in text:
        values.append(int(len(line[0])))
    return round(sum(values)/len(values))

def main():

    #Read in text file
    with open(sys.argv[1], 'r') as txt_file:

        if sys.argv[1] == ".guides/secure/book_data.txt":
            #Group text lines by their three-letter code
            separate_text(txt_file.readlines())

            #Organize lines by line number
            alg.sort(key=sort_line)
            woo.sort(key=sort_line)
            ttl.sort(key=sort_line)

            #Determine longest line of a text and corresponding line number
            longest_line_alg = line_length(alg)
            longest_line_ttl = line_length(ttl)
            longest_line_woo = line_length(woo)

            #Determine shortest line of a text and corresponding line number
            shortest_line_alg = line_length_short(alg)
            shortest_line_ttl = line_length_short(ttl)
            shortest_line_woo = line_length_short(woo)

            #Determine the average length of the lines in the entire text
            avg_line_alg = avg_length(alg)
            avg_line_ttl = avg_length(ttl)
            avg_line_woo = avg_length(woo)

            #Write text into the file novel_text.txt
            with open("novel_text.txt", 'w') as novel_file:
                novel_file.write("ALG\n")
                for line in alg:
                    novel_file.write(line[0] + "\n")
                novel_file.write("-----\n")

                novel_file.write("TTL\n")
                for line in ttl:
                    novel_file.write(line[0] + "\n")
                novel_file.write("-----\n")

                novel_file.write("WOO\n")
                for line in woo:
                    novel_file.write(line[0] + "\n")

            #Write summary of the text data in the file novel_summary.txt
            with open("novel_summary.txt", 'w') as summary_file:
                summary_file.write("ALG\n")
                summary_file.write("Longest line " + "(" + str(longest_line_alg[1]) + "): " + longest_line_alg[0] + "\n")
                summary_file.write("Shortest line " + "(" + str(shortest_line_alg[1]) + "): " + shortest_line_alg[0] + "\n")
                summary_file.write("Average length: " + str(avg_line_alg) + "\n\n")

                summary_file.write("TTL\n")
                summary_file.write("Longest line " + "(" + str(longest_line_ttl[1]) + "): " + longest_line_ttl[0] + "\n")
                summary_file.write("Shortest line " + "(" + str(shortest_line_ttl[1]) + "): " + shortest_line_ttl[0] + "\n")
                summary_file.write("Average length: " + str(avg_line_ttl) + "\n\n")

                summary_file.write("WOO\n")
                summary_file.write("Longest line " + "(" + str(longest_line_woo[1]) + "): " + longest_line_woo[0] + "\n")
                summary_file.write("Shortest line " + "(" + str(shortest_line_woo[1]) + "): " + shortest_line_woo[0] + "\n")
                summary_file.write("Average length: " + str(avg_line_woo))

        elif sys.argv[1] == ".guides/secure/other.txt":

            #Group text lines by their three-letter code
            separate_text_two(txt_file.readlines())

            #Organize lines by line number
            fmp.sort(key=sort_line)
            pnp.sort(key=sort_line)
            tsl.sort(key=sort_line)

            #Determine longest line of a text and corresponding line number
            longest_line_fmp = line_length(fmp)
            longest_line_pnp = line_length(pnp)
            longest_line_tsl = line_length(tsl)

            #Determine shortest line of a text and corresponding line number
            shortest_line_fmp = line_length_short(fmp)
            shortest_line_pnp = line_length_short(pnp)
            shortest_line_tsl = line_length_short(tsl)

            #Determine the average length of the lines in the entire text
            avg_line_fmp = avg_length(fmp)
            avg_line_pnp = avg_length(pnp)
            avg_line_tsl = avg_length(tsl)

            #Write text into the file novel_text.txt
            with open("novel_text.txt", 'w') as novel_file:
                novel_file.write("FMP\n")
                for line in fmp:
                    novel_file.write(line[0] + "\n")
                novel_file.write("-----\n")

                novel_file.write("PNP\n")
                for line in pnp:
                    novel_file.write(line[0] + "\n")
                novel_file.write("-----\n")

                novel_file.write("TSL\n")
                for line in tsl:
                    novel_file.write(line[0] + "\n")

            #Write summary of the text data in the file novel_summary.txt
            with open("novel_summary.txt", 'w') as summary_file:
                summary_file.write("FMP\n")
                summary_file.write("Longest line " + "(" + str(longest_line_fmp[1]) + "): " + longest_line_fmp[0] + "\n")
                summary_file.write("Shortest line " + "(" + str(shortest_line_fmp[1]) + "): " + shortest_line_fmp[0] + "\n")
                summary_file.write("Average length: " + str(avg_line_fmp) + "\n\n")

                summary_file.write("PNP\n")
                summary_file.write("Longest line " + "(" + str(longest_line_pnp[1]) + "): " + longest_line_pnp[0] + "\n")
                summary_file.write("Shortest line " + "(" + str(shortest_line_pnp[1]) + "): " + shortest_line_pnp[0] + "\n")
                summary_file.write("Average length: " + str(avg_line_pnp) + "\n\n")

                summary_file.write("TSL\n")
                summary_file.write("Longest line " + "(" + str(longest_line_tsl[1]) + "): " + longest_line_tsl[0] + "\n")
                summary_file.write("Shortest line " + "(" + str(shortest_line_tsl[1]) + "): " + shortest_line_tsl[0] + "\n")
                summary_file.write("Average length: " + str(avg_line_tsl))

if __name__ == "__main__":
    main()
