browsing_session = [1, 2, 3, 4, 5, 6, 7]

# remove element from stack
browsing_session.pop()
print(browsing_session)

# add element to stack
browsing_session.append('9')
print(browsing_session)

# curret position
print(browsing_session[-1])

if not browsing_session:
    print("disable back")
