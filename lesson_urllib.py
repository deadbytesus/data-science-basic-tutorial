import marimo

app = marimo.App()


@app.cell
def _():
    import marimo as mo

    import json
    from urllib.error import HTTPError, URLError
    from urllib.parse import parse_qs, urlencode, urlsplit
    from urllib.request import Request, urlopen

    return (
        HTTPError,
        Request,
        URLError,
        json,
        mo,
        parse_qs,
        urlencode,
        urlopen,
        urlsplit,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Make HTTP requests with Python's `urllib`

        Python already comes with `urllib`, so there's nothing extra to install.
        It can build URLs and send HTTP requests. It takes a few more steps
        than the `requests` library from the companion lesson, but it's useful
        to know what Python can do out of the box.

        A URL is made of a few parts: `https` is the scheme, `api.example.com`
        is the host, and `/books` is the path. Anything after `?` is the query
        string:

        ```text
        https://api.example.com/books?author=Le+Guin&limit=5
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Build a query string safely

    A **query string** starts after `?`; key/value pairs are separated by
    `&`. Use `urlencode()` rather than joining raw input by hand. `urlsplit()`
    can inspect the pieces of a URL.

    URL query parameters are part of the URL. They are different from the
    newer HTTP `QUERY` method, which sends query content in the request body.
    """)
    return


@app.cell
def _(urlencode, urlsplit):
    endpoint = "https://api.example.com/books"
    params = {"author": "Ursula Le Guin", "limit": 5}
    query_string = urlencode(params)
    search_url = f"{endpoint}?{query_string}"
    url_parts = urlsplit(search_url)
    return query_string, search_url, url_parts


@app.cell
def _(query_string):
    query_string


@app.cell
def _(search_url):
    search_url


@app.cell
def _(url_parts):
    url_parts.path


@app.cell
def _(url_parts):
    url_parts.query


@app.cell
def _(parse_qs, urlencode):
    encoded_query = urlencode([("tag", "python"), ("tag", "data")])
    decoded_query = parse_qs(encoded_query)
    return decoded_query, encoded_query


@app.cell
def _(encoded_query):
    encoded_query


@app.cell
def _(decoded_query):
    decoded_query


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Passing a sequence of pairs to `urlencode()` preserves repeated keys,
    such as `tag=python&tag=data`. `parse_qs()` turns the query string into a
    dictionary whose values are lists.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Choose a method and read the response

        `urlopen(url)` sends a GET request by default. To choose another
        method, build a `Request`. A request body must be bytes; JSON text can
        be encoded with `.encode("utf-8")`.

        The next cell builds examples but does not send them. Call `urlopen()`
        only when you are ready to make a real request. Use `with` to close the
        response when you're done. A response's `read()` method returns bytes.

        `QUERY` was standardized in RFC 10008 (June 2026). Like `GET`, it is
        designed to read data safely without changing server state; unlike
        `GET`, it carries query content in the request body. The server must
        support `QUERY` and document the format it expects. Some servers
        advertise supported formats in the `Accept-Query` response header.
        """
    )
    return


@app.cell
def _(Request, json, urlencode):
    url = "https://api.example.com/books"

    get_request = Request(
        f"{url}?{urlencode({'limit': 5})}",
        headers={"Accept": "application/json"},
        method="GET",
    )
    body = json.dumps({"title": "A Wizard of Earthsea"}).encode("utf-8")
    post_request = Request(
        url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    query_body = json.dumps(
        {"filter": {"author": "Ursula Le Guin"}, "limit": 5}
    ).encode("utf-8")
    query_request = Request(
        url,
        data=query_body,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="QUERY",
    )
    return get_request, post_request, query_request


@app.cell
def _(get_request):
    get_request


@app.cell
def _(post_request):
    post_request


@app.cell
def _(query_request):
    query_request


@app.cell
def _(query_request):
    query_request.data.decode("utf-8")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## When something goes wrong

        `HTTPError` represents an HTTP error response (such as 404).
        `URLError` represents a URL or connection problem. `HTTPError` is a
        subclass of `URLError`, so check it first.

        Before trying a real URL, read the API documentation and use a service
        you are allowed to access. Never include private tokens or passwords
        in shared lesson files.
        """
    )
    return


@app.cell
def _(HTTPError, Request, URLError, urlopen):
    def fetch_status(url):
        try:
            with urlopen(Request(url), timeout=10) as response:
                return response.status
        except HTTPError as error:
            print(f"HTTP status: {error.code}")
            raise error
        except URLError as error:
            print(f"Connection problem: {error.reason}")
            raise error

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    1. Use `urlencode()` to add a `page=2` URL query parameter.
    2. Explain how a URL query parameter differs from the HTTP `QUERY` method.
    3. Why might you choose `QUERY` instead of a long GET URL?
    4. Before using `QUERY`, check whether the server supports it and what
       request media type and body format it expects.
    """)
    return


@app.cell
def _():
    # Write your answers here.
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Solution 1": mo.md("""
            ```python
            urlencode({"page": 2})
            ```
            """),
            "Solution 2": mo.md("""
            URL query parameters come after `?` in the URL. HTTP `QUERY` is a
            request method that carries query content in the body.
            """),
            "Solution 3": mo.md("""
            `QUERY` can send a larger or more complex query in the request body
            instead of encoding it all into a long URL.
            """),
            "Solution 4": mo.md("""
            Check the API documentation for `QUERY` support and its required
            `Content-Type` and body format.
            """),
        }
    )


if __name__ == "__main__":
    app.run()
