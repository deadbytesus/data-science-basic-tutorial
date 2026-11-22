import marimo

app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin

    return BeautifulSoup, mo, requests, urljoin


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Read web pages with Beautiful Soup

        Web pages are written in HTML. If you've ever looked at a page's
        "view source", you've seen tags such as `<h1>`, `<p>`, and `<a>`.
        **Beautiful Soup** helps Python turn that HTML into something you can
        search and work with.

        We'll start with a tiny page stored right here in the lesson, so you
        can experiment without making a network request. You should already
        know basic Python and have seen the `requests` lesson.

        Beautiful Soup reads HTML; it doesn't download pages by itself. For a
        real page, use a tool such as `requests` to fetch the HTML, then pass
        the response text to Beautiful Soup.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## First, meet the HTML

    An HTML **tag** gives content a role. For example, `<h1>` is a main
    heading, `<p>` is a paragraph, and `<a>` is a link. Tags can be nested:
    each book below is an `<article>` with a title, author, and link.
    """)
    return


@app.cell
def _():
    sample_html = """
    <html>
      <head><title>Book notes</title></head>
      <body>
        <h1>Books to read</h1>
        <article class="book" data-id="101">
          <h2 class="title">A Wizard of Earthsea</h2>
          <p class="author">Ursula K. Le Guin</p>
          <a href="/books/101">Book details</a>
        </article>
        <article class="book" data-id="102">
          <h2 class="title">The Hobbit</h2>
          <p class="author">J. R. R. Tolkien</p>
          <a href="/books/102">Book details</a>
        </article>
      </body>
    </html>
    """
    sample_html
    return sample_html


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Parse the page

    `BeautifulSoup(html, "html.parser")` builds a searchable tree from the
    HTML. `"html.parser"` comes with Python. `find()` returns the first
    matching tag; `get_text(strip=True)` returns its text without extra spaces.
    """)
    return


@app.cell
def _(BeautifulSoup, sample_html):
    soup = BeautifulSoup(sample_html, "html.parser")
    page_title = soup.title.get_text()
    first_heading = soup.find("h1").get_text(strip=True)
    return first_heading, page_title, soup


@app.cell
def _(page_title):
    page_title


@app.cell
def _(first_heading):
    first_heading


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Find elements and read their attributes

    `find_all()` returns every matching tag. Narrow the search with a tag name
    and attributes. Use `class_` (with an underscore) because `class` is a
    Python keyword. HTML attributes such as `href`, `id`, and `data-id` can be
    read with `tag.get("href")`.
    """)
    return


@app.cell
def _(soup):
    books = soup.find_all("article", class_="book")
    book_titles = [
        book.find("h2", class_="title").get_text(strip=True)
        for book in books
    ]
    first_book_id = books[0].get("data-id")
    return book_titles, books, first_book_id


@app.cell
def _(books):
    len(books)


@app.cell
def _(book_titles):
    book_titles


@app.cell
def _(first_book_id):
    first_book_id


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## CSS selectors and links

    Beautiful Soup's `select()` and `select_one()` use CSS selector syntax.
    Links often contain relative addresses such as `/books/101`; `urljoin()`
    combines them with the page URL to make complete links.
    """)
    return


@app.cell
def _(books, urljoin):
    book_links = [
        {
            "title": book.find("h2", class_="title").get_text(strip=True),
            "href": urljoin(
                "https://example.com/library/",
                book.find("a").get("href", ""),
            ),
        }
        for book in books
    ]
    return (book_links,)


@app.cell
def _(book_links):
    book_links


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Use it with a real page

        Beautiful Soup parses HTML; `requests` downloads it. The next cell
        defines a helper, but does not contact a site until you call the
        function. Check a site's rules before fetching pages, keep request
        rates reasonable, and prefer an official API when one is available.
        Beautiful Soup doesn't run page JavaScript.

        **Tip:** HTML can be inconsistent or change over time. Check that an
        element exists before calling methods on it.
        """
    )
    return


@app.cell
def _(BeautifulSoup, requests):
    def page_heading(page_url):
        response = requests.get(
            page_url,
            headers={"User-Agent": "LearningExample/1.0"},
            timeout=10,
        )
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        heading = soup.select_one("h1")
        if heading is None:
            return None
        return heading.get_text(strip=True)

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    1. Add a third book to the HTML and find its title.
    2. Collect every book link with `select("article.book a")`.
    3. Find each author's name and make a list.
    4. What happens if you search for a tag that isn't in the page?
    """)
    return


@app.cell
def _():
    # Add your book and try the selectors here.
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Solution 1": mo.md("""
            Add another `<article class="book">` with an `<h2 class="title">`
            tag inside `sample_html`, then run:

            ```python
            soup = BeautifulSoup(sample_html, "html.parser")
            [book.find("h2", class_="title").get_text(strip=True)
             for book in soup.find_all("article", class_="book")]
            ```
            """),
            "Solution 2": mo.md("""
            ```python
            [link.get("href") for link in soup.select("article.book a")]
            ```
            """),
            "Solution 3": mo.md("""
            ```python
            [book.select_one("p.author").get_text(strip=True)
             for book in soup.select("article.book")]
            ```
            """),
            "Solution 4": mo.md("""
            `find()` returns `None` when the tag is missing. Check the result
            before calling methods such as `get_text()` on it.
            """),
        }
    )


if __name__ == "__main__":
    app.run()
