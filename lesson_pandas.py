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
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Build a table and get your bearings

    Here's the sales table we'll explore. `head()` shows the first five rows
    by default; pass a number, such as `sales.head(2)`, to choose how many rows
    to preview. `shape` gives the row and column counts, `columns` lists the
    labels, `info()` shows data types and missing values, and `describe()`
    summarizes numeric data.
    """)
    return


@app.cell
def _(pd):
    sales = pd.DataFrame(
        {
            "item": [
                "Notebook", "Pen", "Notebook", "Mug", "Pen", "Book",
                "Desk", "Lamp", "Chair", "Bottle", "Folder", "Marker",
            ],
            "region": [
                "North", "South", "South", "North", "North", "East",
                "West", "East", "West", "South", "North", "East",
            ],
            "units": [3, 10, 2, 1, 7, 2, 4, 3, 6, 8, 5, 9],
            "price": [
                4.5, 1.2, 4.5, 8.0, 1.2, 12.0,
                35.0, 18.5, 22.0, 7.5, 2.0, 1.5,
            ],
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
    sales.head(2)
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
    for each group. For example, `sales.groupby("item")["units"].sum()` uses
    each item name as a row label (the index). With
    `sales.groupby("item", as_index=False)["units"].sum()`, `item` stays a
    regular column instead. `as_index=False` changes where the group label
    appears; it does not change the sums.

    To add rows, `pd.concat([sales, new_sale])` stacks the rows of the two
    DataFrames. By default, it keeps their row labels: since both tables start
    at label 0, the result has a duplicate label. Use
    `pd.concat([sales, new_sale], ignore_index=True)` to give every row a fresh
    label from 0 to 12. These labels are not data columns.

    Here we'll calculate revenue and compare regions.
    """)
    return


@app.cell
def _(pd):
    example_sale = pd.DataFrame(
        [{"item": "Book", "region": "East", "units": 2, "price": 12.0}]
    )
    return (example_sale,)


@app.cell
def _(example_sale, pd, sales):
    stacked_sales = pd.concat([sales, example_sale])
    return (stacked_sales,)


@app.cell
def _(stacked_sales):
    stacked_sales
    return


@app.cell
def _(example_sale, pd, sales):
    reset_index_sales = pd.concat([sales, example_sale], ignore_index=True)
    return (reset_index_sales,)


@app.cell
def _(reset_index_sales):
    reset_index_sales
    return


@app.cell
def _(sales):
    enriched_sales = sales.assign(revenue=sales["units"] * sales["price"])
    revenue_by_region_default = (
        enriched_sales.groupby("region")["revenue"].sum()
    )
    revenue_by_region = (
        enriched_sales.groupby("region", as_index=False)["revenue"].sum()
    )
    sorted_sales = enriched_sales.sort_values("revenue", ascending=False)
    return (
        enriched_sales,
        revenue_by_region,
        revenue_by_region_default,
        sorted_sales,
    )


@app.cell
def _(enriched_sales):
    enriched_sales
    return


@app.cell
def _(revenue_by_region):
    revenue_by_region
    return


@app.cell
def _(revenue_by_region_default):
    revenue_by_region_default
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

    1. Create a one-row DataFrame with the same columns as `sales`. First
       combine it with `sales` using `pd.concat([sales, new_sale])` and inspect
       the row labels. Then use `ignore_index=True` and compare. Add a
       calculated column with `assign()`.
    2. Filter for one item and sort by units.
    3. Use `groupby()` to find total units per item. Set `as_index=False` so
       `item` stays a regular column in the result.
    4. Load the included `data.csv` file with `pd.read_csv("data.csv")`.
       Inspect it with `head()`, `head(2)`, `shape`, and `info()`. Compare
       `head()` and `head(2)`.
    """)
    return


@app.cell
def _(pd):
    # Write your answers here.
    my_data = pd.read_csv("data.csv")
    my_data.head()
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
            sales.groupby("item", as_index=False)["units"].sum()
            ```
            """),
            "Solution 4": mo.md("""
            ```python
            my_data = pd.read_csv("data.csv")
            my_data.head()
            my_data.head(2)
            my_data.shape
            my_data.info()
            ```
            """),
        }
    )
    return


if __name__ == "__main__":
    app.run()
