import marimo

app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt

    return mo, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Turn your data into a picture with Matplotlib

        Numbers are useful, but a chart can make a pattern much easier to
        spot. **Matplotlib** is a Python library for drawing charts. We'll use
        its `pyplot` tools, usually imported as `plt`, to make a few common
        chart types.

        Keep one rule in mind as we go: give your chart a clear title and label
        its axes, so someone else can understand it too.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A line chart

    Use a line chart to show how a value changes over time. `plot()` draws the
    line; `set_title()`, `set_xlabel()`, and `set_ylabel()` label the chart.
    """)
    return


@app.cell
def _(plt):
    months = ["Jan", "Feb", "Mar", "Apr", "May"]
    temperatures = [4, 6, 11, 15, 20]

    line_figure, line_axes = plt.subplots()
    line_axes.plot(months, temperatures, marker="o", label="Average temperature")
    line_axes.set_title("Average temperature by month")
    line_axes.set_xlabel("Month")
    line_axes.set_ylabel("Temperature (°C)")
    line_axes.legend()
    line_axes.grid(True, alpha=0.3)
    line_figure

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A scatter plot

    A scatter plot shows the relationship between two numeric variables. Each
    dot represents one observation.
    """)
    return


@app.cell
def _(plt):
    study_hours = [1, 2, 3, 4, 5, 6]
    quiz_scores = [52, 58, 63, 72, 78, 86]

    scatter_figure, scatter_axes = plt.subplots()
    scatter_axes.scatter(study_hours, quiz_scores, color="teal")
    scatter_axes.set_title("Study time and quiz score")
    scatter_axes.set_xlabel("Study time (hours)")
    scatter_axes.set_ylabel("Quiz score (%)")
    scatter_axes.grid(True, alpha=0.3)
    scatter_figure

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A bar chart

    Use a bar chart to compare a value across categories.
    """)
    return


@app.cell
def _(plt):
    categories = ["Books", "Pens", "Mugs"]
    quantities = [12, 25, 8]

    bar_figure, bar_axes = plt.subplots()
    bar_axes.bar(categories, quantities, color=["slateblue", "darkorange", "seagreen"])
    bar_axes.set_title("Items sold")
    bar_axes.set_xlabel("Item")
    bar_axes.set_ylabel("Quantity")
    bar_figure

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A histogram

    A histogram groups numeric values into ranges (called bins) and shows how
    many values fall in each range.
    """)
    return


@app.cell
def _(plt):
    scores = [72, 81, 65, 93, 77, 85, 69, 88]

    histogram_figure, histogram_axes = plt.subplots()
    histogram_axes.hist(scores, bins=5, edgecolor="white")
    histogram_axes.set_title("Quiz score distribution")
    histogram_axes.set_xlabel("Score (%)")
    histogram_axes.set_ylabel("Number of students")
    histogram_figure

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A pattern you can reuse

    `subplots()` gives you a **Figure** (the whole image) and an **Axes** (the
    chart area). Use `plot()` for lines, `scatter()` for points, `bar()` for
    categories, and `hist()` for distributions. `savefig("chart.png")` saves
    the figure to a file. The final example makes a line chart of daily steps.
    """)
    return


@app.cell
def _(plt):
    days = [1, 2, 3, 4]
    steps = [4200, 6800, 5100, 8300]

    figure, axes = plt.subplots(figsize=(7, 4))
    axes.plot(days, steps, marker="o", color="purple")
    axes.set(title="Daily steps", xlabel="Day", ylabel="Steps")
    figure.tight_layout()

    figure
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Practice

    1. Change the line-chart values and describe how the chart changes.
    2. Add a second line and a legend label.
    3. Make a bar chart of units sold in the pandas lesson.
    4. Add a title and meaningful axis labels to every chart you create.
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
            fig, ax = plt.subplots()
            months = ["Jan", "Feb", "Mar", "Apr", "May"]
            temperatures = [3, 7, 12, 16, 22]
            ax.plot(months, temperatures)
            ax.set_title("Average temperature by month")
            ax.set_xlabel("Month")
            ax.set_ylabel("Temperature (°C)")
            fig
            ```
            The line changes to match the new temperature values.
            """),
            "Solution 2": mo.md("""
            ```python
            fig, ax = plt.subplots()
            months = ["Jan", "Feb", "Mar", "Apr", "May"]
            temperatures = [4, 6, 11, 15, 20]
            rainfall = [42, 38, 55, 61, 47]
            ax.plot(months, temperatures, marker="o", label="Temperature")
            ax.plot(months, rainfall, marker="s", label="Rainfall")
            ax.legend()
            fig
            ```
            """),
            "Solution 3": mo.md("""
            ```python
            fig, ax = plt.subplots()
            items = ["Books", "Pens", "Mugs"]
            units_sold = [12, 25, 8]
            ax.bar(items, units_sold)
            ax.set_title("Items sold")
            ax.set_xlabel("Item")
            ax.set_ylabel("Units")
            fig
            ```
            """),
            "Solution 4": mo.md("""
            ```python
            fig, ax = plt.subplots()
            days = [1, 2, 3, 4]
            steps = [4200, 6800, 5100, 8300]
            ax.plot(days, steps, marker="o")
            ax.set_title("Daily steps")
            ax.set_xlabel("Day")
            ax.set_ylabel("Steps")
            fig
            ```
            """),
        }
    )


if __name__ == "__main__":
    app.run()
