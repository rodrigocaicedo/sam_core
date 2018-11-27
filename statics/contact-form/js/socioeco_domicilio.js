
$(document).ready(function() {
   
    $('#domicilio-form').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            pais_residencia: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            provincia_residencia: {
                validators: {
                        stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                        notEmpty: {
                        message: 'Ingrese el nombre de la provincia'
                    }
                }
            },

            ciudad_residencia: {
                validators: {
                     stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese el nombre de la ciudad'
                    }
                }
            },
            parroquia_residencia: {
                validators: {
                     stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese el nombre de la parroquia'
                    }
                }
            },
            tipo_parroquia: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },            
            barrio: {
                validators: {
                     stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese el nombre del barrio'
                    }
                }
            },
            zona: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },             
            direccion_principal: {
                validators: {
                     stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese la calle principal'
                    }
                }
            },
            direccion_secundaria: {
                validators: {
                     stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese la calle secundaria'
                    }
                }
            },
            direccion_numero: {
                validators: {
                     stringLength: {
                        min: 1,
                        message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese el número'
                    }
                }
            },                       
            telefono_casa: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su teléfono de casa'
                    },
                    regexp: {
                        regexp: /^[0][0-9]{8}$/i,
                        message: 'Ingrese el teléfono con formato 026017070'
                    }
                }
            }, 
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
 
});

