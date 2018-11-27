#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from django.core.exceptions import ValidationError
    
def validate_file_extension(value):   
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.bmp', '.gif', '.jpg', '.jpeg', '.tif', '.tiff', '.png', '.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'No se puede cargar el documento con esa extensión.')