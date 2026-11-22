import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import requests

    return mo, requests


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Talk to web APIs with `requests`

    A web API lets your program ask a server for information or send it
    some data. Your program sends an **HTTP request**; the server replies
    with an **HTTP response**. If you know Python variables, lists,
    dictionaries, and functions, you have enough Python for this lesson.

    We'll use `requests`, a popular library that makes these conversations
    much easier to write than using Python's standard tools directly.

    The examples here won't contact a server on their own. When you're
    ready to try one for real, use the API's documentation to find an
    endpoint that is safe to use.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## What do the HTTP methods mean?

    The **method** tells the server what you want to do. These are the
    usual meanings; a particular API may support only some of them.

    | Method | Typical purpose | Example |
    | --- | --- | --- |
    | `GET` | Read or search for data | Get a list of books |
    | `POST` | Create something or submit data | Add a new book |
    | `PUT` | Replace a resource | Replace all fields of a book |
    | `PATCH` | Change selected fields | Change only a book's title |
    | `DELETE` | Remove a resource | Delete a book |
    | `QUERY` | Send a query in the request body | Search a large catalog |

    `QUERY` is a newer, standardized HTTP method (RFC 10008, June 2026).
    Like `GET`, it is meant to retrieve results without changing the
    resource. Unlike `GET`, it sends the query in the request body. This
    helps when a search is too large or complicated to fit comfortably in
    the URL. Unlike `POST`, `QUERY` is defined as safe and idempotent, so
    clients can retry it without asking for a state change.

    `GET` queries usually go in the URL. `POST`, `PUT`, and `PATCH` commonly
    send data in the body. `DELETE` commonly identifies the resource in
    the URL. These are conventions, not universal rules. A server must
    explicitly support `QUERY`; many APIs do not yet.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Search and filter with query parameters

    Query parameters are key/value pairs added to a URL after `?`, separated
    by `&`. They are commonly used for searching, filtering, sorting, and
    pagination. Pass a dictionary with `params=`; `requests` will encode it
    safely.

    URL query parameters are **not** the HTTP `QUERY` method. One goes in the
    URL; the other sends a query document in the request body. For `QUERY`,
    check the API documentation or its `Accept-Query` response header.
    """)
    return


@app.cell
def _(requests):
    base_url = "https://api.example.com/books"
    search_params = {"author": "Ursula Le Guin", "limit": 5}
    prepared_get = requests.Request(
        "GET", base_url, params=search_params
    ).prepare()
    prepared_get.url
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Send a request and read the reply

    The next cell defines example functions for the common methods. They
    don't contact a server until you call one. Replace the example URL
    with an endpoint from the API documentation.

    `raise_for_status()` reports unsuccessful HTTP status codes. A response
    also has `status_code`, `headers`, `text`, and (for JSON) `json()`.
    Always set a timeout. Check the API's authentication instructions and
    never put credentials in a notebook you plan to share.
    """)
    return


@app.cell
def _(requests):
    def get_books(url, author, limit=5):
        response = requests.get(
            url,
            params={"author": author, "limit": limit},
            timeout=10,
        )
        response.raise_for_status()
        return response.json()

    def create_book(url, title):
        return requests.post(url, json={"title": title}, timeout=10)

    def replace_book(url, title):
        return requests.put(url, json={"title": title}, timeout=10)

    def update_book_title(url, title):
        return requests.patch(url, json={"title": title}, timeout=10)

    def delete_book(url):
        return requests.delete(url, timeout=10)

    def query_books(url, query):
        return requests.request(
            "QUERY",
            url,
            json=query,
            headers={"Accept": "application/json"},
            timeout=10,
        )

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## What if the request doesn't work?

    Network calls can fail because of a connection problem, a timeout, or
    an unsuccessful HTTP status. The next cell defines a helper that
    catches common request errors, reports them, and raises the error
    again so a failure is not mistaken for a successful result.
    """)
    return


@app.cell
def _(requests):
    def fetch_books(url):
        try:
            response = requests.get(url, params={"limit": 5}, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout as error:
            print("The server took too long to respond.")
            raise error
        except requests.exceptions.HTTPError as error:
            print(f"The server returned an unsuccessful status: {error}")
            raise error
        except requests.exceptions.RequestException as error:
            print(f"Could not complete the request: {error}")
            raise error

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    1. Predict the URL for a search with `page=2` and `search="blue whales"`.
    2. How is a URL query string different from the HTTP `QUERY` method?
    3. Why might an API offer `QUERY` instead of a long GET URL?
    4. Check whether an API supports `QUERY` before trying it.

    **Remember:** URL query parameters go in the URL. The HTTP `QUERY` method
    puts a query document in the request body.
    """)
    return


@app.cell
def _():
    # Write your answers here.
    pass
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Solution 1": mo.md("""
            ```python
            params = {"page": 2, "search": "blue whales"}
            requests.Request(
                "GET", "https://api.example.com/books", params=params
            ).prepare().url
            ```
            """),
            "Solution 2": mo.md("""
            URL query parameters are part of the URL after `?`. The HTTP
            `QUERY` method sends a query document in the request body.
            """),
            "Solution 3": mo.md("""
            A `QUERY` request can carry a larger or more structured query in
            its body without making the URL very long.
            """),
            "Solution 4": mo.md("""
            Check the API documentation for supported methods, request
            `Content-Type`, body format, response format, and authentication.
            """),
        }
    )
    return


if __name__ == "__main__":
    app.run()
