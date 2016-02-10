import media
import fresh_tomatoes


# setting trailer URL variables to shorten URL length for PEP8-compliance
toy_story_trailer_url = ("http://a.dilcdn.com/bl/wp-content/uploads/sites/8/"
                         "2013/02/toy_story_wallpaper_by_artifypics"
                         "-d5gss19.jpg")
# sets Toy Story instance, includes release date
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        toy_story_trailer_url,
                        "https://youtu.be/KYz2wyBy3kc",
                        release_date=1995)


avatar_trailer_url = ("http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5B"
                      "Ml5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,"
                      "1200_AL_.jpg")

# sets Avatar instance, includes release date
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     avatar_trailer_url,
                     "https://youtu.be/5PSNL1qE6VY",
                     release_date=2009)


head_of_state_trailer_url = ("http://www.motherjones.com/files/imagecache/"
                             "colorbox-large/photoessays/head_of_state.jpg")
# sets Head of State instance; basic instance
head_of_state = media.Movie("Head of State",
                            "A black man becomes president in 2004",
                            head_of_state_trailer_url,
                            "https://www.youtube.com/watch?v=UT6ARbhTjiU")

# sets The X-Files instance, includes details on all available params
the_x_files = media.Movie("The X-Files: Fight the Future",
                          "Mulder and Scully investigate a bombing",
                          "http://www.lalalandrecords.com/pix/X-Files-"
                          "Fight-the-Future-hq.jpg",
                          "https://youtu.be/2Dauoy3H764",
                          actors=["David Duchovny",
                                  "Gillian Anderson"],
                          rating="PG-13",
                          release_date=1998)

# sets Pitch Perfect instance
pitch_perfect = media.Movie("Pitch Perfect",
                            "College girls compete in a capella",
                            "http://cdn04.cdn.justjared.com/wp-content/"
                            "uploads/headlines/2015/04/pitch-perfect-3-is-"
                            "happening-rebel-wilson-confirms.jpg",
                            "https://youtu.be/8dItOM6eYXY",
                            actors=["rebel wilson", "anna kendrick"])

# sets Pitch Perfect 2 instance
pitch_perfect_2 = media.Movie("Pitch Perfect 2",
                              "College girls compete in a capella again",
                              "http://images.designntrend.com/data/images/"
                              "full/44154/pitch-perfect-2.jpg",
                              "https://youtu.be/OgPm-yaLoyo")

# list of instances
movies = [
    toy_story,
    avatar,
    head_of_state,
    the_x_files,
    pitch_perfect,
    pitch_perfect_2]

# lists actors for The X-Files, Toy Story, and Pitch Perfect if they're
# available
the_x_files.list_actors()
toy_story.list_actors()
pitch_perfect.list_actors()

# opens webpage with movies list
fresh_tomatoes.open_movies_page(movies)
