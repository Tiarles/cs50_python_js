import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    
    print("filenames:", filenames)

    ret = list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))

    print("ret: ", ret)

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
        ret = f.read().decode("utf-8"); print("ret: ", ret)
        return ret
    except FileNotFoundError:
        return None


def markdown_to_html_body(file_md_path, verbose=False):
    import re
    import os

    # folder_path = os.path.dirname(file_md_path)
    title = os.path.basename(file_md_path)

    patterns = {
        "h1": (re.compile('^# (.*)', re.M), r'<h1>\1</h1>'),
        "h2": (re.compile('^## (.*)', re.M), r'<h2>\1</h2>'),
        "h3": (re.compile('^### (.*)', re.M), r'<h3>\1</h3>'),
        "h4": (re.compile('^#### (.*)', re.M), r'<h4>\1</h4>'),
        "h5": (re.compile('^##### (.*)', re.M), r'<h5>\1</h5>'),
        "h6": (re.compile('^###### (.*)', re.M), r'<h6>\1</h6>'),
        "a": (re.compile(R'\[(.*?)\]\((.*?)\)', re.M), r'<a href="\2">\1</a>')
    }

    with open(file_md_path, 'r') as fmd:
        filestr = fmd.read()

    if verbose:
        print("Markdown:")
        print(filestr)

    file_html_body = filestr

    for pattern, sub_str in patterns.values():
        file_html_body = pattern.sub(sub_str, file_html_body)

    if verbose:
        print("\nHTML:")
        print(file_html_body)

    with open(file_md_path, 'w') as fmd:
        filestr = fmd.read()


    return file_html_body, title
