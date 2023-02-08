movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def rating(s):
    for i in range(len(movies)):
        if movies[i]["name"] == s:
            if movies[i]["imdb"] >=5.5:
                print("True")
            else:
                print("False")
if __name__ == "__main__":
    s = input()
    rating(s)


def rating(movies):
    l = []
    for i in range(len(movies)):
        if movies[i]["imdb"] >= 5.5:
            l.append(movies[i]["name"])
    return l
if __name__ == "__main__":
    print(rating())

def rating(r):
    l = []
    for i in range(len(movies)):
        if movies[i]["imdb"] == r:
            l.append(movies[i]["name"])
    return l
if __name__ == "__main__":
    r = float(input())
    print(rating(r))

def rating():
    sum = 0
    l = len(movies)
    for i in range(l):
        sum += movies[i]["imdb"]
    ave_sc = sum / l
    return ave_sc
if __name__ == "__main__":
    print(rating())

