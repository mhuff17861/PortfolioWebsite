/* @Overview

  This module establishes the models used for the music player.

*/

/* @class
This class defines the model for Songs.

*/
class Song {
  /* @var an unique ID for the song */
  id;
  /* @var the title of the song */
  title;
  /* @var a song description */
  description;
  /* @var the price of the song */
  price;
  /* @var the files associated with the song for playing */
  files;

  constructor(song_json) {
    this.id = song_json.id;
    this.title = song_json.title;
    this.description = song_json.description;
    this.price = song_json.price;
    this.files = Song.format_files(song_json.song_files);
  }

  /* @function
  This function takes a file array and returns a sorted version of that array
  based on file extensions, in the order considered best for web playback.

  Args
  -------------

  - file_array: An array of file names/file paths with file extensions included.
  */
  static format_files(files_array) {
    //preferred web order for files to be played in
    const sortingArr = ['oga', 'ogg', 'webm', 'aac', 'mp3', 'flac', 'wav'];

    return files_array.slice().sort(function(a, b){
      return sortingArr.indexOf(Song.get_file_extension(a)) - sortingArr.indexOf(Song.get_file_extension(b));
    });
  }

  /* @function
  This function takes a file path and returns the file extension.

  Args
  -------------

  - file_path: File path from which the extension will be found.
  */
  static get_file_extension(file_path) {
    return file_path.slice(file_path.lastIndexOf('.') + 1, file_path.length);
  }
}

/* @class
This class defines a read-only model for Albums.

Members
-------------

- id - an unique ID for the album
- title - the title of the song
- description - a song description
- price - the price of the song
- songFiles - the files associated with the song for playing
*/
class Album {
  /* @var an unique ID for the song */
  id;
  /* @var the title of the album */
  title;
  /* @var the album's cover image */
  coverImage;
  /* @var the album type */
  type;
  /* @var the album's release date */
  releaseDate;
  /* @var description of the album */
  description;
  /* @var the price of the album */
  price;
  /* @var list of album tracks. Is an array of Song objects */
  tracks;

  /* @constructor
  This constructor takes in album data in json format and
  formats it properly for use.
  */
  constructor(album_json) {
    this.id = album_json.id;
    this.title = album_json.title;
    this.coverImage = album_json.cover_image;
    this.type = Album.format_type(album_json.type);
    this.releaseDate = album_json.release_date;
    this.description = album_json.description;
    this.price = album_json.price;
    this.tracks = Album.format_tracks(album_json.tracks);
  }

  //**** Static Functions*****

  /* @function
  This static function takes a album type and converts it into a
  human readable form.

  Args
  ---------

  - type - a type as formatted via the API.
  */
  static format_type(type) {
    if (type == "S") {
      return "Single";
    } else if (type == "A") {
      return "Album";
    } else if (type == "EP" || type == "LP") {
      return type;
    } else {
      return "Collection";
    }
  }

  /* @function
  This static function takes an album's tracks and converts them into a
  form better setup for the music player.

  Args
  ---------

  - tracks - the album tracks as given by the API.
  */
  static format_tracks(tracks) {
    tracks = tracks.sort((a, b) => parseInt(a.track_num) - parseInt(b.track_num));
    let formattedTracks = [];
    for (const track of tracks) {
      formattedTracks.push(new Song(track.song_info));
    }

    return formattedTracks;
  }

  /* @function
  Returns a track based on the given index. Throws a RangeError if the index
  is out of range.

  Args
  ---------

  - index - Index of the desired track.
  */
  get_track_by_index(index) {
    if (Number.isInteger(index) && index < tracks.length && index >= 0) {
      return tracks[index];
    } else {
      throw new RangeError(`Track does not exist at ${index}`);
    }
  }
}
