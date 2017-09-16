import argparse
from pathlib import Path


def find(args):
    start_path=Path(args.start[0])

    #If -name
    if args.name and not args.type:
        for f in start_path.rglob(args.name):
            find_print(f, args)

    #If -type
    elif args.type:
        if args.type in ['d','f']:
            for f in start_path.rglob(args.name or '*'):
                if args.type == 'd' and f.is_dir():
                    find_print(f, args)
                elif args.type == 'f' and f.is_file():
                    find_print(f, args)

        else:
            print(f'Unknow type: {args.type}')

    #Else All of file
    else:
        for f in start_path.rglob('*'):
            print(f)

def find_print(f, args):
    if args.print:
        print(f"./{f}")
    else:
        print(f)

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('start', type=str, nargs=1)
    parser.add_argument('-name', type=str)
    parser.add_argument('-type', type=str)
    parser.add_argument('-print', action='store_true')

    return parser.parse_args()


find(parse_args())
