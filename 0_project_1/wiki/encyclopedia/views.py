from django.shortcuts import render
from django.http import HttpResponse

from django.template import Context  # , Template

from . import util


def get_searched_title(request):
    """Function used for all the vies to implement request 
    treatment for the "Search Encyclopedia input"""
    search_topic = request.GET.get('q')

    if search_topic is None:
        # In case the search topic was not defined, 
        # will skip and render the original page
        return None

    list_entries_low = util.list_entries(format="lower")
    search_topic_low = search_topic.lower()

    # Check exactly the title in lower case
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
        matches = []
        list_entries_low = util.list_entries(format="lower")

        for entry in util.list_entries():
            if search_topic_low in entry.lower():
                matches.append(entry)
        
        if len(matches) == 0:
            # Show the page 404
            return render(request, "encyclopedia\error_404.html", {
                "title": search_topic
            })
        else:
            # Show all the possible matches in case the search cannot find a topic
            return render(request, "encyclopedia\search_matches.html", {
                "entries": matches
            })


def index(request):
    entry_request = get_searched_title(request)

    if entry_request is not None:
        # Render entry template when something on the entry "Search Encyclopedia" was typed
        return entry_request

    else:
        # Show the index page
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })


def entries(request, title):
    entry_request = get_searched_title(request)
    if entry_request:
        # Implement entry request for the "Search Encyclopedia" also for the new_page
        return entry_request
    else:
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
    entry_request = get_searched_title(request)
    if entry_request:
        # Implement entry request for the "Search Encyclopedia" also for the random page
        return entry_request
    else:
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
    entry_request = get_searched_title(request)
    if entry_request:
        # Implement entry request for the "Search Encyclopedia" also for the new_page
        return entry_request
    else:
        return render(request, R"encyclopedia\new_page.html", {})
