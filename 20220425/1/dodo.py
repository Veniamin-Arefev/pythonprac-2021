DOIT_CONFIG = {'default_tasks': ['babel', 'test', 'wheel', 'sdist']}
domain = "task"
podir = "task"

def task_babel():
    """Update and compile translation"""
    return {
        "actions": [f"pybabel extract -o {podir}/{domain}.pot --input-dirs=.",
                    f"pybabel update -l ru -D {domain} -i {podir}/{domain}.pot -d {podir}",
                    f"pybabel compile -l ru -D {domain} -d {podir}"],
        "file_dep": ["task.py"],
        'targets': [f'{podir}/{domain}.pot', f'{podir}/ru/LC_MESSAGES/{domain}.mo'],
        "clean": True,
    }

def task_test():
    """Run tests"""
    return {
        "actions": ["python3 -m unittest -v"],
    }

def task_wheel():
    """Build a wheel"""
    return {
        "actions": ["python3 -m build -w"],
        "file_dep": ["task.py", f"{podir}/ru/LC_MESSAGES/{domain}.mo"],
        "targets": ["dist/task-0.0.1-py3-none-any.whl"]
    }

def task_sdist():
    """Build a cdist"""
    return {
        "actions": ["python3 -m build -s"],
        "file_dep": ["task.py", f"{podir}/ru/LC_MESSAGES/{domain}.mo"],
        "targets": ["dist/prog-0.0.1.tar.gz"]
    }

def task_cleanup():
    """Remove all"""
    return {
        "actions": [f"rm {podir}/{domain}.pot",
                    f"rm {podir}/ru/LC_MESSAGES/{domain}.mo"]
    }