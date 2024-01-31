class DES:

    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.key = ""
        
    def permutation(self, table):
        int_value = int(self.plain_text, 16)  # Convert hex to integer
        binary_value = bin(int_value)[2:].zfill(64)  # Convert integer to binary
        cipher_text = []
        i=0

        for i in range(len(table)):
            cipher_text.append(binary_value[table[i]-1])

        binary_string = ''.join(str(bit) for bit in cipher_text)
        int_value = int(binary_string, 2)
        hex_value = hex(int_value)[2:]
        self.plain_text = hex_value
        return hex_value
    
    def initial_permutation(self):
        table = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
        return self.permutation(table)
    
    def halves(self):
        return (self.plain_text[:8], self.plain_text[8:])
    

    
    def rounds(self, left, right, i=1):
        if i == 16:
            return str(left) + str(right)
        self.rounds(right, left ^ self.f_function, i+1)



        # f-Function

            # Expansion E

            # XOR with round key

            # S-box substitution
        
            # Permutation

    # Final permutation

    def run(self):
        ip = self.initial_permutation(self)




def main():
    
    des = DES("0123456789ABCDEF")
    ip = des.initial_permutation()
    print(des.halves())
if __name__ == '__main__':
    main()