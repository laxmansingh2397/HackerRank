def designerPdfViewer(h, word):
    
    max_height_of_alphabet = 0

    for alphabet in word:
        index = ord(alphabet) - 97
        height = h[index]
        max_height_of_alphabet = max(max_height_of_alphabet,height)
        
    return max_height_of_alphabet * len(word)

if __name__ == '__main__':

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(result)