import tweepy, time, random, os
from wordnik import *

def conv(ques):
        
    booleen_ans = ['Yes', 'No', 'Calculating... Maybe', '1... Oops my binary conversion failed!', '0... Oops my binary conversion failed!']
    term_lib = ['hello', 'hi']
    name_ary = ['name', 'who are you']
    age_ary = ['age','old are you']
    gender_ary = ['gender', 'male', 'female', 'sex', 'boy', 'girl']
    booleen_ary = ['can you', 'are you', 'you\'re a', 'did you', 'do you' 'come here']
    funny_rply = ['Hello! I am a robot! I live in a web server!', '0001010010101010101010101', '404 Error', 'Hello there! Its nice to meet you!', 'Help! There are loud clicking noises and i\'m surrounded by metal!']
        
        
    num = 0
    ques = ques.lower()
            
    for x in range(0,20):
        if x + 1 <= len(name_ary) and name_ary[x] in ques and num != 1:
            return('My name is MrBot')
            num = 1

        elif x + 1<= len(age_ary) and age_ary[x] in ques and num != 1:
            return('I was made on the 22/10/2016. 10/22/2016 if you\'re an American.')
            num = 1

        elif x + 1<= len(gender_ary) and gender_ary[x] in ques and num != 1:
            return('My programer never gave me a gender. Maybe i should ask for one.')
            num = 1

        elif x + 1<= len(booleen_ary) and booleen_ary[x] in ques and num != 1:
            bool_rpl = booleen_ans[random.randint(0,len(booleen_ans)-1)]
            return(bool_rpl)
            num = 1
                      
        elif x + 1 <= len(term_lib) and term_lib[x] in ques and num != 1:
            rply = funny_rply[random.randint(0,len(funny_rply)-1)]
            return(rply)
            num = 1
                      
        elif num != 1 and x == 9:
            return('Malfunction! I don\'t know how to reply to that!')


def Reply_to_tweets():

    cwd = os.getcwd()
    path = cwd + '\\'

    CONSUMER_KEY = 'c3uHMoRbtTHCX4PQahnGSnp95'
    CONSUMER_SECRET = 'l2M1Pg7m9m8V4FL3L8oJYEwlDyGsmerxV33OWWLOYve3M9yOjw'
    ACCESS_KEY = '789727477425840128-GBe2O4XOO5piq9dpQKLy9WmhdLkGbwt'
    ACCESS_SECRET = 'cF0ZBdgRmbrZs48i5n61dvXOj0GwQLu8tD3sbdvZGvXxX'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    print('Connected!')
    for a in range(96):
        
        mentions = api.mentions_timeline(count = 5)

        for mention in mentions:
            id_data = open(path + 'the_id.txt', 'r')
            allready_rplyd = False
            ids = id_data.read().split('\n')
            status_id = mention.id_str
            
            for line in ids:
                if status_id == line:
                    allready_rplyd = True
                    
            id_data.close()
            
            if allready_rplyd != True:
                user = mention.user.screen_name
                status_text = mention.text
                response = conv(status_text)
                status = '@{0} {1}'.format(user, response)
                
                #api.update_status(status, in_reply_to_status_id = status_id)
                
                toprint = 'Tweeted: {0}'.format(status)
                print(toprint)

                id_data = open(path + 'the_id.txt', 'a')
                id_data.write(status_id + '\n') 
                id_data.close()
    print('Sleeping for 15 Minutes')
    time.sleep(15*60)

def get_wotd():
    apiUrl = 'http://api.wordnik.com/v4'
    apiKey = '57bc98e0a3f200bf47a450beaed380175142375ddc4ad9f83'
    client = swagger.ApiClient(apiKey, apiUrl)
    wordsapi = wordsapi.wordsapi(client)
    wotd = wordsapi.getWordOfTheDay()
    print(wotd.text)

get_wotd()
    
    
      




