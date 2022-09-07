def count_letters(x):
    dictionary = {}
    x = x.lower()
    x = "".join(x.split())
    print(x)
    dictionary = {}
    for t in x:
        if t not in dictionary:
            dictionary[t] = 0
        dictionary[t] = dictionary[t] + 1
    return dictionary
            #continue
           # dictionary[t] = x.count[t.lower()]
           # return dictionary
x = input("Enter a string:")
print(count_letters(x))

# got help from TAs
