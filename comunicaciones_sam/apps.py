from __future__ import unicode_literals

from django.apps import AppConfig


class ComunicacionesSamConfig(AppConfig):
    name = 'comunicaciones_sam'

    def ready(self):
        from comunicaciones_sam import receivers
