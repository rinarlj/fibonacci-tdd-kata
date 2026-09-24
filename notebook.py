import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Fibonacci Kata
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This notebook implements the Fibonacci sequence using TDD.

    The Fibonacci sequence is defined by:

    - F(0) = 0
    - F(1) = 1
    - F(n) = F(n-1) + F(n-2)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Fibonacci function implementation
    """)
    return


@app.function
def fibonacci(n: int) -> int:
    """
        Returns the n-th Fibonacci number 
        Contract:
        - if n = 0: 0
        - if n = 1: 1
        - otherwise: fibonacci(n-1) + fibonacci(n-2)

    """
    prev = 0
    cur = 1
    
    for k in range(n):
        cur, prev = cur + prev, cur


    return prev


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Unit tests
    """)
    return


@app.cell
def _():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55
    return


@app.cell
def _():
    fibonacci(10**2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Interactive marimo widget
    """)
    return


@app.cell
def _(mo):
    n_input = mo.ui.number(start=1, stop=1000, step=1, value=5, label="n")
    n_input
    return (n_input,)


@app.cell
def _(mo, n_input):
    try:
        result = fibonacci(n_input.value)
        output = mo.md(f"`fibonacci({n_input.value})` → **{result}**")
    except ValueError as e:
        output = mo.md(f"⚠️ Error: {e}")
    output
    return


if __name__ == "__main__":
    app.run()
