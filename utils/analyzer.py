import subprocess
import tempfile
import os
import black

def run_tool(command, code):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
        tmp.write(code.encode())
        tmp_path = tmp.name

    result = subprocess.run(command + [tmp_path], capture_output=True, text=True)
    os.unlink(tmp_path)
    return result.stdout

def run_flake8(code):
    return run_tool(["flake8"], code)

def run_bandit(code):
    return run_tool(["bandit", "-q"], code)

def run_radon(code):
    return run_tool(["radon", "cc"], code)

def format_code(code):
    try:
        return black.format_str(code, mode=black.FileMode())
    except:
        return code
