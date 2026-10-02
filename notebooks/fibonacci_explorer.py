import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    from collections import Counter

    from fibonacci_kata import fibonacci

    return fibonacci, mo, plt


@app.cell
def _(mo):
    mo.md(r"""
    # Fibonacci Explorer

    Pick a range below and see the Fibonacci number for each value
    in it, both as a list and as a chart of the distribution of
    outputs. This notebook consumes the published fibonacci_kata
    package — it does not reimplement the function.
    """)
    return


@app.cell
def _(mo):
    start = mo.ui.slider(
        0,
        20,
        value=0,
        label="Range start",
    )

    end = mo.ui.slider(
        0,
        20,
        value=10,
        label="Range end",
    )

    mo.hstack([start, end])
    return end, start


@app.cell
def _(end, fibonacci, start):
    lo, hi = sorted((start.value, end.value))

    results = [fibonacci(n) for n in range(lo, hi + 1)]

    results
    return (results,)


@app.cell
def _(plt, results):
    fig, ax = plt.subplots()

    ax.bar(
        range(len(results)),
        results,
        color="#4c72b0",
    )

    ax.set_xlabel("n")
    ax.set_ylabel("Fibonacci value")
    ax.set_title("Fibonacci values over the selected range")

    fig
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
