
$(document).ready(function() {
   
    $('#estudiante-form').bootstrapValidator({
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
            genero: {
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
            nivel: {
                validators: {
                        notEmpty: {
                        message: 'Seleccione una opción'
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

