def faylis_statistika(filename):
    try:
        f = open(filename , "r") 
        text = f.read()          
        f.close()                

        lines = len(text.splitlines()) 
        words = len(text.split())      
        chars = len(text)              

        return lines, words, chars     

    except FileNotFoundError:
        return "ფაილი არ არსებობს"   
result = faylis_statistika("text.txt")

if type (result) == str:
    print(result)
else:                       
    print("ხაზები: ", result[0])
    print("სიტყვები: ", result[1])
    print("სიმბოლოები: ", result[2])


 
def ramdenjer(filename, word):
    try:
        f = open(filename, "r")
        text = f.read()
        f.close()
        text = text.lower()
        word = word.lower()
        words = text.split()
        counter = 0
        for w in words:
            if w == word:
                counter += 1

        return counter
    except FileNotFoundError:
        return "ფაილი არ მოიძებნა"

filename = "text.txt"
result = ramdenjer(filename, "python")
print(f" 'python' ფაილში არის {result} ჯერ ")