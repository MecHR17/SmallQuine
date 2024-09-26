def A():
    return """tripleQuotes = chr(34)*3
newline = chr(10)
B_self = A()
A_self = newline.join(["def A():",f"    return {tripleQuotes}{B_self}{tripleQuotes}"])
self_code = newline.join([A_self,B_self])
print(len(self_code))
"""
tripleQuotes = chr(34)*3
newline = chr(10)
B_self = A()
A_self = newline.join(["def A():",f"    return {tripleQuotes}{B_self}{tripleQuotes}"])
self_code = newline.join([A_self,B_self])
print(len(self_code))
