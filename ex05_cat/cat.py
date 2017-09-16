import argparse


def main(args):
    line_number = 1
    for filename in args.filenames:
        file = open(filename)
        if args.numbers == True:
            for line in file.readlines():
                print(f"\t{line_number}\t{line}", end="")
                line_number+=1
        elif args.blank_non == True:
            for line in file.readlines():
                if line == "\n":
                    print(line, end="")
                else:
                    print(f"\t{line_number}\t{line}", end="")
                    line_number+=1
        else:
            print(file.read())

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('filenames', metavar='FILENAMES', type=str, nargs='+')
    parser.add_argument('-n', '--numbers', action='store_true',
            help='Number the output lines, starting at 1.')
    parser.add_argument('-b', '--blank_non', action='store_true',
            help='Number the non-blank output lines, starting at 1.')

    return parser.parse_args()


main(parse_args())
