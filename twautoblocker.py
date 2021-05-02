
import tweepy as tw
import time
import argparse
import json
import pickle
from itertools import zip_longest
import os

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def get_followers(store_file):
    followers = []
    for page in tw.Cursor(api.followers_ids).pages():
        followers.extend(page)
        time.sleep(5)

    print('Retrieved ' + str(len(followers)) + ' ids.')
    # save it just in case
    outfile = open(store_file, 'wb')
    pickle.dump(followers,outfile)
    print('Follower list pickled.')

    for follower in followers:
        print(follower)


def suspiciuos_name(username):
    ## for now, name suspicious if has more than 4 numbers
    return (sum(c.isdigit() for c in username) > 4)

def filter_users(ids_listfile, api):

    infile = open(ids_listfile, 'rb')
    id_list = pickle.load(infile)
    infile.close()

    users_blocked = 0
    users_checked = 0
    groups100 = grouper(id_list, 100)
    for ids in groups100:
        results = api.lookup_users(user_ids=ids)
        for user in results:
            block = False

            ## criteria to clock (needs to be updated)
            block = (user.created_at.year > 2020) and suspiciuos_name(user.screen_name)
            block = block or (suspiciuos_name(user.screen_name) and (user.followers_count < 30))
            block = block and (not user.verified)

            if block:
                print('Eliminado: ' + user.screen_name + '\t(followers: ' + str(user.followers_count) +', creado: ' + str(user.created_at) + ')')
                api.create_block(user_id=user.id)
                ## unblocking after blocking means just eliminating from the followers list
                api.destroy_block(user_id=user.id)
                users_blocked+=1

            users_checked+=1

        print('Users checked: ' + str(users_checked) + '. Blocked: ' + str(users_blocked))
        time.sleep(10)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    parser = argparse.ArgumentParser('twautoblocker')
    parser.add_argument('--credenciales', help="Archivo de credenciales.", default='credenciales.json')
    parser.add_argument('--store_file', help="Archivo opcional para almacenar todas los follower ids.", default='followers.pkl')
    args = parser.parse_args()

    if not os.path.exists(args.credenciales):
        print('No se encuentra el archivo: ' + str(args.credenciales))
        quit()

    credenciales = json.load(open(args.credenciales, 'r'))
    auth = tw.OAuthHandler(credenciales['tw_apikey'], credenciales['tw_secretkey'])
    auth.set_access_token(credenciales['tw_access_token'], credenciales['tw_access_token_secret'])
    api = tw.API(auth, wait_on_rate_limit=True)

    store_file = args.store_file
    if not os.path.exists(store_file):
        get_followers(store_file)

    filter_users(store_file, api)