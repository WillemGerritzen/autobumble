from sys import platform, exit


def _check_os():
    if platform != 'linux' and platform != 'win32':
        print('This bot works only on Windows and Linux machines')
        exit(0)

    return platform
