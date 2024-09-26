def A():
    return """tripleQuotes = chr(34)*3
newline = chr(10)
B_self = A()
A_self = newline.join(["def A():",f"    return {tripleQuotes}{B_self}{tripleQuotes}"])
self = newline.join([A_self,B_self])
# We have obtained the <SELF>. Do anything you want with it
# Add anything you do here to the end of A's string
# Use chr(x) instead of slashes, don't use triple quotes
print(len(self), end="")
"""
tripleQuotes = chr(34)*3
newline = chr(10)
B_self = A()
A_self = newline.join(["def A():",f"    return {tripleQuotes}{B_self}{tripleQuotes}"])
self = newline.join([A_self,B_self])
# We have obtained the <SELF>. Do anything you want with it
# Add anything you do here to the end of A's string
# Use chr(x) instead of slashes, don't use triple quotes
print(len(self), end="")
