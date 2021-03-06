import argparse

def image_storage(args):
    import image_storage

def print_list_of_stored_pictures(args):
    import list_of_stored_pictures

def JPEG_thumbnail_creation(args):
    import thumbnail_creation

def image_filters(args):
    import image_filters

def cli():
    parser = argparse.ArgumentParser(prog = "image_manipulator", usage = "%(prog)s [options]")

    subparsers = parser.add_subparsers(help = "Sub Command Help")

    subparsers.add_parser("storage").set_defaults(func = image_storage)
    subparsers.add_parser("list").set_defaults(func = print_list_of_stored_pictures)
    subparsers.add_parser("thumbnail").set_defaults(func = JPEG_thumbnail_creation)
    subparsers.add_parser("filters").set_defaults(func = image_filters)

    parser.add_argument("--storage", help = "lets user choose what pictures to modify")
    parser.add_argument("--list", help = "gives a list of chosen pictures for modification")
    parser.add_argument("--thumbnail", help = "converts chosen pictures to JPEG "
                                            "thumbnails and saves them")
    parser.add_argument("--filters", help = "lets user modify and apply filters "
                                          "to chosen pictures")

    args = parser.parse_args()

    args.func(args)
