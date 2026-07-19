def cleanstring(s):
    return s.upper().strip()

def extract_substring(s,index):
    return s[index:]

def replace_vowel(s):
    return (s.replace("a", "*")
             .replace("e", "*")
             .replace("i", "*")
             .replace("o", "*")
             .replace("u", "*")
             .replace("A", "*")
             .replace("E", "*")
             .replace("I", "*")
             .replace("O", "*")
             .replace("U", "*"))
def split_string(s):
    return s.split()

def join_list(a):
    return ','.join(a)

s=" hello python wordld"

#cleanstring
m=s.upper().strip()
print(m) #HELLO PYTHON WORLD

#extract substring
print(s[6:]) #python world

r=(s.replace("a", "*")
             .replace("e", "*")
             .replace("i", "*")
             .replace("o", "*")
             .replace("u", "*")
             .replace("A", "*")
             .replace("E", "*")
             .replace("I", "*")
             .replace("O", "*")
             .replace("U", "*"))
print(r)

print(s.split())

a=['apple','banana','guava']

print(','.join(a))

