from django.shortcuts import render
from django.http import HttpResponse

from django.template import Context  # , Template

from . import util


def index(request):    
    search_topic = request.GET.get('q')

    if search_topic is not None:
        list_entries_low = util.list_entries(format="lower")

        search_topic_low = search_topic.lower()
        search_topic_valid = search_topic_low in list_entries_low

        if search_topic_valid:
            # Show the searched page
            file_html_body = util.render_markdown(title=search_topic_low.capitalize())

            return render(request, "encyclopedia\entries_struct.html", {
                "title": search_topic,
                "body": file_html_body,
            })
        else:
            # Try to search through substring
            # list_entries_low = util.list_entries(format="lower")
            print(f"list_entries_low: {list_entries_low}")
            for entry in list_entries_low:
                if search_topic in list_entries_low:
                    search_topic_cap = entry.capitalize()
                    print(f"search_topic_cap: {search_topic_cap}")

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
    print("title: ", title)
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
