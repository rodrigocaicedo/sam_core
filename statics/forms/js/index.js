
$(document).ready(function() {
   
    $('#contact_form').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            name_student: {
                validators: {
                        stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                        notEmpty: {
                        message: 'Ingrese los nombres completos'
                    }
                }
            },
            apellidos: {
                validators: {
                     stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese los apellidos completos'
                    }
                }
            },
            genero: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            fecha_de_nacimiento: {
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
            pais_de_nacimiento: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            
            direccion: {
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
            nivel_aplicado: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            nombres_representante: {
                validators: {
                        stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                        notEmpty: {
                        message: 'Ingrese sus nombres y apellidos'
                    }
                }
            },
            email_representante: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su correo electrónico'
                    },
                    emailAddress: {
                        message: 'Ingrese un correo electrónico válido'
                    }
                }
            },
            telefono_fijo_representante: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su número de teléfono fijo'
                    },
                    stringLength: {
                        min: 9,
                        max: 9,
                        message:'Ingrese el teléfono con formato 026017070'
                    }
                }
            },
            telefono_celular_representante: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su número de teléfono fijo'
                    },
                    phone: {
                        country: 'EC',
                        message: 'Ingrese el teléfono con formato 0990909090'
                    }
                }
            },
            
            zip: {
                validators: {
                    notEmpty: {
                        message: 'Please supply your zip code'
                    },
                    zipCode: {
                        country: 'US',
                        message: 'Please supply a vaild zip code'
                    }
                }
            },
            comment: {
                validators: {
                      stringLength: {
                        min: 10,
                        max: 200,
                        message:'Please enter at least 10 characters and no more than 200'
                    },
                    notEmpty: {
                        message: 'Please supply a description of your project'
                    }
                    }
                }
            }
        })
        .on('success.form.bv', function(e) {
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
        });
        
       $('.datepicker')
    .on('changeDate', function(e) {
         //$('#id_fecha_de_nacimiento').focus();
         //$('#id_telefono_celular_representante').focus();
         //$('#id_fecha_de_nacimiento').focus(); 
        // Revalidate the date when user change it
        //alert("hey");
//        $('#contact_form').bootstrapValidator('validateField', 'fecha_de_nacimiento');
        $('#contact_form').bootstrapValidator('updateStatus', 'fecha_de_nacimiento', 'NOT_VALIDATED')
    .bootstrapValidator('validateField', 'fecha_de_nacimiento');
    }); 
 
});

$(function() {
    $(".datepicker").datepicker({autoclose:true, format: 'yyyy-mm-dd'});
});

