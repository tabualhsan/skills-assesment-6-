import pytest
import os
import sys
import importlib
from pathlib import Path


DIRECTORIES = [p for p in os.listdir() 
                if Path(p).is_dir() 
                and not p.startswith('__') 
                and not p.startswith('.')
                and not p.endswith('env')
            ]


@pytest.fixture(scope="module", params=DIRECTORIES)
def ll_module(request):
    sys.path.append(request.param)
    import linkedlist
    try:
        importlib.reload(linkedlist)
        yield linkedlist
    except Exception as e:
        pytest.skip(f"Could not import {request.param} due to {e}")
    finally:
        sys.path.remove(request.param)

@pytest.fixture(scope="module", params=DIRECTORIES)
def tree_module(request):
    sys.path.append(request.param)
    import tree
    try:
        importlib.reload(tree)
        yield tree
    except Exception as e:
        pytest.skip(f"Could not import {request.param} due to {e}")
    finally:
        sys.path.remove(request.param)


# Runtime is a discussion question section at this time. 
# Can we figure out a way to automate their answers?
# Perhaps feed that into a Google Form or something?

       