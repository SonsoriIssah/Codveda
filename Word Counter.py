def word_counter(filename):
 try:#Avoid getting bugs for files not present
     with  open(filename +'.txt','r') as f:
      content = f.read().split()
     count = [i for i in content if len(i)>1]
     return len(count)
 except FileExistsError as e:
   print(e)


filename = input('Filename: ') 
print(word_counter(filename))





