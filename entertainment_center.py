import fresh_tomatoes
import media

# formatted to meet PEP8 standards and also added break
# line to each string to make
# it more readable
memento = media.Movie("Memento",
                      "A man juggles searching for his wife's murderer "
                      "and keeping his short-term memory loss from"
                      " being an obstacle.",
                      "https://upload.wikimedia.org/wikipedia/en"
                      "/c/c7/Memento_poster.jpg",
                      "https://www.youtube.com/watch?v=0vS0E9bBSL0")


five_hundred_days_of_summer = media.Movie("500 Days of Summer",
                                          "An offbeat romantic comedy "
                                          "about a woman "
                                          "who doesn't believe true "
                                          "love exists, and "
                                          "the young man who falls for her.",
                                          "https://upload.wikimedia."
                                          "org/wikipedia/en"
                                          "/d/d1/Five_hundred_days_of_"
                                          "summer.jpg",
                                          "https://www.youtube.com/w"
                                          "atch?v=aQNs5XmdxEA")


the_wedding_singer = media.Movie("The Wedding Singer",
                                 "some dude singing at weddings",
                                 "https://upload.wikimedia.org/wikipedia"
                                 "/en/8/84/The_Wedding_Singer_film_poster.jpg",
                                 "https://www.youtube.com/watch?v=_bhU3NsCIDs")

pounds_beauty = media.Movie("200 Pounds Beauty",
                            "A talented but obese girl, who "
                            "ghost-sings for a not-so-talented "
                            "pop star, undergoes xtensive plastic "
                            "surgery to become a slender beauty "
                            "with a new identity.",
                            "https://upload.wikimedia.org/"
                            "wikipedia/en/b/b9/200poundsbeauty.jpg",
                            "https://www.youtube.com/watch?v=Ys5MuQ3U3ZU")

# It may look plenty, but this is only 4 arguments for my_sassy_girl
# separated by commas.
my_sassy_girl = media.Movie("My Sassy Girl",
                            "Based on a series of true stories "
                            "posted by Ho-sik Kim on the Internet"
                            " describing his relationship with his "
                            "girlfriend. These were later "
                            "transformed into a best-selling "
                            "book and the movie follows the book "
                            "closely. It describes the meeting of"
                            " Kyun-woo (Cha) and an unnamed girl."
                            " Kyun-woo is shamed into assisting "
                            "the girl because the other passengers"
                            " mistakenly think she is his girlfriend. "
                            "Once he helps her, Kyun-woo develops a"
                            " deep sense of responsibility for her which"
                            " enables him to tolerate (somehow) the "
                            "girl's abuses.",
                            "https://upload.wikimedia.org/wikipedia/en/"
                            "8/88/My_Sassy_Girl_Movie_Poster.jpg",
                            "https://www.youtube.com/watch?v=4lnyW3vIGvI")

windstruck = media.Movie("Windstruck",
                         "The heart-warming romance story between "
                         "Kyungjin and Myungwoo. Even though he has "
                         "passed away, he will be always with Kyungwoo "
                         "forever.",
                         "https://upload.wikimedia.org/wikipedia/en/7/"
                         "78/Windstruck_movie_poster.jpg",
                         "https://www.youtube.com/watch?v=zY2Koe3LfUo")

star_wars_ep_6 = media.Movie("Star Wars Episode VI: Return Of The Jedi "
                             "(Hayden Ending Version)",
                             "After rescuing Han Solo from the palace "
                             "of Jabba the Hutt, the rebels attempt "
                             "to destroy the second Death Star, "
                             "while Luke struggles to make Vader "
                             "return from the dark side of the Force.",
                             "https://upload.wikimedia.org/wikipedia" +
                             "/en/b/b2/ReturnOfTheJediPoster1983.jpg",
                             "https://www.youtube.com/watch?v=CsDwpF3uiZI")

goofy_movie = media.Movie("A Goofy Movie",
                          "When Max makes an preposterous promise "
                          "to a girl he has a crush on, his chances "
                          "to fulfilling it seem hopeless when he is "
                          "dragged onto a cross-country trip with his "
                          "embarrassing father, Goofy.",
                          "https://upload.wikimedia.org/wikipedia/en/f/"
                          "f3/A_Goofy_Movie_poster.jpg",
                          "https://www.youtube.com/watch?v=dHrzG5tHjJ0")

movies = [memento, five_hundred_days_of_summer, the_wedding_singer,
          pounds_beauty, my_sassy_girl, windstruck, star_wars_ep_6,
          goofy_movie]
fresh_tomatoes.open_movies_page(movies)
