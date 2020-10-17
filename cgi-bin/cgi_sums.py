#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
listval = form.getlist('operand')

total = 0
for val in listval:
    total += float(val)

print("Content-type: text/plain")
print()
print(f'operand sum: {total}')
