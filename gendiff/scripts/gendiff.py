

import argparse


# Docstring


def main():
    # Docstring
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', action='store')
    parser.add_argument('second_file', action='store')
    parser.add_argument('-f', '--format', action='store', help='set format of output')
    args = parser.parse_args()


if __name__ == '__main__':
    main()
