import PyPDF2
import re
from tika import parser 

raw = parser.from_file('MAT_1.pdf')
print(type(raw['content']))
s = raw['content']
print(s)
new = re.sub('\D', '', s)
print()
