"""django_music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from albums import views as album_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", album_views.list_albums, name="list_albums"),
    path("albums/add/", album_views.add_album, name="add_album"),
    path("albums/<int:pk>/", album_views.album_detail, name="contact_detail"),
    path("albums/<int:contact_pk>/edit/", album_views.edit_album,
        name="edit_album",),
    path("albums/<int:pk>/delete/", album_views.delete_album,
        name="delete_contact",),
    path('albums/<int:contact_pk>/notes',
         album_views.add_note, name='add_note')
]


# Your app should have the following URLs. You'll need to define view functions to go along with each path. Remember, one view function can handle more than one type of request!

# | path                      | verb | purpose                                               |
# | ------------------------- | ---- | ----------------------------------------------------- | 
# | `""`                      | GET  | show a list of all the albums                         |
# | `/albums/new`             | GET  | show a form to create a new album                     |
# | `/albums/new`             | POST | create a new album                                    |
# | `/albums/<int:pk>`        | GET  | show details about a single album                     |
# | `/albums/<int:pk>/edit`   | GET  | show a form to edit a new album                       |
# | `/albums/<int:pk>/edit`   | POST | update a specific album                               |
# | `/albums/<int:pk>/delete` | GET  | show a confirmation screen to delete a specific album |
# | `/albums/<int:pk>/delete` | POST | delete a specific album                               |
