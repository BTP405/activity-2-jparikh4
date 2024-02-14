def wordCount(t):
    word_dict = {}
    with open(t, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            words = line.strip().split()

            for word in words:
                word = word.strip('.,!?').lower()

                if word not in word_dict:
                    word_dict[word] = []
                if line_number not in word_dict[word]:
                    word_dict[word].append(line_number)

    return word_dict

# Example:
text_file = "word.txt"
result = wordCount(text_file)
