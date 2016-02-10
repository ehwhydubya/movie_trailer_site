# Movie Trailer Site

This repo contains python files that render a webpage with a few of my favorite movies. Exercise that's part of Udacity's Full Stack WebDev Program.

# Usage

* Create a new movie instance:

```
import media

movie_data = {"movie_title": "Head of State",
              "movie_storyline": "A black man becomes president in 2004",
              "poster_image": "http://www.motherjones.com/files/imagecache/colorbox-large/photoessays/head_of_state.jpg",
              "trailer_youtube_url": "https://www.youtube.com/watch?v=UT6ARbhTjiU"}

head_of_state = media.Movie(**movie_data)
```
