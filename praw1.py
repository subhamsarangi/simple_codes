import praw
import sys

reddit = praw.Reddit(client_id = 'p_OIb2EBrWir6w', client_secret='ZNBPZpMHJ0jjZZjUqpfF3_yRrWU', username = '_pythonreddit_', password = 'cookies', user_agent = 'praw1')
print(reddit.user.me())

subreddit = reddit.subreddit('todayilearned')

print(subreddit.display_name)  # Output: redditdev
print(subreddit.title)         # Output: reddit Development
# print(subreddit.description)   # Output: A subreddit for discussion of ...
# subreddit.subscribe()

def get_submission():
    hot_python = subreddit.hot(limit=3)
    for submission in hot_python:
        if not submission.stickied:
            print('\nTitle: {},\n ups: {}, down: {}, Have we visited: {}'.format(submission.title, submission.ups, submission.downs, submission.visited))
            print(submission.author.name,submission.author.link_karma)
            print('URL: ',submission.url)
#            get_comments(submission)

def get_comments(sm):
    sm.comments.replace_more(limit=0)
    print(30*'_')
    for comm in sm.comments:
        # print('Parent ID:', comm.parent())
        print('Comment ID:', comm.id)
        try:
            print(comm.body)
        except UnicodeEncodeError:
            print(comm.body.encode('utf8').decode(sys.stdout.encoding))
        # get_replies(comm)
        print(20*'_')

def get_replies(cm):
    if len(cm.replies) > 0:
        for reply in cm.replies:
            try:
                print('[-]REPLY by',reply,'>' ,reply.body)
            except UnicodeEncodeError:
                print('[-]REPLY by',reply,'>' ,reply.body.encode('utf8').decode(sys.stdout.encoding))

get_submission()
