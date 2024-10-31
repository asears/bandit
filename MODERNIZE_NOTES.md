# Modernization Notes

`October 31, 2024`

- versioning strategy needed for pyproject.toml

## Packaging

- Hatch is default for uv
- uv build to build the wheel

## Dependencies

- Migrate to pyproject.toml / lockfiles
- Dependabot?
- sarif-om, jschema-to-python are not maintained?  Last updates 2019.
- fixtures last updated May 2023

## Tox.ini

- tox.ini conversion needed

## Dockerfile

- Github Codespaces for dockerfile?
- vscode workspace for recommended extensions?

## Documentation

- Markdown instead of rst?
- rst2myst convert **/*.rst failed on 1 file see rst2myst_convert_results.txt

## Ruff Formatter

- ruff check / ruff format replaces linters (pylint, pyupgrade) and formatters (black) both need config

Recommended rule ignores:

```plaintext
tab-indentation (W191)
indentation-with-invalid-multiple (E111)
indentation-with-invalid-multiple-comment (E114)
over-indented (E117)
indent-with-spaces (D206)
triple-single-quotes (D300)
bad-quotes-inline-string (Q000)
bad-quotes-multiline-string (Q001)
bad-quotes-docstring (Q002)
avoidable-escaped-quote (Q003)
missing-trailing-comma (COM812)
prohibited-trailing-comma (COM819)
single-line-implicit-string-concatenation (ISC001)
multi-line-implicit-string-concatenation (ISC002)
```

https://docs.astral.sh/ruff/formatter/#conflicting-lint-rules

## Tests

Some tests fail on nonpriv Windows:

```shell
OSError: [WinError 1314] A required privilege is not held by the client:
```

```shell
file C:\projects\python\bandit\bandit\core\test_properties.py, line 53
  def test_id(id_val):
E       fixture 'id_val' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, class_mocker, cov, doctest_namespace, mocker, module_mocker, monkeypatch, no_cover, package_mocker, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, session_mocker, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.
```
