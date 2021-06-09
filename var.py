# Import Libs
try:
    from os import environ
    import random
    import key
except Exception as e:
    exit("Exception: " + str(e))

# Define Variables
_deployment_env = True
_active_print = True


_model_arg_1 = key._model_arg_1
_model_arg_2= key._model_arg_2
_model_arg_3= key._model_arg_3

if _deployment_env:
   # Prod ENV
   # Debug
    _debug = False
    # Sleep
    _sleep_time_small = random.randint(10, 30)
    # tweepy
    _tweet_max_count = int(random.randint(200, 700))
    _tweet_limit = int(random.randint(250, 500))
    _consumer_key = environ['C_KEY']
    _consumer_secret = environ['C_SEC']
    _auth_token = environ['A_TOKEN']
    _auth_secret = environ['A_SEC']
    _mongo_uri = environ['MONGO_URI']
else:    
    # Dev ENV
    import keys
    # Debug
    _debug = True
    # Sleep
    _sleep_time_small = 0.5
    # tweepy
    _tweet_max_count = 5
    _tweet_limit = 5
    # Define Variables Keys
    _consumer_key = keys._consumer_key
    _consumer_secret = keys._consumer_secret
    _auth_token = keys._auth_token
    _auth_secret = keys._auth_secret
    _mongo_uri = keys._mongo_uri

_min_text_len = 150
_offset = int(random.randint(0, 500))

# msg
_init_msg = " Initiated !!"
_complete_msg = " Completed!!"

# databse
_db_client = "tenet"
_db_name = "dataset"
