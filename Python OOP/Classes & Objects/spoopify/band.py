from spoopify.album import Album
from spoopify.song import Song


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for name in self.albums:
            if name.name == album_name:
                if name.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(name)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = "\n".join(album.details() for album in self.albums)
        return f"Band {self.name}\n" + result
