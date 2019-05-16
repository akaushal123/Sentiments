#!/usr/bin/env python3
import helpers
import os
import sys

from analyzer import Analyzer
from termcolor import colored

def main():

    # ensure proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: ./tweets @user")

    if sys.argv[1][0] != '@':
        sys.exit("Enter the valid Twitter handle")

    # absolute paths to lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")

    # instantiate analyzer
    analyzer = Analyzer(positives, negatives)

    #getting the user's tweets
    tweets = helpers.get_user_timeline(sys.argv[1], 50)

    #checking whether tweets recieved or not
    if tweets == None:
        sys.exit("Error, Unable to access user's tweets")

    #analyzing each tweet
    for tweet in tweets:
        score = analyzer.analyze(tweet)
        if score > 0.0:
            print(colored("{} {}".format(score, tweet),"green"))
        elif score < 0.0:
            print(colored("{} {}".format(score, tweet),"red"))
        else:
            print(colored("{} {}".format(score, tweet),"yellow"))


if __name__ == "__main__":
    main()
