

class MapaUrl():

    def __init__(self):
        self.centro = "center=concepcion del uruguay"
        self.zoom = "&zoom=14"
        self.size = "&size=500x500"
        self.formato = "&formato=png"
        self.maptype = "&maptype=roadmap"
        self.leguaje = "&language=es-ES"
        self.marcadores = "" #"&markers=color:green|label:M|-32.4818434,-58.2391088|-32.4829361,-58.2398935"
        self.marcadores2 = "" #"&markers=color:purple|label:J|concepcion del uruguay"

    def get_url(self):
        parametros = self.centro + self.zoom + self.size + self.formato + self.maptype + self.leguaje + self.marcadores+self.marcadores2
        return "https://maps.googleapis.com/maps/api/staticmap?" + parametros

    def tipomapa(self, num):
        """0 - roadmap, 1 - satellite, 2 - hybrid, and 3 -terrain"""
        tipo = ["roadmap", "satellite", "hybrid", "terrain"]
        self.maptype = "&maptype=" + tipo[num]

    def set_marcadores(self, museos):
        ciencia = []
        historia = []
        for museo in museos:
            print(museo.tipo, museo. nombre)
            if museo.tipo == 'ciencia':
                ciencia.append(museo.direccion + " concepcion del uruguay")
            else:
                historia.append(museo.direccion + " concepcion del uruguay")
        lista = "|"
        lista = lista.join(ciencia)
        self.marcadores = "&markers=color:green|" + lista
        lista = "|"
        lista = lista.join(historia)
        self.marcadores2 = "&markers=color:yellow|" + lista

    def mapa_dinamico(self):
        lista = [
              ['hola', -33.890542, 151.274856, 4],
              ['mundo', -33.923036, 151.259052, 5],
              ['desde', -34.028249, 151.157507, 3],
              ['python', -33.80010128657071, 151.28747820854187, 2],
              ['Maroubra Beach', -33.950198, 151.259302, 1]
            ]


        html = '''
        <!DOCTYPE html>
        <html>
        <head>
          <meta http-equiv='content-type' content='text/html; charset=UTF-8' />
          <title>Google Maps Multiple Markers</title>
          <script src='http://maps.google.com/maps/api/js?sensor=false'
                  type="text/javascript"></script>
        </head>
        <body>
          <div id='map' style='width: 500px; height: 500px;'></div>

          <script type='text/javascript'>
            var locations = ''' + str(lista) +''';

            var map = new google.maps.Map(document.getElementById('map'), {
              zoom: 10,
              center: new google.maps.LatLng(-33.92, 151.25),
              mapTypeId: google.maps.MapTypeId.ROADMAP
            });

            var infowindow = new google.maps.InfoWindow();

            var marker, i;
            for (i = 0; i < locations.length; i++) {
        	var diricon = "";
        	switch (i) {
            case 0:
                diricon = "http://maps.google.com/mapfiles/ms/icons/blue-dot.png";
                break;
            case 1:
                diricon = "http://maps.google.com/mapfiles/ms/icons/red-dot.png";
                break;
            case 2:
                diricon = "http://maps.google.com/mapfiles/ms/icons/purple-dot.png";
                break;
            case 3:
                diricon = "http://maps.google.com/mapfiles/ms/icons/yellow-dot.png";
                break;
            case 4:
                diricon = "http://maps.google.com/mapfiles/ms/icons/green-dot.png";
                break;
        	}
              marker = new google.maps.Marker({
                position: new google.maps.LatLng(locations[i][1], locations[i][2]),

                map: map
              });

              google.maps.event.addListener(marker, 'click', (function(marker, i) {
                return function() {
                  infowindow.setContent(locations[i][0]);
                  infowindow.open(map, marker);
                }
              })(marker, i));
            }
          </script>
        </body>
        </html>
        '''
        return html
