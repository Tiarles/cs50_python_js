filepath = r"C:\Tiarles\cs50_python_js\0_project_1\wiki\entries\CSS.md"

for i, row in enumerate(open(filepath)):
    # if title is None:  # To add HTML Title
    #     html_title = pattern['title'].match(row)

    # match = p.match(row)

    match = p.sub(r"<h1>\1</h1>", row)
    if match:
        print(f"Match: {match}")
    else:
        print(f"No match!")

#########################################

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

#####################################

import re

links = r"to an [HTML](/wiki/HTML) page. Also, on [Github](www.github.com) you can find more details."

p = re.compile(R'\[(.*?)\]\((.*?)\)', re.M)
# m = p.findall(links); print(m)
# m = p.search(links); print(m)


html_str = p.sub(R'<a href="\2">\1</a>', links); print(html_str)

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

