from sys import platform, exit


def _check_os():
    if platform != 'linux' and platform != 'win32':
        print('This bot works only on Windows and Linux machines')
        exit(0)

    return platform


def print_statistics(bleft, bright, bmatch, tleft, tright, tmatch) -> None:

    print('\n========================')
    print('Swiping complete')
    print('========================\n')

    print(f'\tResults:\n\n\t\tBumble:\n\n\t\t\tRight swipes: {bright}\n\n\t\t\tLeft swipes: {bleft}\n\n\t\t\tMatches: {bmatch}\n\n\t\tTinder:\n\n\t\t\tRight swipes: {tright}\n\n\t\t\tLeft swipes: {tleft}\n\n\t\t\tMatches: {tmatch}')


if __name__ == '__main__':
    print_statistics(1,1,1,1,1,1)
