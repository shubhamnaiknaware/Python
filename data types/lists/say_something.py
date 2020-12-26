output = ''
while True:
    string = input('Say Something :')
    t = ('where', 'when', 'how', 'why', 'what', 'whom')
    if string == '\end':
        break
    if string.startswith(t):
        output += string.capitalize() + '?'
    else:
        output += string.capitalize() + '.'
print(output)
