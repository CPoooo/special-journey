import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())
# print(soup.find_all(name="h3"))
all_movies = [soup.getText().split(" ") for soup in soup.find_all(name="h3")]
all_movies.reverse()

s = " "
with open("top_100_movies.txt", "w", encoding="utf8") as file:
    for movie in all_movies:
        file.write(f"{movie[0]} {s.join(movie[1:])}\n")