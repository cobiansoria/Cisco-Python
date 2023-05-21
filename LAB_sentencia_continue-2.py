word_without_vowels = ""

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.

word = input("Ingresa una palabra para el devorador: ")
word = word.upper()

for letter in word:
    # Completa el cuerpo del bucle.
    if letter == 'A':
        continue
    elif letter == 'E':
        continue 
    elif letter == 'I':
        continue 
    elif letter == 'O': 
        continue 
    elif letter == 'U':
        continue
    word_without_vowels += letter
# Imprimir la palabra asignada a word_without_vowels.
print(word_without_vowels)