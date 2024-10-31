from django.core.files.storage import default_storage
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context  # , Template
from django import forms

from . import util

# Form entry class

class NewEntry(forms.Form):
    title = forms.CharField(
        label="title",
        widget=forms.TextInput(
            attrs={
                "id": "create_new_page__title",
                "placeholder": "Title"
            }
        )
    )
    content = forms.CharField(
        label="content",
        widget=forms.Textarea(
            attrs={
                # "name": "new_page_content",
                "id": "create_new_page__textarea"
            }
        )
    )

# Search Encyclopedia request treatment

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
        title = search_topic_low.capitalize()
        file_html_body = util.render_markdown(title=title)

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

# Views

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
    import random
    title = random.choice(util.list_entries())

    return entries(request, title)


def new_page(request):
    entry_request = get_searched_title(request)
    if entry_request:
        # Implement entry request for the "Search Encyclopedia" also for the new_page
        return entry_request
    else:
        if request.method == "POST":
            form_entry = NewEntry(request.POST)

            if form_entry.is_valid():
                title = form_entry.cleaned_data["title"]
                content = form_entry.cleaned_data["content"]

                list_entries_low = util.list_entries(format="lower")

                if title.lower() in list_entries_low:
                    return render(request, "encyclopedia\error_404.html", {
                        "title": title,
                        "context": "exist"
                    })

                util.save_entry(title, bytes(content, "utf8"))
                file_html_body = util.render_markdown(title)
            
                return render(request, "encyclopedia\entries_struct.html", {
                    "title": title,
                    "body": file_html_body,
                })

        return render(request, R"encyclopedia\new_page.html", {
            "form": NewEntry()
        })


def edit_page(request, title):
    entry_request = get_searched_title(request)
    if entry_request:
        # Implement entry request for the "Search Encyclopedia" also for the new_page
        return entry_request
    else:
        content = util.get_entry(title)

        if request.method == "POST":
            form_entry = NewEntry(request.POST)

            if form_entry.is_valid():
                title = form_entry.cleaned_data["title"]
                content = form_entry.cleaned_data["content"]; print(f"POST content: {content}")

                util.save_entry(title, bytes(content, "utf8"))
                file_html_body = util.render_markdown(title)
            
                return render(request, "encyclopedia\entries_struct.html", {
                    "title": title,
                    "body": file_html_body,
                })

        form_entry_2 = NewEntry()
        form_entry_2.fields['title'].initial = title
        form_entry_2.fields['content'].initial = content

        return render(request, R"encyclopedia\edit_page.html", {
            "title": title,
            "form": form_entry_2,
        })


def tutorial_spec(request):
    f = default_storage.open(f"entries/Tutorial Specification.html")
    html_body = f.read().decode("utf-8")

    return render(request, "encyclopedia\entries_struct.html", {
        "title": "Tutorial Specification",
        "body": html_body,
    })
