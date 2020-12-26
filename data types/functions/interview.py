sentence = "this is a common interview question"
sentence = sentence.strip()
A = {}
for i in set(sentence):
    A[i] = sentence.count(i)
print(max(A.values()))
