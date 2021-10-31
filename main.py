import tinder
import bumble
import argparse
import utils

parser = argparse.ArgumentParser()
parser.add_argument('--headless', default=False)
args = parser.parse_args()

HEADLESS = args.headless

if __name__ == '__main__':
    bumble = bumble.Bumble()
    tinder = tinder.Tinder()

    bumble.autoswipe(headless=HEADLESS)
    tinder.autoswipe(headless=HEADLESS)

    utils.print_statistics(bumble.LEFT, bumble.RIGHT, bumble.MATCH, tinder.LEFT, tinder.RIGHT, tinder.MATCH)
