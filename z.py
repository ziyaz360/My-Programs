def NewWord(caves, KnownWords):
    NewWords = []
    for cave in caves:
        for word in cave:
            if word not in KnownWords and word not in NewWords:
                NewWords.append(word)
    return NewWords
caves = [["gold", "silver", "emerald"], ["emerald", "diamond", "ruby"], ["sapphire", "silver", "platinum"]]
KnownWords = ["gold", "silver", "platinum"]

output = NewWord(caves, KnownWords)
print(output)
