from design.banner import get_banner
from design.clear import clear
from src.finder import finder 
import argparse


def main():
    clear()
    get_banner()

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help='Target URL to perform Velkan', type=str)
    parser.add_argument('-w', '--wordlist', help='The Wordlist', type=str,)
    args = parser.parse_args()

    finder(args)


if __name__ == "__main__":
    main()
