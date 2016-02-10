import pytest
import media

default_args = {"movie_title": "Head of State",
                "movie_storyline": "A black man becomes president in 2004",
                "poster_image": "http://www.motherjones.com/files/imagecache/colorbox-large/photoessays/head_of_state.jpg",
                "trailer_youtube_url": "https://www.youtube.com/watch?v=UT6ARbhTjiU"}


@pytest.fixture
def movie():
    return media.Movie(**default_args)

# tests for correct output for no actors in arguments


def test_empty_actors_list_output(movie):
    assert "no actors to list" in movie.list_actors()
