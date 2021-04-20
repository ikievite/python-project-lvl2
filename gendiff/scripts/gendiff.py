

"""gendiff package."""


from gendiff.args_parser import args_parse
from gendiff.generate_diff import generate_diff
from gendiff.loader import FileTypeError
from gendiff.format_diff import FormaterError


def main():
    """Run main func."""
    args = args_parse()
    try:  # noqa: WPS229 # allow long ``try`` body length
        diff = generate_diff(args.first_file, args.second_file, args.formater)

        print(diff)  # noqa: WPS421 # allow print call
    except FormaterError as e:  # noqa: WPS111 # ignore warning about to short name
        print('Exception: {0}'.format(str(e)))  # noqa: WPS421, ignore warning about print call
    except FileTypeError as e:  # noqa: WPS111
        print('Exception: {0}'.format(str(e)))  # noqa: WPS421


if __name__ == '__main__':
    main()
