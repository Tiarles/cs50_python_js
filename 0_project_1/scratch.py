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

###########################################################

import re

links = r"to an [HTML](/wiki/HTML) page. Also, on [Github](www.github.com) you can find more details."

p = re.compile(R'\[(.*?)\]\((.*?)\)', re.M)
# m = p.findall(links); print(m)
# m = p.search(links); print(m)


html_str = p.sub(R'<a href="\2">\1</a>', links); print(html_str)

###########################################################

import re

p = re.compile(R"^\* (.*)$\n", re.M)

links = """peido da onca
* headings
* paragraphs
* lists
* links
* and more!

asdasdasdf * and more!"""

print(links)
# print(repr(links))

elements_list = p.findall(links); print(elements_list)

print()
print("HTML:")

# html_str = p.sub(r'    <li>\1</li>\n', links)

# html_str = f"<ul>\n{html_str}\n</ul>"; print(html_str)

from django.template import Template, Context

with open(r'C:\WORK\cs50_python_js\0_project_1\wiki\encyclopedia\templates\encyclopedia\unordered_list.html', "r") as fhtml:
    template_str = fhtml.read()

template = Template(template_str)
context = Context({"elements": elements_list})
rendered = template.render(context)
print("rendered:", rendered)


###########################################################

"^([a-zA-Z0-9 \[\]\(\)\/\*])*$\n"

"""
# CSS

CSS is a language that can be used to add style to an [HTML](/wiki/HTML) page.


# Django

Django is a web framework written using [Python](/wiki/Python) that allows for the design of web applications that generate [HTML](/wiki/HTML) dynamically.


# Git

Git is a version control tool that can be used to keep track of versions of a software project.

## GitHub

GitHub is an online service for hosting git repositories.


# HTML

HTML is a markup language that can be used to define the structure of a web page. HTML elements include

* headings
* paragraphs
* lists
* links
* and more!

The most recent major version of HTML is HTML5.


# Python

Python is a programming language that can be used both for writing **command-line scripts** or building **web applications**.

"""