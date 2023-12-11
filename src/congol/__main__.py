import sys
from congol import pattern, views
from congol.cli import get_command_line_args


def main() -> None:
    args = get_command_line_args()
    View = getattr(views, args.view)
    if args.all:
        for p in pattern.instantiate_all_patterns():
            _show_pattern(View, p, args)
    else:
        _show_pattern(
            View,
            pattern.Pattern.from_toml(name=args.pattern),
            args
        )


def _show_pattern(View, pattern, args):
    try:
        View(
            pattern=pattern,
            gen=args.gen,
            frame_rate=args.fps,
            bounds=(0, 40, 0, 40)
        ).show()
    except Exception as error:
        print(error, file=sys.stderr)


if __name__ == "__main__":
    main()