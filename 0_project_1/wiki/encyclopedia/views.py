from django.shortcuts import render
from django.template import loader
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

def django(request):
    filestr_md = util.get_entry("Django")
    file_html_body = util.markdown_to_html_body(filestr_md, verbose=False)

    return render(request, "encyclopedia\entries_struct.html", {
        "title": "Django",
        "body": file_html_body,
    })

def entries(request, title):
    title_cap = title.capitalize()
    filestr_md = util.get_entry(title_cap)
    file_html_body = util.markdown_to_html_body(filestr_md)

    return render(request, "encyclopedia\entries_struct.html", {
        "title": title_cap,
        "body": file_html_body,
    })
