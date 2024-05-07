import re

p = re.compile('[a-z]+')
m = p.match("tempo")
print(m.group())
print(m.span())

p = re.compile('[a-z]+')
# m = p.match("::: message")
m = p.search("::: message")
print(m.group())
print(m.span())

###############################
import re

p = re.compile('section{ ( [^}]* ) }', re.VERBOSE)
p.sub(r'subsection{\1}','section{First} section{second}')
print()


###############################

import re

filepath = r"C:\Tiarles\cs50_python_js\0_project_1\wiki\entries\CSS.md"

patterns = {
    "h1": (re.compile('^# (.*)', re.M), r'<h1>\1</h1>'),
    "h2": (re.compile('^## (.*)', re.M), r'<h2>\1</h2>'),
    "h3": (re.compile('^### (.*)', re.M), r'<h3>\1</h3>'),
    "h4": (re.compile('^#### (.*)', re.M), r'<h4>\1</h4>'),
    "h5": (re.compile('^##### (.*)', re.M), r'<h5>\1</h5>'),
    "h6": (re.compile('^###### (.*)', re.M), r'<h6>\1</h6>'),
}

with open(filepath, 'r') as fmd:
    filestr = fmd.read()

print("Markdown:")
print(repr(filestr))

file_html = filestr

for pattern, sub_str in patterns.values():
    file_html = pattern.sub(sub_str, file_html)

print("\nHTML:")
print(file_html)


for i, row in enumerate(open(filepath)):
    # if title is None:  # To add HTML Title
    #     html_title = pattern['title'].match(row)

    # match = p.match(row)

    match = p.sub(r"<h1>\1</h1>", row)
    if match:
        print(f"Match: {match}")
    else:
        print(f"No match!")

#####################################

import re

links = r"to an [HTML](/wiki/HTML) page."

# p = re.compile(R'\[(.*)\]\((.*)\)', re.M)
p = re.compile(r'\((.*)\)')
m = p.match(links)
print(m)

########################################################
def removing_console_color_chars(packet_str):
    import re

    # 7-bit C1 ANSI sequences
    ansi_escape = re.compile(r'''
        \x1B  # ESC
        (?:   # 7-bit C1 Fe (except CSI)
            [@-Z\\-_]
        |     # or [ for CSI, followed by a control sequence
            \[
            [0-?]*  # Parameter bytes
            [ -/]*  # Intermediate bytes
            [@-~]   # Final byte
        )
    ''', re.VERBOSE)
    return ansi_escape.sub('', packet_str)

