import markovify

maxsyllables = 8  # set limit of syllables per line
max_length = 10
text_file = 'inspiring_poems.txt'  # read training dataset


def markov(text_file):
    # define a function that creates a markov model of a text
    read = open(text_file, "r", encoding='utf-8').read()
    text_model = markovify.NewlineText(read)
    return text_model


def syllables(line):
    # define a function to makes sure the we don't exceed a set number of syllables
    count = 0
    for word in line.split(" "):
        vowels = 'aeiouy'
        word = word.lower().strip(".:;?!")
        if word[0] in vowels:
            # a vowel found at the begining of the word makes a syllable
            count += 1
        for index in range(1, len(word)):
            # a non-vowel followed by a vowel makes a syllable
            if word[index] in vowels and word[index-1] not in vowels:
                count += 1
        if word.endswith('e'):
            # if word ends in (silent) 'e', that is not a syllable
            count -= 1
        if word.endswith('le'):
            # unless 'le'
            count += 1
        if count == 0:
            count += 1
    return count / maxsyllables


# execute the functions to generate the poem
markov_model = markov(text_file)
bars = []  # initialise poem as list of lines
last_words = []  # initialise last words of each line
poem_length = len(
    open(text_file, encoding='utf-8').read().split("\n"))  # poem length
# we won't use this because we read a collection of poems
count = 0  # initialise count of lines


while len(bars) < max_length and count < poem_length * 2:
    bar = markov_model.make_sentence(max_overlap_ratio=.49, tries=100)
    if type(bar) != type(None) and syllables(bar) < 1:
        def get_last_word(bar):
            last_word = bar.split(" ")[-1]
            if last_word[-1] in "!.?,":
                last_word = last_word[:-1]
            return last_word
        last_word = get_last_word(bar)
        if bar not in bars and last_words.count(last_word) < 3:
            bars.append(bar)
            last_words.append(last_word)
            count += 1


poem = '\n'.join(str(i) for i in bars)

with open("output.txt", "w") as file:
    file.write(poem)
output = open("output.txt", "r")
print(output.read())
