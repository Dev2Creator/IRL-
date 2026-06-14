<div align="center">

# IRL™ 🌱
**Software for Humans.**

```text
 ╔══════════════════════╗
 ║      IRL™ 🌱         ║
 ║ Software for Humans  ║
 ╚══════════════════════╝
```

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![PyPI version](https://badge.fury.io/py/irl-pkg.svg)](https://badge.fury.io/py/irl-pkg)

</div>

`irl` is a universal package installer built natively in Python. Whether it's an NPM package, a PyPI module, or a GitHub repository, just ask `irl` to install it. It will magically figure out the registry, check your system, and give you a beautiful "Touching grass" progress bar along the way.

## Features

- **Universal Installer:** `irl install <package>`. It automatically figures out if `<package>` is on NPM, PyPI, or GitHub.
- **Doctor Diagnostics:** `irl doctor <package>` checks your dependencies, network, and storage before you install.
- **Detective Glasses:** `irl glasses <package>` peeks into a registry and tells you the version, size, and source of a package.
- **Beautiful UI:** Powered by Rich, you get buttery-smooth spinners, colored ASCII menus, and clear visual feedback.

## Installation

```bash
pip install irl-pkg
```

## Usage

```text
 👓 Glasses - See Clearly
 🩺 Doctor  - Stay Healthy
 📦 Install - Get Started
 
 Usage: irl <command> <package>
```

### Install Packages
Installs seamlessly using NPM, PIP, or direct Git clone under the hood.

```bash
# Trans Power™ App
irl install transpower

# Direct internet downloads (auto-extracts ZIP/TAR files)
irl install https://example.com/package.zip
irl install https://example.com/script.py

# PyPI
irl install requests

# NPM
irl install chalk

# GitHub Repo
irl install octocat/Hello-World
```

### Run Diagnostics
Make sure you are ready to install.

```bash
irl doctor chalk
```
```text
🩺 Checking package...

✅ Dependencies installed
✅ Network available
✅ Storage available

Diagnosis:
Ready for installation.
```

### Inspect Packages
Peek into the registry to see what you are getting before you download.

```bash
irl glasses requests
```
```text
👓 Looking closely...

Package: requests 
Version: 2.31.0
Source: PyPI
Install Method: pip install

Vision enhanced.
```

## Authors
© 2026 **UNKNOWN™**

## License
This project is licensed under the **AGPL-3.0 License** - see the `LICENSE` file for details.
