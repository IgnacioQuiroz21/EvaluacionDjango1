
//Validador que proporciona Boostrap 5
//(function () {
//  'use strict'   
//    var forms = document.querySelectorAll('.needs-validation')   
//    Array.prototype.slice.call(forms)
//      .forEach(function (form) {
//        form.addEventListener('submit', function (event) {
//          if (!form.checkValidity()) {
//            event.preventDefault()
//           event.stopPropagation()
//          }
//  
//         form.classList.add('was-validated')
//        }, false)
//      })
//  })()

$(function() {
    

   $("#fnFamilia_error_mensaje").hide();
   $("#fnPersonaje_error_mensaje").hide();
   $("#femail_error_mensaje").hide();
   $("#fdescripcion_error_mensaje").hide();
   

   var error_fnFamilia = false;
   var error_fnPersonaje = false;
   var error_femail = false;
   var error_fdescripcion = false;
   

   $("#form_familia").focusout(function(){
      check_nFamilia()
   });
   $("#form_personaje").focusout(function() {
      check_nPersonaje();
   });
   $("#form_email").focusout(function() {
      check_email();
   });
   $("#form_descripcion").focusout(function() {
      check_descripcionTexto();
   });


   function check_nFamilia() {
      var pattern = /^[a-zA-Z]*$/;
      var Ffamilia = $("#form_familia").val();
      if (pattern.test(Ffamilia) && Ffamilia !== '') {
         $("#fnFamilia_error_mensaje").hide();
         $("#form_familia").css("border-bottom","2px solid #34F458");
      } else {
         $("#fnFamilia_error_mensaje").html("Por favor, escriba su nombre de familia.");
         $("#fnFamilia_error_mensaje").show();
         $("#form_familia").css("border-bottom","2px solid #F90A0A");
         error_fnFamilia = true;
      }
   }

   function check_nPersonaje() {
      var pattern = /^[a-zA-Z]*$/;
      var FPersonaje = $("#form_personaje").val()
      if (pattern.test(FPersonaje) && FPersonaje !== '') {
         $("#fnPersonaje_error_mensaje").hide();
         $("#form_personaje").css("border-bottom","2px solid #34F458");
      } else {
         $("#fnPersonaje_error_mensaje").html("Por favor, escriba el nombre de su personaje.");
         $("#fnPersonaje_error_mensaje").show();
         $("#form_personaje").css("border-bottom","2px solid #F90A0A");
         error_fnPersonaje = true;
      }
   }

   function check_email() {
    var pattern = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
    var email = $("#form_email").val();
    if (pattern.test(email) && email !== '') {
       $("#femail_error_mensaje").hide();
       $("#form_email").css("border-bottom","2px solid #34F458");
    } else {
       $("#femail_error_mensaje").html("Por favor, escriba un correo electrónico.");
       $("#femail_error_mensaje").show();
       $("#form_email").css("border-bottom","2px solid #F90A0A");
       error_femail = true;
    }
   }

   function check_descripcionTexto() {
    
    var FdescripcionTexto = $("#form_descripcion").val()
    if ( FdescripcionTexto !== '') {
       $("#fdescripcion_error_mensaje").hide();
       $("#form_descripcion").css("border-bottom","2px solid #34F458");
    } else {
       $("#fdescripcion_error_mensaje").html("Por favor, escriba su mensaje.");
       $("#fdescripcion_error_mensaje").show();
       $("#form_descripcion").css("border-bottom","2px solid #F90A0A");
       error_fdescripcion = true;
    }
   }



   $("#formulario").submit(function() {
    error_fnFamilia = false;
    error_fnPersonaje = false;
    error_femail = false;
    error_fdescripcion = false;
    

    check_nFamilia();
    check_nPersonaje();
    check_email();
    check_descripcionTexto();
      

      if (error_fnFamilia === false && error_fnPersonaje === false && error_femail === false && error_fdescripcion === false) {
         alert("Mensaje Enviado!");
         return true;
      } else {
         alert("Completa el formulario correctamente");
         return false;
      }


   });
});



