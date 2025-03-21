def transform_data(data):
    def categorize_rating(rating):
        if rating >= 8:
            return "Buena"
        elif rating >= 5:
            return "Regular"
        else:
            return "Mala"

    for movie in data:
        movie["nombre_formateado"] = movie["p.nombre"].lower().replace(" ", "-")
        movie["categoria_calificacion"] = categorize_rating(movie["p.calificacion"])
        movie["decada"] = f"{(movie['p.año_lanzamiento'] // 10) * 10}s"
        movie["puntuacion_ajustada"] = (movie["p.calificacion"] * 2) - (2025 - movie["p.año_lanzamiento"]) / 10

    return data
