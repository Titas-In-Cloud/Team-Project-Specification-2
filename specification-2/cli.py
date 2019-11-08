import argparse

def image_storage(args):
    import image_storage

def cli():
    parser = argparse.ArgumentParser(prog = "image_manipulator", usage = "%(prog)s [options]")

    subparsers = parser.add_subparsers(help = "Sub Command Help")

    subparsers.add_parser("storage").set_defaults(func = image_storage)

    args = parser.parse_args()

    args.func(args)
