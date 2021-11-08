

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm, NoteForm


# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html", {"albums": albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    form = NoteForm()
    return render(
        request,
        "albums/album_detail.html",
        {"album": album, "pk": pk, "form": form},
    )


def add_album(request):
    if request.method == "GET":
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="list_albums")

    return render(request, "albums/add_album.html", {"form": form})


def edit_album(request, album_pk):
    album = get_object_or_404(album, pk=album_pk)
    if request.method == "GET":
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to="list_albums")

    return render(
        request, "albums/edit_album.html", {"form": form, "album": album}
    )


def delete_album(request, pk):
    album = get_object_or_404(album, pk=pk)
    if request.method == "POST":
        album.delete()
        return redirect(to="list_albums")

    return render(request, "albums/delete_album.html", {"album": album})


def add_note(request, album_pk):
    # get the associated album
    album = get_object_or_404(album, pk=album_pk)
    # We need a form!

    form = NoteForm(data=request.POST)
    if form.is_valid():
        note = form.save(
            commit=False
        )  # this step lets us save the object, but NOT to rhe database yet!
        note.album = album  # that's so we can do THIS step, associating the note with the album
        note.save()  # here is where we save the note with the relationship to album and everything!
        return redirect(to="album_detail", pk=album.pk)

    return render(
        request, "albums/album_detail.html", {"note_form": form, "album": album}
    )