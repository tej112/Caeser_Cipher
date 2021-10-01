'''This program prints encrypted/decrypted message of only alphabets(a-z)
    ignoring special charecters(*&%#@etc.,) and spaces
    
    Usage =  ceaser(text,shift,direction)
    where 'text' = the message you want to encrypt/decrypt
          'shift' = number of letters youn want the message to get shifted
          'direction' = encode or decode
          
    TO check how ceaser_cipher works check
        here https://en.wikipedia.org/wiki/Caesar_cipher 
        Thank You '''

from art import logo

run = True
print(logo)


def ceaser(text,shift,direction):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encrypted = []
    decrypted = []
    # if gien shift is greater than number of alphabets 
    # then number is divided by 25 and remainder is taken as ahift number
    if shift < 26:
        shift = shift
    else:
        shift = shift % 25
        
    #the alphabets are arranged in such a way that 
    # each letter is shifted by shift number provided
    arranged_alphabet = alphabet[shift:] + alphabet[:shift]
    #you can use 
    #print(arranged_alphabet)
    #to chech how letters are shifted by given number
    
    if direction == 'encode':
        for i in text:
            #checks only for alphabets and ignores special characters and spaces
            if i in alphabet:
                #for encoding text we get index of original letter from alphabet array 
                #get the same letter from arranged_alphabet array to get encrypted message
                encrypted.append(arranged_alphabet[alphabet.index(i)])
            else:
                encrypted.append(i)
            
        print(f"The encrypted text is {''.join(encrypted)}")
    
    elif direction == 'decode':
        for i in text:
            #checks only for alphabets and ignores special characters and spaces
            if i in alphabet:
                #for decoding text we get index of arranged letter from arranged_alphabet array and
                #get the same letter from alphabet array to get decrypted message                
                decrypted.append(alphabet[arranged_alphabet.index(i)])
            else:
                decrypted.append(i)
        print(f"The decrypted text is {''.join(decrypted)}")
    
    else:
        print("check direction again")
while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = abs(int(input("Type the shift number:\n")))
    ceaser(text,shift,direction)
    x = input("Want to run again? Type 'y' for YES or 'n' for NO\n").lower()
    if x == 'n':
        print("GoodBye :-)")
        run = False
    elif x == 'y':
        run = True
    else:
        print("wrong input BYE!! :-(")
        run = False
