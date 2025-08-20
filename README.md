# SDK Stubs

This repository contains type stubs for the ArduSimple's micropython SDK, allowing type checkers and IDEs to provide autocompletion, type checking, and better developer experience.

## Installation

You can install the stubs directly from GitHub

```bash
# Install the stubs
pip install git+https://github.com/eps-works/sdk-stubs.git --target typings
```

> [!Tip]
> Use `--upgrade` and `--force-reinstall` flags to update typings

Ensure the installed stubs directory is included in your PYTHONPATH or recognized by your IDE.  
An easy set up is to configure your `pyproject.toml` to import typings.

```toml
[tool.pyright]
exclude = ["typings"]
extraPaths = ["src", "typings"]

[tool.pylint]
ignore = ["__pycache__", ".venv", "typings"]
init-hook = "import sys; sys.path.append('typings')"
```

