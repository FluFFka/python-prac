DOIT_CONFIG = {
    'default_tasks': ['extract', 'update', 'compile', 'test']
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
