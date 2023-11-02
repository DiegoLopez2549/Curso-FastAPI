from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(
    title="App con FastAPI", version="0.0.1", description="Una API para aprender"
)
movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción",
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción",
    },
]


@app.get("/", tags=["home"], response_class=HTMLResponse)
def message():
    return """
        <html
            <head>
                <title>Web App con FastAPI</title>
                </head>
                <body>
                    <h1>¡Hola a todos!</h1>
                    <p>Este es un mensaje de ejemplo</p>
                </body>
        </html>
"""


@app.get("/movies/{id}", tags=["movies"])
def get_movie(id: int):
    try:
        return [movie for movie in movies if movie["id"] == id][0]
    except IndentationError:
        return {"Error": "No hay pelicalas para mostrar"}


@app.get("/items/{item_id}/sub/{item_id2}")
def read_item(item_id: int, item_id2: str):
    return {"item_id": item_id, "item_id2": item_id2}


# Porque las operaciones de path son evaluadas en orden,
# tienes que asegurarte de que el path para /users/me
# sea declarado antes que el path para /users/{user_id}:
# De otra manera el path para /users/{user_id}
# coincidiría también con /users/me "pensando"
# que está recibiendo el parámetro user_id con el valor "me".


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


# Parametro Query
@app.get("/movies/", tags=["movies"])
def get_movies_by_category(category: str, year: int):
    return category


"""@app.post("/movies/", tags=["movies"])
def create_movie(
    id: int = Body(default=1),
    title: str = Body(default=0),
    overview: str = Body(default=0),
    year: int = Body(default=0),
    rating: float = Body(default=0),
    category: str = Body(default="text"),
):
    movies.append(
        {
            "id": id,
            "title": title,
            "overview": overview,
            "year": year,
            "rating": rating,
            "category": category,
        }
    )
    return movies
"""


# Otra forma de hacerlo...
# Modelo de datos para representar información de películas.
class Movies(BaseModel):
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str


@app.post("/movies/", tags=["movies"])
def create_movie(movie: Movies = Body(...)):
    movies.append(movie)
    return movies


# Editar una película
@app.put("/movies/{id}", tags=["movies"])
def update_movie(id: int, movie: Movies):
    for item in movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category
    return movies


# Eliminar una película
@app.delete("/movies/{id}", tags=["movies"])
def delete_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            break
    return movies
