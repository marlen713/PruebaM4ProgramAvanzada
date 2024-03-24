
from campaña import Campaña
from anuncio import Video, Display, Social
from error import SubTipoInvalidoException, LargoExcedidoException


try:
    anuncio = Video("Subtipo del video", 10)
    campaña = Campaña("Campaña 1", [anuncio])

    new_nombre = input("Ingrese el nuevo nombre de la campaña: ")
    new_subtipo = int(input("Ingrese el nuevo subtipo para el anuncio: "))

    campaña.nombre = new_nombre 
    anuncio.sub_tipo = new_subtipo

except (SubTipoInvalidoException, LargoExcedidoException) as e:
    with open('error.log', 'a') as f:
        f.write(str(e))


try:
    anuncio = Display(10, 5, "Subtipo1", "url_archivo_display", "url_clic_display")
    campaña = Campaña("Campaña 2", [anuncio])

    new_nombre = input("Ingrese el nuevo nombre de la campaña: ")
    new_subtipo = int(input("Ingrese el nuevo subtipo para el anuncio: "))

    campaña.nombre = new_nombre 
    anuncio.sub_tipo = new_subtipo

except (SubTipoInvalidoException, LargoExcedidoException) as e:
    with open('error.log', 'a') as f:
        f.write(str(e))


try:
    anuncio = Social(10, 5, "Subtipo1", "url_archivo_display", "url_clic_display")
    campaña = Campaña("Campaña 3", [anuncio])

    new_nombre = input("Ingrese el nuevo nombre de la campaña: ")
    new_subtipo = int(input("Ingrese el nuevo subtipo para el anuncio: "))

    campaña.nombre = new_nombre 
    anuncio.sub_tipo = new_subtipo

except (SubTipoInvalidoException, LargoExcedidoException) as e:
    with open('error.log', 'a') as f:
        f.write(str(e))
