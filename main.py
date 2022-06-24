#!/usr/bin/python3
import sys
from utils import *
from time import sleep
from pypresence import Presence


def main():
    # This is the Client ID of a Rich Presence Application I made, feel free to try it or change it and make your own
    # at: https://discord.com/developers/applications
    RPC = Presence("942974252200648756")
    RPC.connect()
    try:
        while True:
            if is_playing():
                formatted_str = f"{get_artist()} - {get_title()}"
                search_str = f"{get_artist()}+{get_title()}".replace(" ", "+")
                RPC.update(state=formatted_str)
                print(f"Updated RPC Status To: {formatted_str}")
                sleep(5)
            else:
                RPC.clear()
                sys.exit()
    except KeyboardInterrupt as user_exit:
        RPC.clear()
        sys.exit()


if __name__ == '__main__':
    main()