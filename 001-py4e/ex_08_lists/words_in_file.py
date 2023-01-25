file_name = input("Enter file name: ")

try:
    file_handle = open(file_name)
except:
    print("File can't be opened: ", file_name)
    exit()
    
words = list()

for line in file_handle:
    line_list = line.rstrip().split()
    
    for word in line_list:
        if not word in words:
            words.append(word)
                 
words.sort()
print(words)