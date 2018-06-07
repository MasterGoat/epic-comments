#!/usr/bin/python

import praw
import time
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

SUBREDDIT_NAME = "FortniteBRTest"
AUTHOR_FLAIR = "epic"
BOT_USERNAME = "EpicCommentBot"


def __init__(self):

    self.conf = ConfigParser()
    self.reddit = None

    os.chdir(sys.path[0])
    if os.path.exists('conf.ini'):
        self.conf.read('conf.ini')
    else:
        raise FileNotFoundError('Config file, conf.ini, was not found.')

    if self.conf.get('log', 'logging') == 'False':
        self.logging = False
    else:
        self.logging = True

    self.login()

def login(self):

    app_id = self.conf.get('app', 'app_id')
    app_secret = self.conf.get('app', 'app_secret')
    user_agent = self.conf.get('app', 'user_agent')

    if self.conf.get('app', 'auth_type') == 'webapp':
        token = self.conf.get('auth-webapp', 'token')
        self.reddit = praw.Reddit(client_id=app_id,
                                  client_secret=app_secret,
                                  refresh_token=token,
                                  user_agent=user_agent)
    else:
        username = self.conf.get('auth-script', 'username')
        password = self.conf.get('auth-script', 'passwd')
        self.reddit = praw.Reddit(client_id=app_id,
                                  client_secret=app_secret,
                                  username=username,
                                  password=password,
                                  user_agent=user_agent)
            
    print(self.reddit.user.me())


def bot_run(reddit, subreddit)
    for new_comment in subreddit.stream.comments():
        if AUTHOR_FLAIR.lower() in str(new_comment.author_flair_text).lower():
            comment_reply = ""
            bot_comment_id = 0
            counter = 0
            new_comment.submission.comments.replace_more(limit=None)
            for s_comment in new_comment.submission.comments.list():
                if s_comment.author.name == BOT_USERNAME:
                    bot_comment_id = s_comment.id
                if AUTHOR_FLAIR.lower() in str(s_comment.
                                               author_flair_text).lower():
                    counter += 1
                    comment_reply += "[COMMENT #" + str(counter)\
                        + " - " + s_comment.author.name + "]"\
                        + "(https://www.reddit.com" + s_comment.permalink\
                        + ")\n\n"
            if bot_comment_id == 0:
                bot_comment = new_comment.submission.reply(comment_reply)
                bot_comment.mod.distinguish(sticky=True)
                print("Creating bot's sticky comment:",
                      new_comment.submission.title, time.ctime())
            else:
                reddit.comment(bot_comment_id).edit(comment_reply)
                print("Editing bot's sticky comment:",
                      new_comment.submission.title, time.ctime())
    

reddit = login(self)
subreddit = reddit.subreddit(SUBREDDIT_NAME)
bot_run(reddit, subreddit)
