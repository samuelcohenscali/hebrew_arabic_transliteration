from translation_map import translations, clusters, sofit_forms
from pathlib import Path
import string
import unicodedata

# Constant, turn this into a command line arg
HE_TO_AR = False


def replace_sofits(word, sofits):

    non_letter_suffix = ''
    while (
            len(word) > 0 and
        (word[-1] in string.punctuation
                or unicodedata.combining(word[-1])
         )
    ):
        non_letter_suffix = word[-1] + non_letter_suffix
        word = word[:-1]

    for letter in sofits:
        if word.endswith(letter):
            word = word[:-1 * len(letter)]
            word += sofits[letter]
            break

    word += non_letter_suffix

    return word


def search_and_replace(transformations, words, clusters, sofits, second_pass):
    for i in range(len(words)):
        word = words[i]

        # If going back to Arabic, we need to un-sofit the final forms first.
        if HE_TO_AR:
            word = replace_sofits(word, sofits)

        # Replace the special clusters at the start of a word
        for c in clusters:
            if word.startswith(c):
                word = word.replace(c, clusters[c])
                break
        # Replace all other letters.
        for t in transformations:
            word = word.replace(t, transformations[t])

        # Run the "2nd pass" processing.
        for s in second_pass:
            word = word.replace(s, second_pass[s])

        # If going to Hebrew, we need to sofit the final forms.
        if not HE_TO_AR:
            word = replace_sofits(word, sofits)
        words[i] = word
    return words

# Wrapper function to split document into words.
def process_words(document, transformations, clusters, sofits, second_pass):
    lines = document.split('\n')
    processed_lines = [''] * len(lines)
    for i in range(len(lines)):
        l = lines[i]
        words = l.split(' ')
        words = search_and_replace(
            transformations, words, clusters, sofits, second_pass)
        processed_lines[i] = ' '.join(words)

    return '\n'.join(processed_lines)


def main():
    # Open file
    # Run process_words
    transformations = translations
    c = clusters
    s = sofit_forms
    second_pass = second_pass
    document = Path('input.txt').read_text()

    if HE_TO_AR:
        # Flip dictionaries
        transformations = {transformations[k]: k for k in transformations}
        c = {clusters[k]: k for k in clusters}
        # Need to even flip the sofit dictionary, so the sofit transformation can be reversed
        s = {sofit_forms[k]: k for k in sofit_forms}

    processed_text = process_words(document, transformations, c, s, second_pass)
    Path('output.txt').write_text(processed_text)
