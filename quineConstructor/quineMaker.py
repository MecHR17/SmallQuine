total = ""
B = """tripleQuotes = chr(34)*3
newline = chr(10)
B_self = A()
A_self = newline.join(["def A():",f"    return {tripleQuotes}{B_self}{tripleQuotes}"])
self_code = newline.join([A_self,B_self])
"""
with open("quineInput.py","r") as f:
    code = f.readlines()
    code = code[1:]
    code = "\n".join(code)
    triple_quotes = "\""*3
    total += "\n".join(["def A():",f"    return {triple_quotes}{B}{code}{triple_quotes}\n"])
    total += B
    total += code
with open("quineOutput.py","w") as f:
    f.write(total)