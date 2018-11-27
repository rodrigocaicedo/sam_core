
$(document).ready(function() {
   
    $('#contact_form').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            representante: {
                validators: {
                        stringLength: {
                        min: 8,
                        message:'Información no válida'
                    },
                        notEmpty: {
                        message: 'Ingrese los nombres completos'
                    }
                }
            },
            reunion: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            }
        }   
        });
    $('#contact_form2').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            estudiante: {
                validators: {
                        stringLength: {
                        min: 8,
                        message:'Información no válida'
                    },
                        notEmpty: {
                        message: 'Ingrese los nombres completos'
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
            relacion: {
                validators: {
                    notEmpty: {
                        message: 'Seleccione una opción'
                    }
                }
            }
        }   
        })

});

$(function() {
    $(".datepicker").datepicker({autoclose:true, format: 'yyyy-mm-dd'});
});



$('#submit_estudiante').click(function(){
   $('#contact_form2').attr('action', '/registro/estudiante/');
});

$('#submit_estudiante_fin').click(function(){
   $('#contact_form2').attr('action', '/registro/estudiante_fin/');
});

