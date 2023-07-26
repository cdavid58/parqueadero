!function ($) {
    "use strict";

    var SweetAlert = function () {
    };

    //examples
    SweetAlert.prototype.init = function () {

        $('#error_data').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops...',
                    text: 'La información es incorrecta',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });

        $('#error_login').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops...',
                    text: 'La información es incorrecta',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });

        $('#register_data').click(function () {
            swal(
                {
                    type: 'success',
                    title: 'Éxito',
                    text: 'Se registro el vehiculo exitosamente',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });

        $('#delete_data').click(function () {
            swal(
                {
                    type: 'success',
                    title: 'Éxito',
                    text: 'El carro fué eliminado con exito',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });

        $('#validate_login_error').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops...',
                    text: 'Usuario o contraseña incorrecta',
                    timer: 3000,
                    showConfirmButton:false
                }
            )
        });


        $('#REGISTRAMOSCLIENTE').click(function () {
            swal(
                {
                    type: 'info',
                    title: 'Información',
                    text: 'Enviando datos',
                    timer: 1500,
                    showConfirmButton:false
                }
            )
        });

        $('#SAVEUSER').click(function () {
            swal(
                {
                    type: 'success',
                    title: 'Éxito',
                    text: 'El usuario fué creado con éxito',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });

        $('#ERRORUSER').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops...',
                    text: 'El usuario no ya existe',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });

        $('#UPATEUSER').click(function () {
            swal(
                {
                    type: 'success',
                    title: 'Éxito',
                    text: 'El usuario fué actualizado con éxito',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });

        $('#UPDATERRORUSER').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops...',
                    text: 'El usuario no fué actualizado con éxito',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });





    },
        //init
        $.SweetAlert = new SweetAlert, $.SweetAlert.Constructor = SweetAlert
}(window.jQuery),

//initializing
    function ($) {
        "use strict";
        $.SweetAlert.init()
    }(window.jQuery);