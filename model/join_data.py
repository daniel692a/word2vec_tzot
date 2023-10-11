import glob

lines = []

def read_files(filename:str)->None:
    chapter = open(filename, 'r')
    verses = chapter.readlines()
    for verse in verses:
        if verse != '':
            lines.append(verse) 
    chapter.close()

def write_lines()->None:
    output = open('corpus.txt', 'w')
    output.writelines(lines)
    output.close()

txt_counter = len(glob.glob1("../data/", "*.txt"))

for i in range(1, txt_counter+1):
    filename = f"../data/chapter-{i}.txt"
    read_files(filename)

write_lines()

