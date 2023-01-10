program_word = {
    'int':'整数形',
    'float':'浮点型',
    'double':'双精度浮点型',
    'list':'列表',
    'char':'字符',
}

for word,mean in program_word.items():
    print(f"{word}:{mean}")

for word in program_word.keys():
    print(word)

for mean in program_word.values():
    print(mean)