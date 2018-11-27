
$(document).ready(function() {
   
    $('#integrante-form').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            nombres_completos: {
                validators: {
                        stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                        notEmpty: {
                        message: 'Ingrese nombres y apellidos'
                    }
                }
            },
            actividad: {
                validators: {
                        stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                        notEmpty: {
                        message: 'Ingrese su actividad'
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
            pais_nacimiento: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            },
            parentesco: {
                validators: {
                     stringLength: {
                        min: 2,
                        message:'Información no válida'
                    },
                    notEmpty: {
                        message: 'Ingrese el parentesco'
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
            nivel: {
                validators: {
                        notEmpty: {
                        message: 'Seleccione una opción'
                    }

                }
            },
        }
    })
    /**.on('success.form.bv', function(e) {
        $('#success_message').slideDown({ opacity: "show" }, "slow") // Do something ...
            $('#representante-form').data('bootstrapValidator').resetForm();

            e.preventDefault();

            var $form = $(e.target);

            var bv = $form.data('bootstrapValidator');

            $.post($form.attr('action'), $form.serialize(), function(result) {
                console.log(result);
            }, 'json');
    });**/

})
