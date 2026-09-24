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


@app.function
def fibonacci(n: int) -> int:
    """
        Returns the n-th Fibonacci number 
        Contract:
        - if n = 0: 0
        - if n = 1: 1
        - otherwise: fibonacci(n-1) + fibonacci(n-2)

    """
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


@app.cell
def _():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55
    return


if __name__ == "__main__":
    app.run()
