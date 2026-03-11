class Movie:
    def __init__(self, title, genre, duration):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = []

    def add_rating(self, r):
        self.rating.append(r)

    def average_rating(self):
        if len(self.rating) == 0:
            return 0
        return sum(self.rating) / len(self.rating)

    def info(self):
        return f"{self.title} | {self.genre} | {self.duration} min | {self.average_rating():.2f}"


class Cinema:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, genre, duration):
        m = Movie(title, genre, duration)
        self.movies.append(m)

    def show_movies(self):
        for i, m in enumerate(self.movies):
            print(i + 1, m.info())

    def rate_movie(self, index, rate):
        self.movies[index].add_rating(rate)


def run():
    cinema = Cinema()

    cinema.add_movie("Avatar", "Sci-Fi", 160)
    cinema.add_movie("Batman", "Action", 140)

    while True:
        print("1. Kinolar")
        print("2. Baholash")
        print("3. Chiqish")

        c = input()

        if c == "1":
            cinema.show_movies()

        elif c == "2":
            cinema.show_movies()
            i = int(input("Kino: ")) - 1
            r = int(input("Baho: "))
            cinema.rate_movie(i, r)

        else:
            break


run()
