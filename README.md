# data-science-basic-tutorial

Minimal, hands-on Data Science lessons written as [marimo](https://marimo.io) notebooks.

Covering NumPy, pandas, Matplotlib, working with APIs (`requests`, `urllib`), and parsing HTML with Beautiful Soup.

Prerequisites: basic Python (loops, dicts, functions).

## Quickstart

Clone repo & install dependencies:

```bash
git clone https://github.com/deadbytesus/data-science-basic-tutorial
cd data-science-basic-tutorial

pip install -r requirements.txt

```

Start your lessons with marimo:

```bash
marimo edit

```

## Lessons

| Topic | File |
| --- | --- |
| NumPy arrays | `lesson_numpy.py` |
| Tables with pandas | `lesson_pandas.py` |
| Charts with Matplotlib | `lesson_matplotlib.py` |
| HTTP with `requests` | `lesson_requests.py` |
| HTTP with `urllib` | `lesson_urllib.py` |
| HTML with Beautiful Soup | `lesson_beautiful_soup.py` |

The HTTP lessons cover standard methods (GET, POST, PUT, PATCH, DELETE) plus the new `QUERY` method ([RFC 10008](https://www.rfc-editor.org/rfc/rfc10008)).

```