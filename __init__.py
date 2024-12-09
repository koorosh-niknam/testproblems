import check50
import check50.py
@check50.check()
def exists():
    """degrees.py exists."""
    check50.exists("degrees.py")

@check50.check(exists)
def compiles():
    """degrees.py compiles."""
    check50.compile("degrees.py")

