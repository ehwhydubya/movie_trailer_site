import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
    "A story of a boy and his toys that come to life",
    "http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg",
    "https://youtu.be/KYz2wyBy3kc")


avatar = media.Movie("Avatar",
    "A marine on an alien planet",
    "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
    "https://youtu.be/5PSNL1qE6VY")


head_of_state = media.Movie("Head of State",
    "A black man becomes president in 2004",
    "http://www.motherjones.com/files/imagecache/colorbox-large/photoessays/head_of_state.jpg",
    "https://www.youtube.com/watch?v=UT6ARbhTjiU")


the_x_files = media.Movie("The X-Files: Fight the Future",
    "Mulder and Scully investigate a bombing",
    "http://www.lalalandrecords.com/pix/X-Files-Fight-the-Future-hq.jpg",
    "https://youtu.be/2Dauoy3H764")

pitch_perfect = media.Movie("Pitch Perfect",
    "College girls compete in a capella",
    "http://cdn04.cdn.justjared.com/wp-content/uploads/headlines/2015/04/pitch-perfect-3-is-happening-rebel-wilson-confirms.jpg",
    "https://youtu.be/8dItOM6eYXY")

pitch_perfect_2 = media.Movie("Pitch Perfect 2",
    "College girls compete in a capella again",
    "http://images.designntrend.com/data/images/full/44154/pitch-perfect-2.jpg",
    "https://youtu.be/OgPm-yaLoyo")

movies = [toy_story, avatar, head_of_state, the_x_files, pitch_perfect, pitch_perfect_2]
fresh_tomatoes.open_movies_page(movies)
