DOIT_CONFIG = {
    'default_tasks': ['extract', 'update', 'compile', 'test', 'wheel', 'sdist', 'cleanup']
}

def task_extract():
    """
    Extract the translation.
    """
    return {
        "actions": ["pybabel extract -o po/eq.pot eq"],
        "targets": ["po/eq.pot"]
    }

def task_update():
    """
    Update the translation.
    """
    return {
        "actions": ["pybabel update -D eq -i po/eq.pot -d po -l ru",
                    "pybabel update -D eq -i po/eq.pot -d po -l en"],
        "file_dep": ["po/eq.pot"],
        "targets": ["po/ru/LC_MESSAGES/eq.po"]
    }

def task_compile():
    """
    Compile the translation.
    """
    return {
        "actions": ["pybabel compile -D eq -d po -l ru",
                    "pybabel compile -D eq -d po -l en"],
        "targets": ["po/ru/LC_MESSAGES/eq.mo"]
    }

def task_test():
    """
    Test the module.
    """
    return {
        "actions": ["python3 -m tests"]
    }

def task_wheel():
    """
    Build the wheel.
    """
    return {
        "actions": ["python3 -m build -w"],
        "file_dep": ["eq", "po/ru/LC_MESSAGES/eq.mo"],
        "targets": ["dist/eq-0.0.1-py3-none-any.whl"]
    }

def task_sdist():
    """
    Build a sdist.
    """
    return {
        "actions": ["python3 -m build -s"],
        "file_dep": ["eq", "po/ru/LC_MESSAGES/eq.mo"],
        "targets": ["dist/eq-0.0.1.tar.gz"]
    }

def task_cleanup():
    """
    Remove extra files.
    """
    return {
        "actions": ["rm po/eq.pot",
                    "rm po/ru/LC_MESSAGES/eq.mo"]
    }