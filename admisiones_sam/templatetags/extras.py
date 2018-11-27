
from django import template
register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})

@register.filter(name='addplaceholder')
def addplaceholoder(field, placeholder):
   return field.as_widget(attrs={"placeholder":placeholder})

@register.filter(name='add_attributes')
def add_attributes(field, css):
    attrs = {}
    definition = css.split(',')

    for d in definition:
        if ':' not in d:
            attrs["class"] = d
        else:
            t, v = d.split(':')
            attrs[t] = v

    return field.as_widget(attrs=attrs)
 

@register.filter(name='SplitNombres')
def SplitNombres(nombre):

 
    tokens = nombre.split(" ")
    
    q_nombres = "+".join(tokens)
 
    return (q_nombres)

