# -*- coding:utf-8 -*-


from textblob import TextBlob
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def basic_sentiment_analysis():
    testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
    print testimonial.sentiment

def tokenizatio_test():
    para = "Get the official YouTube app for Android phones and tablets. See what the world is watching -- from the hottest music videos to what’s trending in gaming, entertainment, news, and more. Subscribe to channels you love, share with friends, and watch on any device."
    para += "With a new design, you can have fun exploring videos you love more easily and quickly than before. Just tap an icon or swipe to switch between recommended videos, your subscriptions, or your account. You can also subscribe to your favorite channels, create playlists, edit and upload videos, express yourself with comments or shares, cast a video to your TV, and more – all from inside the app."

    # zen = TextBlob("Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex.")
    zen =  TextBlob(para)

    # word
    print zen.words
    # sentences
    print zen.sentences
    for sentence in zen.sentences:
        print(sentence.sentiment)

if __name__ == '__main__':
    tokenizatio_test()