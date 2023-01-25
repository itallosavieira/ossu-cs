file_name = input("Enter file name: ")
try:
    file_handle = open(file_name)
except:
    print("File can't be opened: ", file_name)
    exit()

count = 0
total = 0

for line in file_handle:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    
    count = count + 1
    total = total + float(line[len('X-DSPAM-Confidence:'):len(line)])

average = total / count
print('Average spam confidence:', average)