
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
                    },
                    lessThan: {
                        value: "2147483647 ",
                        message: "Ingrese un número menor a 2147483647 ."
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
                    },
                    lessThan: {
                        value: "2147483647 ",
                        message: "Ingrese un número menor a 2147483647 ."
                    }                    
                }
            },
            telefono_trabajo: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su teléfono de trabajo'
                    },


                    regexp: {
                        regexp: /^[0][0-9]{8}$/i,
                        message: 'Ingrese el teléfono con formato 026017070'
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
                    regexp: {
                        regexp: /^[0][0-9]{9}$/i,
                        message: 'Ingrese el teléfono con formato 0920304050'
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
                        message: 'Ingrese su teléfono de trabajo'
                    },
                    regexp: {
                        regexp: /^[0][0-9]{8}$/i,
                        message: 'Ingrese el teléfono con formato 026017070'
                    }
                },
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
            }
        }/**/
 
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

