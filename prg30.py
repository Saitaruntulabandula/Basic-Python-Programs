from http.client import HTTPConnection
conn = HTTPConnection("google.com")
conn.request("GET", "/")
result = conn.getresponse()
contents = result.read()
print(contents)