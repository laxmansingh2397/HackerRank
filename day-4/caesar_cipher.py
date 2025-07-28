# s = middle-Outz

def caesarCipher(s, k):
    encode_string = ""
    for char in s:
        if char.isalpha():
            if char.islower():
                character = (ord(char) - ord('a') + k) % 26
                encode_string += chr(character + ord('a'))
            else:
                character = (ord(char) - ord('A') + k) % 26
                encode_string += chr(character + ord('A'))
        else:
            encode_string += char
    
    return encode_string

if __name__ == '__main__':

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)
