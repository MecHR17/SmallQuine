def A():
    return """self = A()
og_self = self
x = self.find(chr(34)*3)
self = self[:x] + chr(92) + self[x:]
x = self.find("}"+chr(34)*3)
self = self[:x+1] + chr(92) + self[x+1:]
total = ""
total += 'def A():' + chr(10)
total += f'    return \"""{self}\"""' + chr(10)
total += chr(10)
total += og_self
print(len(total), end="")
"""

self = A()
og_self = self
x = self.find(chr(34)*3)
self = self[:x] + chr(92) + self[x:]
x = self.find("}"+chr(34)*3)
self = self[:x+1] + chr(92) + self[x+1:]
total = ""
total += 'def A():' + chr(10)
total += f'    return """{self}"""' + chr(10)
total += chr(10)
total += og_self
print(len(total), end="")
