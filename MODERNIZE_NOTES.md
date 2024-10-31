# Modernization Notes

`October 31, 2024`

- ruff check / ruff format replaces linters (pylint, pyupgrade) and formatters (black) need config
- versioning strategy needed for pyproject.toml
- uv build to build the wheel
- tox.ini conversion needed
- Github Codespaces for dockerfile
- vscode workspace
- rst2myst convert **/*.rst failed on 1 file see rst2myst_convert_results.txt
