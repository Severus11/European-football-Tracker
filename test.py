from googlesearch import search
query = "bundesliga,  reference 2014"

for j in search(query, tld="com", num=1, stop=1, pause =2):
    url = j

print(url)


    