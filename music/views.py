
from random import randint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.shortcuts import render
from django.http import HttpResponse

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

# Create your views here.

def home(request):
    # TODO: add way to pick country
    releases = sp.new_releases(country='JP')
    items = []
    while releases:
        albums = releases['albums']
        for item in albums['items']:
            items.append(item)
        if albums['next']:
            releases = sp.next(albums)
        else:
            releases = None

    chosen = []
    for i in range(5):
        if len(items) == 0:
            break
        n = randint(0, len(items) - 1)
        chosen.append(items[n])
        del items[n]

    for i in chosen:
        print(
            f'{i["name"]} by {", ".join(list(map(lambda x: x["name"], i["artists"])))}')
        print(f'img url: {i["images"][0]["url"]}')
    context = {
        'albums': chosen,
        'title': 'home'
    }
    return render(request, 'music/home.html', context)
