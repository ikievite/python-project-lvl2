# GenDiff

utility that determines the difference between two data structures.

[![MyWorkflowCI](https://github.com/ikievite/python-project-lvl2/workflows/ci/badge.svg)](https://github.com/ikievite/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/306bf34be6c2e0d53560/maintainability)(https://codeclimate.com/github/ikievite/python-project-lvl2/maintainability)]
[![Test Coverage](https://codeclimate.com/github/ikievite/python-project-lvl2/test_coverage)](https://api.codeclimate.com/v1/badges/306bf34be6c2e0d53560/test_coverage)
[![Actions Status](https://github.com/ikievite/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/ikievite/python-project-lvl2/actions)

Features:
 - supports different input formats: yaml, json
 - generating a report in plain text, stylish and json formats

SYNOPSIS  
    gendiff [OPTION]... FILES

Mandatory positional arguments:  
    first_file
    second_file

Optional arguments:  
   - -h, --help  
    display help and exit  
   - -f, --format  
    set output format, posible fornats: stylish, plain, json (default: stylish)  

Example: Run gendiff
[![asciicast](https://asciinema.org/a/3awsblJyEGmNEYiJYq6NY7voT.svg)](https://asciinema.org/a/3awsblJyEGmNEYiJYq6NY7voT)

Asciinema with comparing files with nested structures
[![asciicast](https://asciinema.org/a/vMdODVUkX1TNnkWEAczEEHQYj.svg)](https://asciinema.org/a/vMdODVUkX1TNnkWEAczEEHQYj)

Asciinema that shows how plain and json formaters works
[![asciicast](https://asciinema.org/a/5OgZMiAfUxOpnXkHHvvZpfKRM.svg)](https://asciinema.org/a/5OgZMiAfUxOpnXkHHvvZpfKRM)


