from urllib.request import * 
URL = "https://www.geeksforgeeks.org/data-structures/"
r = getcode(URL) 
print(r.content) 
