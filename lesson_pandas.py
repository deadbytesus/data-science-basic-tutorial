import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import pandas as pd

    return mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Meet pandas: Python's table toolkit

    Ever opened a spreadsheet and wanted to sort it, filter it, or total up
    a column? That's the kind of work **pandas** is built for. Its main
    object, a **DataFrame**, is a table with named columns. A single column
    is called a **Series**.

    We'll use a tiny sales table we create here, so there's no file to find
    and no setup beyond installing pandas.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Build a table and get your bearings

    Here's the sales table we'll explore. `head()` previews rows, `shape`
    gives the row and column counts, `columns` lists the labels, `info()` shows
    data types and missing values, and `describe()` summarizes numeric data.
    """)
    return


@app.cell
def _(pd):
    sales = pd.DataFrame(
        {
            "item": ["Notebook", "Pen", "Notebook", "Mug", "Pen"],
            "region": ["North", "South", "South", "North", "North"],
            "units": [3, 10, 2, 1, 7],
            "price": [4.5, 1.2, 4.5, 8.0, 1.2],
        }
    )

    sales
    return (sales,)


@app.cell
def _(sales):
    sales.head()
    return


@app.cell
def _(sales):
    sales.shape
    return


@app.cell
def _(sales):
    sales.columns
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Find the columns and rows you want

    Select one column with `sales["item"]` or several with
    `sales[["item", "units"]]`. To filter rows, put a condition inside the
    brackets, for example `sales[sales["region"] == "North"]`.
    """)
    return


@app.cell
def _(sales):
    chosen_columns = sales[["item", "units"]]
    north_sales = sales[sales["region"] == "North"]
    larger_sales = sales[sales["units"] >= 3]
    return chosen_columns, larger_sales, north_sales


@app.cell
def _(chosen_columns):
    chosen_columns
    return


@app.cell
def _(north_sales):
    north_sales
    return


@app.cell
def _(larger_sales):
    larger_sales
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Add a calculation, sort, and summarize

    `assign()` adds a calculated column. `sort_values()` changes row order.
    `groupby()` gathers rows with the same label so you can calculate a summary
    for each group. Here we'll calculate revenue and compare regions.
    """)
    return


@app.cell
def _(sales):
    enriched_sales = sales.assign(revenue=sales["units"] * sales["price"])
    revenue_by_region = (
        enriched_sales.groupby("region", as_index=False)["revenue"].sum()
    )
    sorted_sales = enriched_sales.sort_values("revenue", ascending=False)
    return enriched_sales, revenue_by_region, sorted_sales


@app.cell
def _(enriched_sales):
    enriched_sales
    return


@app.cell
def _(revenue_by_region):
    revenue_by_region
    return


@app.cell
def _(sorted_sales):
    sorted_sales
    return


@app.cell
def _(pd):
    small_table = pd.DataFrame(
        {"name": ["Ava", "Sam", "Lee"], "score": [8, None, 10]}
    )
    filled_scores = small_table.assign(
        score=small_table["score"].fillna(small_table["score"].mean())
    )
    return filled_scores, small_table


@app.cell
def _(small_table):
    small_table
    return


@app.cell
def _(filled_scores):
    filled_scores
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    1. Add a row and a calculated column to `sales`.
    2. Filter for one item and sort by units.
    3. Use `groupby()` to find total units per item.
    4. Load a CSV file and inspect it with `head()`, `shape`, and `info()`.
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
            new_sale = pd.DataFrame(
                [{"item": "Book", "region": "East", "units": 2, "price": 12.0}]
            )
            sales_with_new_row = pd.concat(
                [sales, new_sale], ignore_index=True
            )
            sales_with_revenue = sales_with_new_row.assign(
                revenue=sales_with_new_row["units"]
                * sales_with_new_row["price"]
            )
            ```
            """),
            "Solution 2": mo.md("""
            ```python
            pens = sales[sales["item"] == "Pen"].sort_values("units")
            ```
            """),
            "Solution 3": mo.md("""
            ```python
            sales.groupby("item")["units"].sum()
            ```
            """),
            "Solution 4": mo.md("""
            ```python
            my_data = pd.read_csv("data.csv")
            my_data.head()
            my_data.shape
            my_data.info()
            ```
            """),
        }
    )
    return


if __name__ == "__main__":
    app.run()
