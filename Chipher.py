shift = input("shift for chipher: ")
text = input("what text you want to encrypt: ")


def chipher(shift, text):
    alphabet = list(" abcdefghijklmnopqrstuvwxyz")
    text_list = list(text)  
    shift_list = int(shift)
    num = len(text)
    for i in range(num):
        elem = text_list[i]            # elem   это буква из введеного текста 
        index = alphabet.index(elem)   # index  это индекс элемента из алфавита 
        if index + shift_list < 27:
            text_list[i] = alphabet[index + shift_list]
          
            a = text_list
            
            
        else:
            text_list[i] = alphabet[(index + shift_list) - 27]
            a = text_list
        
        chiphered_text = "".join(a)
    print(chiphered_text) 
        
    
chipher(shift, text)
