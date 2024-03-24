from anuncio import Video, Display, Social


class Campaña:
    def __init__(self, nombre, anuncios):
        self.nombre = nombre
        self.anuncios = anuncios

    def __str__(self):
        count_video = sum(1 for anuncio in self.anuncios if isinstance(anuncio, Video))
        count_display = sum(1 for anuncio in self.anuncios if isinstance(anuncio, Display))
        count_social = sum(1 for anuncio in self.anuncios if isinstance(anuncio, Social))

        return f"Nombre de la campaña: {self.nombre}\nAnuncios: {count_video} Video, {count_display} Display, {count_social} Social"

