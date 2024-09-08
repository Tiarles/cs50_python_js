from django.shortcuts import render
from django.http import HttpResponse

from django.template import Context  # , Template

from . import util


def index(request):    
    search_topic = request.GET.get('q')

    if search_topic is not None:
        search_topic_cap = search_topic.capitalize()
        search_topic_valid = search_topic_cap in util.list_entries(capitalize=True)

        if search_topic_valid:
            # Show the searched page
            file_html_body = util.render_markdown(title=search_topic_cap)

            return render(request, "encyclopedia\entries_struct.html", {
                "title": search_topic,
                "body": file_html_body,
            })
        else:
            # Show the page 404
            return render(request, "encyclopedia\error_404.html", {
                "title": search_topic
            })
    else:
        # Show the index page
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })


def entries(request, title):
    file_html_body = util.render_markdown(title)

    if file_html_body is None:
        return render(request, "encyclopedia\error_404.html", {
            "title": title
        })
    else:
        return render(request, "encyclopedia\entries_struct.html", {
            "title": title,
            "body": file_html_body,
        })


def random_page(request):
    import random

    title = random.choice(util.list_entries())
    title_cap = title.capitalize()
    filestr_md = util.get_entry(title_cap)
    file_html_body = util.markdown_to_html_body(filestr_md)

    return render(request, "encyclopedia\entries_struct.html", {
        "title": title_cap,
        "body": file_html_body,
    })


def new_page(request):
    return render(request, R"encyclopedia\new_page.html", {})
