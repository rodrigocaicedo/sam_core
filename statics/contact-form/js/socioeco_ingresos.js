
$(document).ready(function() {
   
    $('#ingresos-form').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            dependencias: {
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
            negocios: {
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
            inversiones: {
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
            arriendos: {
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
            otros_ingreso: {
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
     