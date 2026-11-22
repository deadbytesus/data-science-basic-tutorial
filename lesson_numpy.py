import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import numpy as np

    return mo, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Let's work with NumPy arrays

    NumPy is a library that helps Python work with numbers. Its main tool is
    the **array**: a collection of values that you can calculate with all
    at once.

    Python lists are great for many jobs. When your data is mostly numbers,
    NumPy makes common calculations much simpler. Let's see how.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Make an array and take a look

    `np.array()` turns a Python list into a NumPy array. `np.zeros()` makes an
    array of zeros, and `np.arange()` makes a sequence of numbers. Arrays also
    tell you their dimensions, shape, element type, and size.
    """)
    return


@app.cell
def _(np):
    temperatures = np.array([18.0, 20.5, 19.0, 22.0, 21.5])
    days = np.arange(1, 6)
    zeros = np.zeros(3)
    return days, temperatures, zeros


@app.cell
def _(temperatures):
    temperatures


@app.cell
def _(days):
    days


@app.cell
def _(zeros):
    zeros


@app.cell
def _(temperatures):
    temperatures.ndim


@app.cell
def _(temperatures):
    temperatures.shape


@app.cell
def _(temperatures):
    temperatures.dtype


@app.cell
def _(temperatures):
    temperatures.size


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Do the same calculation on every value

    NumPy applies arithmetic to every value in an array. This is called
    **vectorization**. You can scale, shift, and summarize a whole collection
    without writing a loop.
    """)
    return


@app.cell
def _(np):
    original = np.array([2, 4, 6, 8])
    return (original,)


@app.cell
def _(original):
    original


@app.cell
def _(original):
    original * 2


@app.cell
def _(original):
    original + 10


@app.cell
def _(np, original):
    np.mean(original)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Pick out the values you need

    Array positions start at zero, just like in a Python list. A slice such as
    `array[:2]` selects the first two values. A condition creates a boolean
    mask, which you can use to filter the array.
    """)
    return


@app.cell
def _(np):
    measurements = np.array([12.1, 15.4, 9.8, 18.2, 14.0])
    return (measurements,)


@app.cell
def _(measurements):
    measurements[:2]


@app.cell
def _(measurements):
    measurements[measurements >= 14]


@app.cell
def _(measurements, np):
    np.round((measurements - 32) * 5 / 9, 1)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Work with rows and columns

    A two-dimensional array arranges values into rows and columns. The `axis`
    argument tells NumPy which direction to combine: `axis=0` works down the
    rows (one result per column), while `axis=1` works across the columns (one
    result per row). The next cells show the array, then its column and row
    totals.
    """)
    return


@app.cell
def _(np):
    grid = np.array([[1, 2, 3], [4, 5, 6]])
    return (grid,)


@app.cell
def _(grid):
    grid


@app.cell
def _(grid, np):
    np.sum(grid, axis=0)


@app.cell
def _(grid, np):
    np.sum(grid, axis=1)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Practice

    1. Create an array of five prices and calculate the total and mean.
    2. Select values greater than a threshold using a boolean mask.
    3. Make a 2D array and inspect its `shape`.
    4. Try `np.min`, `np.max`, and `np.std` on a numeric array.
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
            prices = np.array([2.5, 3.0, 4.25, 5.0, 6.5])
            prices.sum()
            prices.mean()
            ```
            """),
            "Solution 2": mo.md("""
            ```python
            values = np.array([2, 5, 8, 3, 10])
            threshold = 5
            values[values > threshold]
            ```
            """),
            "Solution 3": mo.md("""
            ```python
            table = np.array([[1, 2, 3], [4, 5, 6]])
            table.shape
            ```
            """),
            "Solution 4": mo.md("""
            ```python
            np.min(prices)
            np.max(prices)
            np.std(prices)
            ```
            """),
        }
    )


if __name__ == "__main__":
    app.run()
