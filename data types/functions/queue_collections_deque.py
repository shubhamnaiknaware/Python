from collections import deque
l = deque([])
# add element to queue
l.append(1)
l.append(2)
l.append(3)
l.append(4)

# remove first element of queue
l.popleft()

# print
print(l)

# if empty queue
if not l:
    print("empty queue")
