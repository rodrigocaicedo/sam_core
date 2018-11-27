#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from admisiones_sam import views
#def

urlpatterns = [
    #Inicio eer
    url(r'^Inicio/$',views.Home, name='Inicio'),
   
    #Solicitud
    
    url(r'^NuevaSolicitud/$',views.Applications_new, name='NuevaSolicitud'), #para representantes creacion de la solicitud de admisiones de estudiantes sin hermanos
    url(r'^NuevaSolicitudHermanos/$',views.Applications_newCH, name='NuevaSolicitudHermanos'), #para representantes creacion de la solicitud de admisiones de estudiantes con Hermanos
    url(r'^SeleccionaTour/$',views.Tours_select, name='SeleccionaTour'),  #para representantes seleccion de la fecha de Tour
    url(r'^MensajeSolicitud/$',views.AppMessage, name='MensajeSolicitud'), #mensaje de exito al representante
    url(r'^MensajeSolicitudHermanos/$',views.AppMessageCH, name='MensajeSolicitudHermanos'), #mensaje de exito al representante, hijos con hermanos
    url(r'^MensajeSolicitudEstado/$',views.AppMessageState, name='MensajeSolicitudEstado'), #Mensaje al representante con fecha tour otra
    url(r'^EditarSolicitud/(?P<id_applications>\d+)/$', views.Applications_edit, name='EditarSolicitud'),  #edita la informacion de la solicitud para manejo del representante
    url(r'^ConsultarSolicitud/(?P<id_applications>\d+)/$', views.Applications_Select, name='ConsultarSolicitud'),  #edita la informacion de la solicitud para manejo del representante
    url(r'^EliminaAplicacion/(?P<id_applications>\d+)/$', views.DeleteApplications, name='EliminaAplicacion'), 
    
   #Administracion 
    url(r'^Administracion/$',views.Administration, name='Administracion'), # maneja la informacion de las solicitudes para manejo de admisiones
    url(r'^EditarTipoAplicante/(?P<id_applications>\d+)/$',views.EditTypeApplicant, name='EditarTipoAplicante'),
    
    #Tours
    url(r'^EditarFechaTour/(?P<id_applications>\d+)/$', views.DateTourUpdate, name='EditarFechaTour'), 
    url(r'^TipoTour/$',views.TypeTours, name='TipoTour'), # creacion de un nuevo registro de fecha de tour cuando se reagenda fecha de toour a un solicitante
    url(r'^MantenerTipoTour/$',views.KeepTypeTour, name='MantenerTipoTour'), # Mantenimiento de la tabla Type_Tour ingreso, editar eliminar, consultar
    url(r'^EliminaTipoTour/(?P<id_typetour>\d+)/$', views.DeleteTypeTours, name='EliminaTipoTour'),  
    url(r'^EditaTipoTour/(?P<id_typetour>\d+)/$', views.EditTypeTours, name='EditaTipoTour'), # edita la informacion de la tabla Type_Tour
    url(r'^RecordatorioTour/$', views.ToursMassiveEmails, name='RecordatorioTour'), # envia notificaciones masivas para recordar las fechas de tour.
    
   
   #Test
    url(r'^MantenerTipoTest/$',views.KeepTypeTest, name='MantenerTipoTest'), # Mantenimiento de la tabla Type_Test ingreso, editar eliminar, consultar
    url(r'^EliminaTipoTest/(?P<id_typetest>\d+)/$', views.DeleteTypeTest, name='EliminaTipoTest'),  
    url(r'^EditaTipoTest/(?P<id_typetest>\d+)/$', views.EditTypeTest, name='EditaTipoTest'), # edita la informacion de la tabla Type_Test
    url(r'^SeleccionaFecha/(?P<id_applications>\d+)/$', views.SelectDateTest, name='SeleccionaFecha'), # edita la informacion de la tabla fechas evaluaciones
    url(r'^TipoTest/(?P<id_applications>\d+)/$',views.TypeTest, name='TipoTest'), # creacion de un nuevo registro de fecha de test cuando se reagenda fecha de test a un solicitante
    url(r'^RecordatorioTest/$', views.TestMassiveEmails, name='RecordatorioTest'), # envia notificaciones masivas para recordar las fechas de Evaluaciones.
   
   
   #Consultas 
    url(r'^ListaAplicantes/$', views.ListApplicant, name='ListaAplicantes'),
    url(r'^BuscaAplicantes/$', views.SearchApplicant, name='BuscaAplicantes'),
    url(r'^ListaEstudiantes/$', views.ListStudent, name='ListaEstudiantes'),
    url(r'^ListaUsuariosEstudiantes/$', views.ListUserStudents, name='ListaUsuariosEstudiantes'),
    url(r'^BuscaEstudiantes/$', views.SearchStudent, name='BuscaEstudiantes'),
    
   #Auxiliares
    url(r'^PaginaColegio/$', views.ReturnHome, name='PaginaColegio'),
   
    
    
   #Periodos
   url(r'^MantenerPeriodos/$',views.KeepPeriod, name='MantenerPeriodos'), # Mantenimiento de la tabla Periodos, ingreso, editar eliminar, consultar
   url(r'^EliminaPeriodos/(?P<per_id>\d+)/$', views.DeletePeriod, name='EliminaPeriodos'),  
   url(r'^EditaPeriodos/(?P<per_id>\d+)/$', views.EditPeriod, name='EditaPeriodos'), # edita la informacion de la tabla Periodos
   
   #Estados Aplicaciones
   url(r'^CambiaEstados/(?P<id_applications>\d+)/$', views.ChangeState, name='CambiaEstados'), # permite cambiar los estados
   
   #Cupos
   url(r'^MantenerCupos/$',views.KeepQuotas, name='MantenerCupos'), # Mantenimiento de la tabla Quotas, ingreso, editar eliminar, consultar
   url(r'^EditaCupos/(?P<id_quotas>\d+)/$', views.EditQuotas, name='EditaCupos'), # edita la informacion de la tabla Quotas
   url(r'^EliminaCupos/(?P<id_quotas>\d+)/$', views.DeleteQuotas, name='EliminaCupos'),  
   
   #Mails
   url(r'^MantenerMails/$',views.KeepMails, name='MantenerMails'), # Mantenimiento de la tabla Mails, ingreso, editar eliminar, consultar
   url(r'^EditaMails/(?P<id_mails>\d+)/$', views.EditMails, name='EditaMails'), # edita la informacion de la tabla Mails
   url(r'^EliminaMails/(?P<id_mails>\d+)/$', views.DeleteMails, name='EliminaMails'),  
   
   #Facturas
   url(r'^MantenerFacturas/$',views.KeepInvoices, name='MantenerFacturas'), # Mantenimiento de la tabla Invoices, ingreso, editar eliminar, consultar
   url(r'^EditaFacturas/(?P<id_invoice>\d+)/$', views.EditInvoices, name='EditaFacturas'), # edita la informacion de la tabla Invoices
   url(r'^EliminaFacturas/(?P<id_invoice>\d+)/$', views.DeleteInvoices, name='EliminaFacturas'),  
   url(r'^CreaFactura/(?P<id_applications>\d+)/$',views.CreateInvoices, name='CreaFactura'), # Pantalla que se envia a los representantes para ingreso de datos de facturacion
   url(r'^NuevaFactura/(?P<id_applications>\d+)/$',views.NewInvoices, name='NuevaFactura'), # Pantalla para que el usuario del sistema cree un nuevo registro de datos de facturacion

   # Niveles o Grados
   url(r'^MantenerGrados/$', views.KeepGrade, name='MantenerGrados'),  #Pantalla para dar mantenimiento a la informacion de niveles o grados academicos
   url(r'^EditaGrados/(?P<id_typegrade>\d+)/$', views.EditGrade, name='EditaGrados'), # edita la informacion de la tabla type_grade
   url(r'^EliminaGrados/(?P<id_typegrade>\d+)/$', views.DeleteGrade, name='EliminaGrados'),  
   
   
   #Forms  Formularios de informacion que deben completar los padres de familia
   url(r'^Formulario/(?P<id_applications>\d+)/$', views.NewForms, name='Formulario'),  #Ingreso de informacion completa del estudiante (no esta en uso)
   url(r'^FormularioEstudiantes/(?P<id_applications>\d+)/$', views.NewFormsStudents, name='FormularioEstudiantes'),  #Ingreso de informacion completa del estudiante ingreso nuevo formato usuarios
   url(r'^EditaFormularioEstudiantes/$', views.EditFormsStudents, name='EditaFormularioEstudiantes'),  #Edicion de informacion completa del estudiante ingreso nuevo formato usuarios
   url(r'^MensajeFormularioActualiza/$',views.FormsMessageSave, name='MensajeFormularioActualiza'), #Mensaje de confirmacion a los representantes
   url(r'^EditaFormulario/$', views.EditForms, name='EditaFormulario'),  #Consulta para actualizar de informacion completa del estudiante (no esta en uso)
   url(r'^EditaFormularioGuarda/$', views.EditFormsPost, name='EditaFormularioGuarda'),  #Actualiza de informacion completa del estudiante
   
   
   #Evaluaciones
   url(r'^MantenerEvaluaciones/$', views.KeepTest, name='MantenerEvaluaciones'),  #Mantenimiento y registro de evaluaciones por parte de psicologia
   url(r'^ConsultarEvaluaciones/$', views.SearchTest, name='ConsultarEvaluaciones'),  #Consultar  evaluaciones
   url(r'^EditarEvaluaciones/(?P<id_test>\d+)/$', views.EditTest, name='EditarEvaluaciones'),  #Edita  reportes de evaluaciones
   url(r'^EvaluacionesEstudiante/$', views.TestStudent, name='EvaluacionesEstudiante'),  #Mantenimiento a la tabla Test
   url(r'^EditarEvaluacionesEstudiante/(?P<id_test>\d+)/$', views.EditTestStudent, name='EditarEvaluacionesEstudiante'),  #Editar la tabla Test
   url(r'^AprobarEvaluaciones/$', views.ApproveTest, name='AprobarEvaluaciones'),  #Aprobacion de las evaluaciones por admisiones
   url(r'^ResumenEvaluaciones/(?P<id_typetest_id>\d+)/(?P<id_report>\d+)/$', views.SummaryTest, name='ResumenEvaluaciones'),  #Resumen del tipo y resultados de la evaluacion
   
   
   
   
   # Documentacion
   url(r'^MantenerDocumentos/$', views.KeepDocuments, name='MantenerDocumentos'),  #Mantenimiento y registro de Documentos como requisitos
   url(r'^EditaDocumentos/(?P<id_doctype>\d+)/$', views.EditDocuments, name='EditaDocumentos'), # edita la informacion de la tabla Documents_Types
   url(r'^EliminaDocumentos/(?P<id_doctype>\d+)/$', views.DeleteDocuments, name='EliminaDocumentos'),  
   url(r'^CargaDocumentos/$', views.ListUploadDocuments, name='ListaCargaDocumentos'),
   url(r'^CargaDocumentos/(?P<id_applications>\d+)/$', views.UploadDocuments, name='CargaDocumentos'),  #pantalla en la que los representantes suben la documentacion requerida
   url(r'^EnviaDocumentos/$', views.SendDocuments, name='EnviaDocumentos'),  #pantalla en la que se envia a los representantes el comunicado que estan errados los documentos a que vuelva a cargar
   url(r'^CambiaDocumentos/(?P<id_applications>\d+)/$', views.UploadEditDocuments, name='CambiaDocumentos'),  #pantalla en la que los representantes vuelve a subir la documentacion errada
   url(r'^ValidaDocumentos/$', views.CheckDocuments, name='ValidaDocumentos'),  #pantalla de validacion de docuementos por Admisiones   
   url(r'^VerDocumentos/$', views.ViewDocuments, name='VerDocumentos'),  #pantalla de validacion de docuementos por Admisiones   
   url(r'^CorrigeDocumentos/(?P<id_detdoc>\d+)/$', views.ChangeDocuments, name='CorrigeDocumentos'),   
   url(r'^MailCorrigeDocumentos/(?P<id_applications>\d+)/$', views.MailChangeDocuments, name='MailCorrigeDocumentos'), 
   url(r'^DocumentosPorValidar/$', views.KeepValidaDocuments, name='DocumentosPorValidar'),    

   
   #Aprobaciones Contabilidad
   url(r'^AprobarContabilidad/$', views.ApproveAccounting, name='AprobarContabilidad'),  #pantalla que permite al departamento de contabilidad ingresar el acuerdo financiero y aprobar al aplicante cuando pago la matricula
   url(r'^AprobarContabilidadEvaluaciones/$', views.ApproveAccountingTest, name='AprobarContabilidadEvaluaciones'),  #pantalla que permite al departamento de contabilidad registrar el pago de las evaluaciones.
   
   #Aprobaciones Secretaria
   url(r'^AprobarSecretaria/$', views.ApproveSecretary, name='AprobarSecretaria'),  #pantalla que permite al departamento de secretaria academica luego de revisar el formulario de datos aprobar al aplicante
   
   
   #Reportes Admisiones
         
    url(r'^ListaTour/$', views.ReportListTour, name='ListaTour'), #Pantalla de parametros
    url(r'^ListaTourxlsx/(?P<fecha>\d+-\d+-\d+)/$', views.ReportListTour_xlsx, name='ListaTourxlsx'),  #reporte en excel
    
    url(r'^ListaEvaluaciones/$', views.ReportListTest, name='ListaEvaluaciones'), #Pantalla de parametros
    url(r'^ListaEvaluacionesxlsx/(?P<fecha>\d+-\d+-\d+)/$', views.ReportListTest_xlsx, name='ListaEvaluacionesxlsx'),  #reporte en excel
    
    url(r'^ResumenAplicaciones/$', views.SummaryApplications, name='ResumenAplicaciones'), #Pantalla de parametros
    url(r'^ResumenAplicacionesxlsx/(?P<fecha>\d+-\d+-\d+)/$', views.SummaryApplications_xlsx, name='ResumenAplicacionesxlsx'),  #reporte en excel
    


  #Borrar
   #url(r'^prueba4/$',views.prueba4, name='prueba4'), #borrar es para pruebas
]
urlpatterns += staticfiles_urlpatterns()
