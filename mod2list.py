a = "my name is Susan and Susan is my name".split()
print(set(a))
b = set("my month is june and june is my month".split())
print(b)

print(a)
for word in set(a):
    print(word, a.count(word))

a = set(a)

print(a.intersection(b))
print(a.symmetric_difference(b))
print(a.union(b))
