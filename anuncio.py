from error import SubTipoInvalidoException, LargoExcedidoException
from abc import ABC,  abstractmethod


class Anuncio(ABC):
    def __init__(self, ancho, alto, sub_tipo, url_archivo, url_clic):
        self.ancho = ancho if ancho > 0 else 1
        self.alto = alto if alto > 0 else 1
        self.__sub_tipo = sub_tipo
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        
        
    #AQUI COLOCO JUNTO LOS GET
    @property    
    def sub_tipo(self):
        return self.__sub_tipo
    
    @property    
    def url_archivo(self):
        return self.__url_archivo
    
    @property
    def url_clic(self):
        return self.__url_clic
    
    
    #AQUI COLOCO JUNTO LOS SETTER
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo):
        if type(self) == Video:
            if(sub_tipo in Video.SUB_TIPOS):
                self.__sub_tipo = sub_tipo
            else:
                raise SubTipoInvalidoException("El subtipo ingresado no es valido")
        elif type(self) == Display:
            if(sub_tipo in Display.SUB_TIPOS):
                self.__sub_tipo = sub_tipo
            else:
                raise SubTipoInvalidoException("El subtipo ingresado no es valido")
        elif type(self) == Social:
            if(sub_tipo in Social.SUB_TIPOS):
                self.__sub_tipo = sub_tipo
            else:
                raise SubTipoInvalidoException("El subtipo ingresado no es valido")
    
    @url_archivo.setter
    def url_archivo(self, nuevo_url):
        self.__url_archivo = nuevo_url
    
    @url_clic.setter
    def url_clic(self, nuevo_url):
        self.__url_clic = nuevo_url
        


    def mostrar_formatos(self):
        print("FORMATO 1:")
        print("==========")
        for subtipo in self.SUB_TIPOS:
            print(f"- {subtipo}")
            
    @abstractmethod
    def comprimir_anuncio(self):
        pass
    def redimensionar_anuncio(self):
        pass
    


class Video(Anuncio):
    SUB_TIPOS = ["Subtipo1", "Subtipo2"]
    
    def __init__(self, sub_tipo, duracion):
        super().__init__(1, 1, sub_tipo, "url_archivo", "url_clic")
        self.duracion = duracion if duracion > 0 else 5

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")



class Display(Anuncio):
    SUB_TIPOS = ["Subtipo1", "Subtipo2"]
     
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")



class Social(Anuncio):
    SUB_TIPOS = ["Subtipo1", "Subtipo2"]
     
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
