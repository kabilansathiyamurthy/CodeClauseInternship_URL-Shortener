import pyshorteners
a = input("Enter the URL to shorten: ")
type_tiny = pyshorteners.Shortener()
b = type_tiny.tinyurl.short(a)
print("The Shortened URL is: " + b)