lines = open("README.md").read().splitlines()
title = "\n".join(lines[:2])
sections = "\n".join(lines[3:]).split("###")[1:]
words = []
def get_word(section):
    i = section.find("\n")
    word = section[:i].strip()
    description = section[i:]
    return word, description
words = [get_word(section) for section in sections]
words = sorted(words, key=lambda item: item[0])
content = "".join([f"### {word}{description}" for word, description in words])
content = title + "\n\n" + content
open("README.md", "w").write(content)
print("Format is complete")
