lower_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypt(text):
    result = []
    for letter in text:
        if letter in lower_alpha:
            if letter < 'z':
                new_letter = lower_alpha[lower_alpha.index(letter) + 1]
                result.append(new_letter)
            elif letter is 'z':
                new_letter = 'a'
                result.append(new_letter)
        elif letter in upper_alpha:
            if letter < 'Z':
                new_letter = upper_alpha[upper_alpha.index(letter) + 1]
                result.append(new_letter)
            elif letter is 'Z':
                new_letter = 'A'
                result.append(new_letter)
        else:
            result.append(letter)
    return ''.join(result)

def decrypt(text):
    result = []
    for letter in text:
        if letter in lower_alpha:
            if letter < 'z':
                new_letter = lower_alpha[lower_alpha.index(letter) - 1]
                result.append(new_letter)
            elif letter is 'z':
                new_letter = 'a'
                result.append(new_letter)
        elif letter in upper_alpha:
            if letter < 'Z':
                new_letter = upper_alpha[upper_alpha.index(letter) - 1]
                result.append(new_letter)
            elif letter is 'Z':
                new_letter = 'A'
                result.append(new_letter)
        else:
            result.append(letter)
    return ''.join(result)

if __name__ == '__main__':
    while True:
        text = encrypt(input('Enter text to encrypt: '))
        print('Your encrypted text is: {}'.format(text))
