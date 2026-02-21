count = 0
with  open('words.txt','r') as f:
    content = f.read().split()

for i in content:
    if len(i) > 1:
        count+= 1

print(count)


