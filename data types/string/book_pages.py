last_page = int(input())
page = int(input())
if page % 2 == 0:
    page = page+1
if last_page % 2 == 0:
    last_page = last_page+1
elif last_page-page == 1:
    print("0")
a = last_page-page
b = page-1
if last_page-page <= page-1:
    print(a//2)
else:
    print(b//2)
