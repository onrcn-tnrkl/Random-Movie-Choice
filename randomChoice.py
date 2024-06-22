import random

movie_list = [
    "Apocalypse Now", "Goodfellas", "The Shining", "2001: A Space Odyssey", "1917",
    "All Quiet On The Western Front", "Top Gun Maverick", "The Sixth Sense", "Gran Torino",
    "The Exorcist", "The Menu", "Apocalypto", "Velvet Buzzsaw", "Sound of Metal",
    "Once Upon a Time in America", "Braveheart", "City Lights", "Full Metal Jacket",
    "Edward Scissorhands", "One Flew Over The Cuckoo's Nest", "Midnight In Paris",
    "Groundhog Day", "Rain Man", "Titanic", "The Breakfast Club", "Caphernaum",
    "American Beauty", "Sleepy Hollow", "Eyes Wide Shut", "Uzak", "Once Upon A Time İn Anatolia",
    "Mystic River", "In Bruges", "Sweeney Todd: The Demon Barber of Fleet Street", "Black Swan",
    "Les Misérables", "The Lone Ranger", "The Father", "Bad Company", "Immortal Beloved",
    "Kaybedenler Klubü", "Okul Tıraşı", "Kader", "Yazgı", "Pardon", "Big Fish",
    "The Fabelmans", "Goodbye Lenin", "The Game", "Source Code", "Irreversible", "Solaris",
    "Sacrifice", "Ocean's 11", "Ocean's 12", "Ocean's 13", "Her", "Raging Bull", "The Aviator",
    "Casino", "Tonya", "Snatch", "Syke Pike", "The Art Of Racing In The Rain", "Deja Vu", "21",
    "The Bucket List", "The Thirteen Floor", "12 Monkeys", "28 Days Later", "The Road",
    "Melancholy", "Funny Games", "La Pianiste", "Amour", "La Haine", "Chungking Express",
    "Anatomie D'une Chute", "Nocturnal Animals", "Stalingrad", "Das Boot", "Come and See",
    "The Deer Hunter", "The Fighter", "Seven Samurai", "Persona", "Carlito's Way",
    "The Untouchables", "Lars and the Real Girl", "At Eternity's Gate", "There Will Be Blood",
    "Incendies", "Anti Christ", "The Zone Of Interest"
]


def randomMovie(movie_list):
    while len(movie_list)>1:
        f1 = random.choice(movie_list)

        while True:
            f2 = random.choice(movie_list)
            if f1 != f2:
                break

        print("""
        Seç birini!
        .......................................
        1-{}
        2-{}
        """.format(f1, f2))
        yourChoice = input("Seçiminiz (1 veya 2): ")

        if yourChoice == '1':
            movie_list.remove(f2)
        elif yourChoice == '2':
            movie_list.remove(f1)
        else:
            print("Lütfen sadece 1 veya 2 olarak yanıt verin!")
            continue

    print("İzlenecek film:{}".format(movie_list[0]))

randomMovie(movie_list)
