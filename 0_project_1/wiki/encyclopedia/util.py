import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries(format=None):
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    
    ret = list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))
    
    if format == "capitalize":
        for i, entry in enumerate(ret):
            ret[i] = entry.capitalize()

    elif format == "lower":
        for i, entry in enumerate(ret):
            ret[i] = entry.lower()

    return ret


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        ret = f.read().decode("utf-8")
        return ret
    except FileNotFoundError:
        return None

#
# My new functions
#

def _unoredered_list_converter(string):
    ul_pattern = re.compile(r'^\s*[-\*\+] (.*)')
    lines = string.split('\n')

    ul_flag = False

    html_body = []

    for i, line in enumerate(lines):
        m = ul_pattern.match(line)
        
        if m is not None: 
            if not ul_flag:
                ul_flag = True
                html_body.append("<ul>")

            html_body.append(f"<li>{m.group(1)}</li>")

            if ul_pattern.match(lines[i+1]) is None:
                ul_flag = False
                html_body.append("</ul>")
        else:
            html_body.append(line)

    html_body = '\n'.join(html_body)
    return html_body


def markdown_to_html_body(filestr, verbose=False):
    patterns = { # 1/2 Replacements
        "h1":     (re.compile('^# (.*)', re.M),             r'<h1>\1</h1>'),
        "h2":     (re.compile('^## (.*)', re.M),            r'<h2>\1</h2>'),
        "h3":     (re.compile('^### (.*)', re.M),           r'<h3>\1</h3>'),
        "h4":     (re.compile('^#### (.*)', re.M),          r'<h4>\1</h4>'),
        "h5":     (re.compile('^##### (.*)', re.M),         r'<h5>\1</h5>'),
        "h6":     (re.compile('^###### (.*)', re.M),        r'<h6>\1</h6>'),
        "a":      (re.compile(R'\[(.*?)\]\((.*?)\)', re.M), r'<a href="\2">\1</a>'),
        "strong": (re.compile(R'\*\*(.*?)\*\*', re.M),      r'<strong>\1</strong>'),
    }

    file_html_body = filestr

    for key in patterns:
        pattern, sub_str = patterns[key]
        file_html_body = pattern.sub(sub_str, file_html_body)
    
    # Checking unordered list and add HTML Template
    file_html_body = _unoredered_list_converter(file_html_body)
    
    if verbose:
        print("Markdown:")
        print(filestr)
        print()
        print("HTML:")
        print(file_html_body)

    return file_html_body


def render_markdown(title):
    title_cap = title.capitalize()
    filestr_md = get_entry(title_cap)

    if filestr_md is not None:
        return markdown_to_html_body(filestr_md)
    else:
        return None
