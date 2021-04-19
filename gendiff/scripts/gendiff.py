

"""gendiff package."""


from gendiff.args_parser import args_parse
from gendiff.generate_diff import generate_diff


def main():
    """Run main func."""
    args = args_parse()
    try:  # noqa: WPS229 # allow long ``try`` body length
        diff = generate_diff(args.first_file, args.second_file, args.formater)

        print(diff)  # noqa: WPS421 # allow print call
    except Exception as e:  # noqa: WPS111 # ignore warning about to short name
        print('Exception: {0}'.format(str(e)))  # noqa: WPS421, ignore warning about print call


if __name__ == '__main__':
    main()
