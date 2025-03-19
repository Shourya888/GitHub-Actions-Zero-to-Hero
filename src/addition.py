# app.py
# This is a test commit
#another random comment to have the pipeline run.
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
