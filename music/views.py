from atexit import register
from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Song, Rating, Album #models
from .forms import UserForm, RatingForm, AlbumForm

# Create your views here.
def default_html_view(request):
    response_content = '''
    <html>
    <head>
        <title> Hello World </title>
    </head>
    <body>
        <h1> This is a demo <h1>
    </body>
    </html>
    '''
    return HttpResponse(response_content)


def get_song_reviews(request):
    #filter
    print(request)
    if request.method == 'POST':
        context = {'name': "yes"}
        # adding user to users database
        # User.add(username="",password="")
    
    elif request.method == 'GET':
        context = {'name': request.GET}

        # getting song reviews from user

    return render(request, "forms.html", context)


def register_user(request):
    if 'register' in request.POST:
        userF = UserForm(request.POST or None)
        if userF.is_valid():
            userF.save()
        context = {
            "userF": userF,
            "userRet": userF.cleaned_data["username"]
        }
    else:
        context = {"userF": UserForm(None)}
    return context

def post_song_rating(request):
    if 'retrieve_rating' in request.POST:
        ratingF = RatingForm(request.POST or None)
        ratings = []
        if ratingF.is_valid():
            ratings = Rating.objects.filter(username=ratingF.cleaned_data["username"])
        context = {
            "ratingF": ratingF,
            "ratingRet": ratings, 
        }
    else:
        context = {"ratingF": RatingForm(None)}
    return context

def get_album_info(request):
    if 'retrieve_album' in request.POST:
        albumF = AlbumForm(request.POST or None)
        albumInfo = []
        if albumF.is_valid():
            album = albumF.cleaned_data["albumTitle"].replace(" ", "")
            artist = albumF.cleaned_data["artistName"].replace(" ", "")
            query = "{}_{}".format(album,artist)
            albumInfo = Album.objects.filter(albumArtist=query)
            
        context = {
            "albumF": albumF,
            "albumRet": albumInfo,
        }
    else:
        context = {'albumF': AlbumForm(None)}
    return context

def html_view(request):
    context = {}
    userContext = register_user(request)
    ratingContext = post_song_rating(request)
    albumContext = get_album_info(request)
    for i in userContext:
        context[i] = userContext[i]
    for i in ratingContext:
        context[i] = ratingContext[i]
    for i in albumContext:
        context[i] = albumContext[i]
    return render(request,'forms.html',context)