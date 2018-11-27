
$(document).ready(function() {
   
    $('#representante-form').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            nombres: {
                validators: {
                        stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                        notEmpty: {
                        message: 'Ingrese el o los nombre'
                    }
                }
            },
            apellido_paterno: {
                validators: {
                     stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese el apellido paterno'
                    }
                }
            },
            apellido_materno: {
                validators: {
                     stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese el apellido materno'
                    }
                }
            },
            numero_id: {
                validators: {
                     stringLength: {
                        min: 6,
                        message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese su número de identificación'
                    }
                }
            },
            pais_nacimiento: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            ciudad_nacimiento: {
                validators: {
                     stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese la ciudad de nacimiento'
                    }
                }
            },                                                
            fecha_nacimiento: {
                    validators: {
                        notEmpty: {
                            message: 'Ingrese la fecha de nacimiento'
                        },

                        date: {
                            format: 'DD/MM/AAAA',
                            message: 'Ingrese fecha en formato DD/MM/AAAA'
                        }
                        
                    }
            },
            estado_civil: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },

            nivel_estudios: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },

            
            numero_hijos: {
                validators: {
                     stringLength: {
                        min: 1,
                         message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese solamente números'
                    }
                }
            },
            relacion: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            lugar_trabajo: {
                validators: {
                     stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese su lugar de trabajo'
                    }
                }
            },
            direccion_trabajo: {
                validators: {
                     stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese la dirección'
                    }
                }
            },
            cargo: {
                validators: {
                        stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                        notEmpty: {
                        message: 'Ingrese el cargo'
                    }
                }
            },
            tiempo_trabajo: {
                validators: {
                        notEmpty: {
                        message: 'Ingrese los años de trabajo'
                    }
                }
            },
            telefono_trabajo: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su teléfono de trabajo'
                    },
                    stringLength: {
                        min: 9,
                        max: 9,
                        message:'Ingrese el teléfono con formato 026017070'
                    }
                }
            },
            correo_trabajo: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su correo de trabajo'
                    },
                    emailAddress: {
                        message: 'Ingrese un correo electrónico válido'
                    }
                }
            },
            telefono_celular: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su teléfono celular'
                    },
                    stringLength: {
                        min: 10,
                        max: 10,
                        message:'Ingrese el teléfono con formato 0920304050'
                    }
                }
            },
            operadora_celular: {
                validators: {
                        notEmpty: {
                        message: 'Seleccione una opción'
                    }

                }
            },
            telefono_casa: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su teléfono de casa'
                    },
                    stringLength: {
                        min: 9,
                        max: 9,
                        message:'Ingrese el teléfono con formato 026017070'
                    }
                }
            },
            correo_personal: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su correo personal'
                    },
                    emailAddress: {
                        message: 'Ingrese un correo electrónico válido'
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
            },/**/
 
        }
    })
    .on('success.form.bv', function(e) {
        $('#success_message').slideDown({ opacity: "show" }, "slow") // Do something ...
            $('#representante-form').data('bootstrapValidator').resetForm();

            e.preventDefault();

            var $form = $(e.target);

            var bv = $form.data('bootstrapValidator');

            $.post($form.attr('action'), $form.serialize(), function(result) {
                console.log(result);
            }, 'json');
    });
        
    $('.datepicker')
    .on('changeDate', function(e) {
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

