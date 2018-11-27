
$(document).ready(function() {
   
    $('#gastos-form').bootstrapValidator({
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
            gastos_vivienda: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese un número'
                    },
                    regexp: {
                        regexp: /^[0-9]+$/i,
                        message: 'Ingrese un número positivo sin separadores.'
                    },
                    lessThan: {
                        value: "2147483647 ",
                        message: "Ingrese un número menor a 2147483647 ."
                    }
                }
            },
            gastos_educacion: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese un número'
                    },
                    regexp: {
                        regexp: /^[0-9]+$/i,
                        message: 'Ingrese un número positivo sin separadores.'
                    },
                    lessThan: {
                        value: "2147483647 ",
                        message: "Ingrese un número menor a 2147483647 ."
                    }

                }
            },
            gastos_alimentacion: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese un número'
                    },
                    regexp: {
                        regexp: /^[0-9]+$/i,
                        message: 'Ingrese un número positivo sin separadores.'
                        
                    },
                    lessThan: {
                        value: "2147483647 ",
                        message: "Ingrese un número menor a 2147483647 ."
                    }
                

                }
            },
            gastos_transporte: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese un número'
                    },
                    regexp: {
                        regexp: /^[0-9]+$/i,
                        message: 'Ingrese un número positivo sin separadores.'
                    },
                    lessThan: {
                        value: "2147483647 ",
                        message: "Ingrese un número menor a 2147483647 ."
                    }
                

                }
            },
            gastos_salud: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese un número'
                    },
                    regexp: {
                        regexp: /^[0-9]+$/i,
                        message: 'Ingrese un número positivo sin separadores.'
                    }
                

                }
            },          
            gastos_vestimenta: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese un número'
                    },
                    regexp: {
                        regexp: /^[0-9]+$/i,
                        message: 'Ingrese un número positivo sin separadores.'
                    },
                    lessThan: {
                        value: "2147483647 ",
                        message: "Ingrese un número menor a 2147483647 ."
                    }
                }
            },              
            gastos_otros: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese un número'
                    },
                    regexp: {
                        regexp: /^[0-9]+$/i,
                        message: 'Ingrese un número positivo sin separadores.'
                    },
                    lessThan: {
                        value: "2147483647 ",
                        message: "Ingrese un número menor a 2147483647 ."
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
