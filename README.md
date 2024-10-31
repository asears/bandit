```{image} https://raw.githubusercontent.com/pycqa/bandit/main/logo/logotype-sm.png
:alt: Bandit
```

______________________________________________________________________

```{image} https://github.com/PyCQA/bandit/actions/workflows/pythonpackage.yml/badge.svg?branch=main
:alt: Build Status
:target: https://github.com/PyCQA/bandit/actions?query=workflow%3A%22Build+and+Test+Bandit%22+branch%3Amain
```

```{image} https://readthedocs.org/projects/bandit/badge/?version=latest
:alt: Docs Status
:target: https://readthedocs.org/projects/bandit/
```

```{image} https://img.shields.io/pypi/v/bandit.svg
:alt: Latest Version
:target: https://pypi.org/project/bandit/
```

```{image} https://img.shields.io/pypi/pyversions/bandit.svg
:alt: Python Versions
:target: https://pypi.org/project/bandit/
```

```{image} https://img.shields.io/pypi/format/bandit.svg
:alt: Format
:target: https://pypi.org/project/bandit/
```

```{image} https://img.shields.io/badge/license-Apache%202-blue.svg
:alt: License
:target: https://github.com/PyCQA/bandit/blob/main/LICENSE
```

```{image} https://img.shields.io/discord/825463413634891776.svg
:alt: Discord
:target: https://discord.gg/qYxpadCgkx
```

A security linter from PyCQA

- Free software: Apache license
- Documentation: <https://bandit.readthedocs.io/en/latest/>
- Source: <https://github.com/PyCQA/bandit>
- Bugs: <https://github.com/PyCQA/bandit/issues>
- Contributing: <https://github.com/PyCQA/bandit/blob/main/CONTRIBUTING.md>

# Overview

Bandit is a tool designed to find common security issues in Python code. To do
this Bandit processes each file, builds an AST from it, and runs appropriate
plugins against the AST nodes. Once Bandit has finished scanning all the files
it generates a report.

Bandit was originally developed within the OpenStack Security Project and
later rehomed to PyCQA.

```{image} https://raw.githubusercontent.com/pycqa/bandit/main/bandit-terminal.png
:alt: Bandit Example Screen Shot
```

# Show Your Style

```{image} https://img.shields.io/badge/security-bandit-yellow.svg
:alt: Security Status
:target: https://github.com/PyCQA/bandit
```

Use our badge in your project's README!

using Markdown:

```
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
```

using RST:

```
.. image:: https://img.shields.io/badge/security-bandit-yellow.svg
    :target: https://github.com/PyCQA/bandit
    :alt: Security Status
```

# References

Python AST module documentation: <https://docs.python.org/3/library/ast.html>

Green Tree Snakes - the missing Python AST docs:
<https://greentreesnakes.readthedocs.org/en/latest/>

Documentation of the various types of AST nodes that Bandit currently covers
or could be extended to cover:
<https://greentreesnakes.readthedocs.org/en/latest/nodes.html>

# Container Images

Bandit is available as a container image, built within the bandit repository
using GitHub Actions. The image is available on ghcr.io:

```console
docker pull ghcr.io/pycqa/bandit/bandit
```

The image is built for the following architectures:

- amd64
- arm64
- armv7
- armv8

To pull a specific architecture, use the following format:

```console
docker pull --platform=<architecture> ghcr.io/pycqa/bandit/bandit:latest
```

Every image is signed with sigstore cosign and it is possible to verify the
source of origin using the following cosign command:

```console
cosign verify ghcr.io/pycqa/bandit/bandit:latest \
  --certificate-identity https://github.com/pycqa/bandit/.github/workflows/build-publish-image.yml@refs/tags/<version> \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
```

Where `<version>` is the release version of Bandit.

# Sponsors

The development of Bandit is made possible by the following sponsors:

```{eval-rst}
.. list-table::
   :width: 100%
   :class: borderless

   * - .. image:: https://github.githubassets.com/assets/tidelift-8cea37dea8fc.svg
          :target: https://tidelift.com/lifter/search/pypi/bandit
          :alt: Tidelift
          :width: 88

     - .. image:: https://avatars.githubusercontent.com/u/110237746?s=200&v=4
          :target: https://stacklok.com/
          :alt: Stacklok
          :width: 88

     - .. image:: https://avatars.githubusercontent.com/u/1396951?s=70&v=4
          :target: https://sentry.io/
          :alt: Sentry
          :width: 88
```

If you also ❤️ Bandit, please consider sponsoring.
