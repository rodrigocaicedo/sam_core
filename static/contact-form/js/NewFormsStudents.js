
$(document).ready(function() {



    $(function() {
        $(".datepicker").datepicker({autoclose:true, format: 'yyyy-mm-dd'});
    });
 

    $('#s_fecha_nacimiento_id')
    .on('change', function(e) {
        $(this).datepicker("hide");
        $('#contact_form').bootstrapValidator('updateStatus', 's_fecha_nacimiento', 'NOT_VALIDATED');
        $('#contact_form').bootstrapValidator('validateField', 's_fecha_nacimiento');
    });

    $('#m_fecha_nacimiento_id')
    .on('change', function(e) {
        $(this).datepicker("hide");
        $('#contact_form').bootstrapValidator('updateStatus', 'm_fecha_nacimiento', 'NOT_VALIDATED');
        $('#contact_form').bootstrapValidator('validateField', 'm_fecha_nacimiento');
    });
    $('#p_fecha_nacimiento_id')
    .on('change', function(e) {
        $(this).datepicker("hide");
        $('#contact_form').bootstrapValidator('updateStatus', 'p_fecha_nacimiento', 'NOT_VALIDATED');
        $('#contact_form').bootstrapValidator('validateField', 'p_fecha_nacimiento');
    });
    $('#r_fecha_nacimiento_id')
    .on('change', function(e) {
        $(this).datepicker("hide");
        $('#contact_form').bootstrapValidator('updateStatus', 'r_fecha_nacimiento', 'NOT_VALIDATED');
        $('#contact_form').bootstrapValidator('validateField', 'r_fecha_nacimiento');
    });
   
    $('#contact_form').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            s_identificacion: {
                validators: {
                        stringLength: {
                        min: 6,
                        max: 15,
                        message:'Ingrese entre 6 y 15 caracteres'
                    },
                        notEmpty: {
                        message: 'Ingrese el número del Documento de Identificación'
                    },
                        regexp: {
                        regexp: /^[a-zA-Z0-9]+$/i,
                        message: 'Ingrese letras y/o números solamente'
                    }

                }
            },
            s_nombres: {
                validators: {
                        stringLength: {
                        min: 3,
                        message:'Información no válida'
                    },
                        notEmpty: {
                        message: 'Ingrese los nombres completos'
                    },
                        regexp: {
                        regexp: /^[a-zA-Z\s]+$/i,
                        message: 'Ingrese letras y espacios solamente'
                    }
                }
            },
            s_apellidos: {
                validators: {
                        stringLength: {
                        min: 3,
                        message:'Información no válida'
                    },
                        notEmpty: {
                        message: 'Ingrese el apellido paterno'
                    },
                        regexp: {
                        regexp: /^[a-zA-Z\s]+$/i,
                        message: 'Ingrese letras y espacios solamente'
                    }
                }
            },
            s_apellidos_2: {
                validators: {
                        stringLength: {
                        min: 3,
                        message:'Información no válida'
                    },
                        notEmpty: {
                        message: 'Ingrese el apellido materno'
                    },
                        regexp: {
                        regexp: /^[a-zA-Z\s]+$/i,
                        message: 'Ingrese letras y espacios solamente'
                    }
                }
            },
            s_genero: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            s_fecha_nacimiento: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese la fecha de nacimiento'
                    },

                    date: {
                        format: 'YYYY-MM-AA',
                        message: 'Ingrese fecha en formato YYYY-MM-AA'
                    }
                    
                }
            },
            s_pais_nacimiento: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            s_pais_residencia: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            s_direccion: {
                validators: {
                     stringLength: {
                        min: 5,
                         message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese la dirección de su domicilio'
                    }
                }
            },
            s_grado_aplica: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            p_identificacion: {
                validators: {
                        stringLength: {
                        min: 6,
                        max: 15,
                        message:'Ingrese entre 6 y 15 caracteres'
                    },
                        notEmpty: {
                        message: 'Ingrese el número del Documento de Identificación'
                    },
                        regexp: {
                        regexp: /^[a-zA-Z0-9]+$/i,
                        message: 'Ingrese letras y/o números solamente'
                    }
                }
            },
            p_nombres: {
                validators: {
                        stringLength: {
                        min: 3,
                        message:'Información no válida'
                    },
                        notEmpty: {
                        message: 'Ingrese los nombres completos'
                    },
                        regexp: {
                        regexp: /^[a-zA-Z\s]+$/i,
                        message: 'Ingrese letras y espacios solamente'
                    }
                }
            },
            p_apellidos: {
                validators: {
                     stringLength: {
                        min: 3,
                        message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese el apellido paterno'
                    },
                        regexp: {
                        regexp: /^[a-zA-Z\s]+$/i,
                        message: 'Ingrese letras y espacios solamente'
                    }
                }
            },
            p_apellidos_2: {
                validators: {
                     stringLength: {
                        min: 3,
                        message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese el apellido materno'
                    },
                        regexp: {
                        regexp: /^[a-zA-Z\s]+$/i,
                        message: 'Ingrese letras y espacios solamente'
                    }
                }
            },
            p_fecha_nacimiento: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese la fecha de nacimiento'
                    },

                    date: {
                        format: 'YYYY-MM-AA',
                        message: 'Ingrese fecha en formato YYYY-MM-AA'
                    }
                    
                }
            },
            p_pais_nacimiento: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            p_pais_residencia: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            p_instruccion: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            p_direccion: {
                validators: {
                     stringLength: {
                        min: 8,
                         message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese la dirección de su domicilio'
                    }
                }
            },
            p_profesion: {
                validators: {
                     stringLength: {
                        min: 3,
                         message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese su profesión'
                    }
                }
            },
            p_trabajo: {
                validators: {
                     stringLength: {
                        min: 3,
                         message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese el nombre de la organización'
                    }
                }
            },
            p_mail: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su correo electrónico'
                    },
                    emailAddress: {
                        message: 'Ingrese un correo electrónico válido'
                    }
                }
            },
            p_telefono: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su número de teléfono fijo'
                    },
                    stringLength: {
                        min: 9,
                        max: 9,
                        message:'Ingrese el teléfono con formato 026017070'
                    },
                    digits: {
                        message: 'Ingrese números solamente'
                    }
                }
            },
            p_telofi: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su número de teléfono oficina'
                    },
                    stringLength: {
                        min: 9,
                        max: 9,
                        message:'Ingrese el teléfono con formato 026017070'
                    },
                    digits: {
                        message: 'Ingrese números solamente'
                    }
                }
            },
            p_cell: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su número de celular'
                    },
                    phone: {
                        country: 'EC',
                        message: 'Ingrese el teléfono con formato 0990909090'
                    },
                    digits: {
                        message: 'Ingrese números solamente'
                    }
                }
            },
            p_difunto: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            p_vive_con: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            p_retirar: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            m_identificacion: {
                validators: {
                        stringLength: {
                        min: 6,
                        max: 15,
                        message:'Ingrese entre 6 y 15 caracteres'
                    },
                        notEmpty: {
                        message: 'Ingrese el número del Documento de Identificación'
                    },
                        regexp: {
                        regexp: /^[a-zA-Z0-9]+$/i,
                        message: 'Ingrese letras y/o números solamente'
                    }
                }
            },
            m_nombres: {
                validators: {
                        stringLength: {
                        min: 3,
                        message:'Información no válida'
                    },
                        notEmpty: {
                        message: 'Ingrese los nombres completos'
                    },
                        regexp: {
                        regexp: /^[a-zA-Z\s]+$/i,
                        message: 'Ingrese letras y espacios solamente'
                    }
                }
            },
            m_apellidos: {
                validators: {
                     stringLength: {
                        min: 3,
                        message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese el apellido paterno'
                    },
                        regexp: {
                        regexp: /^[a-zA-Z\s]+$/i,
                        message: 'Ingrese letras y espacios solamente'
                    }
                }
            },
            m_apellidos_2: {
                validators: {
                     stringLength: {
                        min: 3,
                        message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese el apellido materno'
                    },
                        regexp: {
                        regexp: /^[a-zA-Z\s]+$/i,
                        message: 'Ingrese letras y espacios solamente'
                    }
                }
            },
            m_fecha_nacimiento: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese la fecha de nacimiento'
                    },

                    date: {
                        format: 'YYYY-MM-AA',
                        message: 'Ingrese fecha en formato YYYY-MM-AA'
                    }
                    
                }
            },
            m_pais_nacimiento: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            m_pais_residencia: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            m_instruccion: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            m_direccion: {
                validators: {
                     stringLength: {
                        min: 8,
                         message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese la dirección de su domicilio'
                    }
                }
            },
            m_profesion: {
                validators: {
                     stringLength: {
                        min: 3,
                         message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese su profesión'
                    }
                }
            },
            m_trabajo: {
                validators: {
                     stringLength: {
                        min: 3,
                         message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese el nombre de la organización'
                    }
                }
            },
            m_mail: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su correo electrónico'
                    },
                    emailAddress: {
                        message: 'Ingrese un correo electrónico válido'
                    }
                }
            },
            m_telefono: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su número de teléfono fijo'
                    },
                    stringLength: {
                        min: 9,
                        max: 9,
                        message:'Ingrese el teléfono con formato 026017070'
                    },
                    digits: {
                        message: 'Ingrese números solamente'
                    }
                }
            },
            m_telofi: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su número de teléfono oficina'
                    },
                    stringLength: {
                        min: 9,
                        max: 9,
                        message:'Ingrese el teléfono con formato 026017070'
                    },
                    digits: {
                        message: 'Ingrese números solamente'
                    }
                }
            },
            m_cell: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su número de celular'
                    },
                    phone: {
                        country: 'EC',
                        message: 'Ingrese el teléfono con formato 0990909090'
                    },
                    digits: {
                        message: 'Ingrese números solamente'
                    }
                }
            },
            m_difunto: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            m_vive_con: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            m_retirar: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },

            r_identificacion: {
                validators: {
                        stringLength: {
                        min: 6,
                        max: 15,
                        message:'Ingrese entre 6 y 15 caracteres'
                    },
                        notEmpty: {
                        message: 'Ingrese el número del Documento de Identificación'
                    },
                        regexp: {
                        regexp: /^[a-zA-Z0-9]+$/i,
                        message: 'Ingrese letras y/o números solamente'
                    }
                }
            },
            r_nombres: {
                validators: {
                        stringLength: {
                        min: 3,
                        message:'Información no válida'
                    },
                        notEmpty: {
                        message: 'Ingrese los nombres completos'
                    },
                        regexp: {
                        regexp: /^[a-zA-Z\s]+$/i,
                        message: 'Ingrese letras y espacios solamente'
                    }
                }
            },
            r_apellidos: {
                validators: {
                     stringLength: {
                        min: 3,
                        message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese el apellido paterno'
                    },
                        regexp: {
                        regexp: /^[a-zA-Z\s]+$/i,
                        message: 'Ingrese letras y espacios solamente'
                    }
                }
            },
            r_apellidos_2: {
                validators: {
                     stringLength: {
                        min: 3,
                        message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese el apellido materno'
                    },
                        regexp: {
                        regexp: /^[a-zA-Z\s]+$/i,
                        message: 'Ingrese letras y espacios solamente'
                    }
                }
            },
            r_fecha_nacimiento: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese la fecha de nacimiento'
                    },

                    date: {
                        format: 'YYYY-MM-AA',
                        message: 'Ingrese fecha en formato YYYY-MM-AA'
                    }
                    
                }
            },
            r_genero: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            r_pais_nacimiento: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            r_pais_residencia: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            r_instruccion: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            r_direccion: {
                validators: {
                     stringLength: {
                        min: 8,
                         message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese la dirección de su domicilio'
                    }
                }
            },
            r_profesion: {
                validators: {
                     stringLength: {
                        min: 3,
                         message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese su profesión'
                    }
                }
            },
            r_trabajo: {
                validators: {
                     stringLength: {
                        min: 3,
                         message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese el nombre de la organización'
                    }
                }
            },
            r_mail: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su correo electrónico'
                    },
                    emailAddress: {
                        message: 'Ingrese un correo electrónico válido'
                    }
                }
            },
            r_telefono: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su número de teléfono fijo'
                    },
                    stringLength: {
                        min: 9,
                        max: 9,
                        message:'Ingrese el teléfono con formato 026017070'
                    },
                    digits: {
                        message: 'Ingrese números solamente'
                    }
                }
            },
            r_telofi: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su número de teléfono oficina'
                    },
                    stringLength: {
                        min: 9,
                        max: 9,
                        message:'Ingrese el teléfono con formato 026017070'
                    },
                    digits: {
                        message: 'Ingrese números solamente'
                    }
                }
            },
            r_cell: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su número de celular'
                    },
                    phone: {
                        country: 'EC',
                        message: 'Ingrese el teléfono con formato 0990909090'
                    },
                    digits: {
                        message: 'Ingrese números solamente'
                    }
                }
            },
            r_vive_con: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            r_retirar: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            representante: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            }
        }
    })
/*    .on('success.form.bv', function(e) {
        $('#success_message').slideDown({ opacity: "show" }, "slow") // Do something ...
            $('#contact_form').data('bootstrapValidator').resetForm();

            // Prevent form submission
            e.preventDefault();

            // Get the form instance
            var $form = $(e.target);

            // Get the BootstrapValidator instance
            var bv = $form.data('bootstrapValidator');

        // Use Ajax to submit form data
            $.post($form.attr('action'), $form.serialize(), function(result) {
                console.log(result);
            }, 'json');
    });*/
        




});



