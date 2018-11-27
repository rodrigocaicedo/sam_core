
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
            surname_student: {
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
            gender_student: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            birth_date: {
                    validators: {
                        notEmpty: {
                            message: 'Ingrese la fecha de nacimiento'
                        },

                        date: {
                            format: 'dd/mm/aaaa',
                            message: 'Ingrese fecha en formato dd/mm/aaaa'
                        }
                        
                    }
            },
            birth_country: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },

            country_home: {
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
            applied_grade: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            school_period: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },


            name_tutor: {
                validators: {
                        stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                        notEmpty: {
                        message: 'Ingrese sus nombres'
                    }
                }
            },

            surname_tutor: {
                validators: {
                        stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                        notEmpty: {
                        message: 'Ingrese sus apellidos'
                    }
                }
            },
            mail_tutor: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su correo electrónico'
                    },
                    emailAddress: {
                        message: 'Ingrese un correo electrónico válido'
                    }
                }
            },
            phone_tutor: {
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
            cell_tutor: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su número de teléfono fijo'
                    },
                    stringLength: {
                        min: 10,
                        max: 10,
                        message:'Ingrese el teléfono con formato 0920304050'
                    }
                }
            },
            name_school: {
                validators: {
                        notEmpty: {
                        message: 'Ingrese sus apellidos'
                    }

                }
            },
            address_school: {
                validators: {

                        notEmpty: {
                        message: 'Ingrese sus apellidos'
                    }
                }
            },
            last_year: {
                validators: {

                        notEmpty: {
                        message: 'Ingrese sus apellidos'
                    }
                }
            },
            surname_tutor: {
                validators: {
                        stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                        notEmpty: {
                        message: 'Ingrese sus apellidos'
                    }
                }
            },            

            s_identificacion: {
                validators: {
                        stringLength: {
                        min: 2,
                        max: 15,
                        message:'Información no válida máximo 15 caracteres'
                    },
                        notEmpty: {
                        message: 'Ingrese el número de Identificación'
                    }
                }
            },
            s_nombres: {
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
            s_apellidos: {
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
                        min: 2,
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
                        min: 10,
                        max: 15,
                        message:'Información no válida máximo 15 caracteres'
                    },
                        notEmpty: {
                        message: 'Ingrese el número de Identificación'
                    }
                }
            },
            p_nombres: {
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
            p_apellidos: {
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
            p_genero: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
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
                    }
                }
            },
            m_identificacion: {
                validators: {
                        stringLength: {
                        min: 10,
                        max: 15,
                        message:'Información no válida máximo 15 caracteres'
                    },
                        notEmpty: {
                        message: 'Ingrese el número de Identificación'
                    }
                }
            },
            m_nombres: {
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
            m_apellidos: {
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
            m_genero: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
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
            m_direccion: {
                validators: {
                     stringLength: {
                        min: 2,
                         message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese la dirección de su domicilio'
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
                    }
                }
            },
            r_identificacion: {
                validators: {
                        stringLength: {
                        min: 10,
                        max: 15,
                        message:'Información no válida máximo 15 caracteres'
                    },
                        notEmpty: {
                        message: 'Ingrese el número de Identificación'
                    }
                }
            },
            r_nombres: {
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
            r_apellidos: {
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
            r_genero: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
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
            r_direccion: {
                validators: {
                     stringLength: {
                        min: 2,
                         message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese la dirección de su domicilio'
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
                    }
                }
            },
            phone: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su número de teléfono'
                    },
                    stringLength: {
                        min: 9,
                        max: 9,
                        message:'Ingrese el teléfono con formato 026017070'
                    }
                }
            },
            cell: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su número de celular'
                    },
                    phone: {
                        country: 'EC',
                        message: 'Ingrese el teléfono con formato 0990909090'
                    }
                }
            },
            mail: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su correo electrónico'
                    },
                    emailAddress: {
                        message: 'Ingrese un correo electrónico válido'
                    }
                }
            },
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
        $('#contact_form').bootstrapValidator('updateStatus', 's_fecha_nacimiento_id', 'NOT_VALIDATED')
            .bootstrapValidator('validateField', 's_fecha_nacimiento');
        $('#contact_form').bootstrapValidator('updateStatus', 'm_fecha_nacimiento_id', 'NOT_VALIDATED')
            .bootstrapValidator('validateField', 'm_fecha_nacimiento');
        $('#contact_form').bootstrapValidator('updateStatus', 'p_fecha_nacimiento_id', 'NOT_VALIDATED')
            .bootstrapValidator('validateField', 'p_fecha_nacimiento');
        $('#contact_form').bootstrapValidator('updateStatus', 'r_fecha_nacimiento_id', 'NOT_VALIDATED')
            .bootstrapValidator('validateField', 'r_fecha_nacimiento');
    }); 
 
});

$(function() {
    $(".datepicker").datepicker({autoclose:true, format: 'yyyy-mm-dd'});
});

