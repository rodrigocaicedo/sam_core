
$('#contact_form').bootstrapValidator({
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

        seccion: {
            trigger: 'change keyup',
            validators: {
                notEmpty: {
                    message: 'Seleccione una opción'
                }
            }
        },

        
        area: {
            trigger: 'change keyup',
            validators: {
                notEmpty: {
                    message: 'Seleccione una opción'
                }
            }
        },
        comentarios: {
            validators: {
                    stringLength: {
                    min: 10,
                    message:'Información no válida'
                },
                    notEmpty: {
                    message: 'Por favor, cuéntenos un poco sobre su interés en trabajar con nosotros.'
                }
            }
        },            
        telefono: {
            validators: {
                notEmpty: {
                    message: 'Ingrese su número de teléfono'
                },
                stringLength: {
                    min: 9,
                    max: 10,
                    message:'Ingrese un teléfono fijo o celular'
                }
            }
        },
        correo: {
            validators: {
                notEmpty: {
                    message: 'Ingrese su correo electrónico'
                },
                emailAddress: {
                    message: 'Ingrese un correo electrónico válido'
                }
            }
        }
    }
})
.on('success.form.bv', function(e) {
            if($(".jFiler-item").length == 0){
            e.preventDefault();
                alert("Por favor, cargue al menos un archivo para proceder con el envío del formulario.");
                $("#contact_form").data("bootstrapValidator").resetForm();
            };
})
.on('status.field.bv', function(e, data) {
// I don't want to add has-success class to valid field container
//data.element.parents('.form-group').removeClass('has-success');
// I want to enable the submit button all the time
data.bv.disableSubmitButtons(false);
});
//    $('#success_message').slideDown({ opacity: "show" }, "slow") // Do something ...
//        $('#contact_form').data('bootstrapValidator').resetForm();

        // Prevent form submission
//        e.preventDefault();

        // Get the form instance
//        var $form = $(e.target);

        // Get the BootstrapValidator instance
//        var bv = $form.data('bootstrapValidator');

    // Use Ajax to submit form data
//        $.post($form.attr('action'), $form.serialize(), function(result) {
//            console.log(result);
//        }, 'json');
//});


