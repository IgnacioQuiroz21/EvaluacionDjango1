$(document).ready(function() {
                                                                   
    $.getJSON('http://127.0.0.1:8000/api/listar', function(data) {
        var anuncio = data;
       
        $.each(anuncio, function(i, item) {
            $('#Anuncios').append("<tr><td>" + item.idAnuncio + "</td><td>" + item.nombre + 
                                "</td><td>" + item.descAnuncio + "</td></tr>");
        });

        
    }).fail(function() {
        console.log('Error al consumir la API!');
    });



    

});
           
        
  