name = input('Enter file: ')
handle = open(name)
print(handle,'\n')


counts = dict()
print('counts',counts)


for line in handle :
    print(line)
    words = line.split()
    print('words are',words)

    for w in words :
        counts[w] = counts.get(w,0) + 1
        print('counts are ',counts,'\t\tw is',w,'\n')
        
bigcount = None
bigword = None

for word,count in counts.items() :
    print(counts.items())
    print('word :-  ',word,'\t','count is :- ',count)
    print('bigword :-  ',bigword,'\t','bigcount is :-  ',bigcount,'\n')
        
    if bigcount is None or count > bigcount :
        bigword = word
        bigcount = count
        print('inside if loop')
        print('word :-  ',word,'\t','count is :- ',count)
        print('bigword :-  ',bigword,'\t','bigcount is :-  ',bigcount,'\n')
        
print('bigword\t',bigword,'\t','bigcount is \t',bigcount)