def replace_word():
    text = "Hy, im Luis :), and i wanna play Valorant"
    print(text)
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")

    print(text.replace(word_to_replace, word_replacement))


replace_word()
