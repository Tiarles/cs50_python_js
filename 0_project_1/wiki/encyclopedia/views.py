from django.shortcuts import render
from django.http import HttpResponse

from django.template import Context  # , Template

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def css(request):
    filestr_md = util.get_entry("CSS")
    file_html_body = util.markdown_to_html_body(filestr_md, verbose=False)

    return render(request, "encyclopedia\entries_struct.html", {
        "title": "CSS",
        "body": file_html_body,
    })

# def django(request):
#     filestr_md = util.get_entry("Django")
#     file_html_body = util.markdown_to_html_body(filestr_md, verbose=False)
# 
#     return render(request, "encyclopedia\entries_struct.html", {
#         "title": "Django",
#         "body": file_html_body,
#     })

def entries(request, title):
    title_cap = title.capitalize()
    filestr_md = util.get_entry(title_cap)
    file_html_body = util.markdown_to_html_body(filestr_md)

    return render(request, "encyclopedia\entries_struct.html", {
        "title": title_cap,
        "body": file_html_body,
    })

def tmp(request):
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

    elements_list = p.findall(links); print("elements_list:", elements_list)

    print()
    print("HTML:")

    # html_str = p.sub(r'    <li>\1</li>\n', links)

    # html_str = f"<ul>\n{html_str}\n</ul>"; print(html_str)

    from django.template import Template, Context

    with open(r'C:\WORK\cs50_python_js\0_project_1\wiki\encyclopedia\templates\encyclopedia\unordered_list.html', "r") as fhtml:
        template_str = fhtml.read()
    
    print("template_str:", template_str)

    template = Template(template_str)
    context = Context({"elements": elements_list})
    rendered = template.render(context)
    print("rendered:", rendered)

    return HttpResponse("Not found!")
