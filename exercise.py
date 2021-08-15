import codecs

def copy(file, new_file):
    with open(file, encoding='utf8') as file:
        data = file.read()
    with open(new_file, 'w') as n:
        n.write(data)


# copy('story.txt','story_copy.txt')

def copy_and_reverse(filename, new_file):
    with open(filename, encoding='utf8') as file:
        data = file.read()

    with open(new_file, 'w') as f:
        f.write(data[::-1])


# print(copy_and_reverse('story.txt','story_copy.txt'))
def statistics(filename):
    with open(filename, encoding='utf8') as file:
        # s = file.readlines()
        # print(len(s))
        data = file.read()
        line = data.split("\n")
        word = data.split()
        return {'lines': len(line), 'words': len(word), 'characters': len(data)}

# print(statistics('story.txt'))

def find_and_replace(filename, word, new_word):
    with open(filename, 'r+', encoding ='utf8') as file:
        data = file.read()
        new_data = data.replace(word, new_word, data.find(word))
        file.write(new_data)

find_and_replace('story.txt', 'Alice', 'Colt')
print("Hello")