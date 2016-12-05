from modules import vk_friends
import argparse


def menu():
    parser = argparse.ArgumentParser(usage=' --[group] -s script --token token.\nFor example: '
                                     '--friends -s 1 --token your_token\n')

    parser.add_argument('--friends', help='Work with friends', dest='action', action='store_const',
                        const=vk_friends.choose_script)
    parser.add_argument('-s', '--script', help='Write script id. --[group] --list for getting list of scripts')
    parser.add_argument('-l', '--list', action='store_true', help='Get scripts list for this group')
    parser.add_argument('-t', '--token')

    parsed_args = parser.parse_args()
    if parsed_args.action is None:
        parser.parse_args(['-h'])
    parsed_args.action(parsed_args)