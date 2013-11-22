## coding: utf-8
#from django import template
#import urllib, hashlib
#
#register = template.Library()
#
#@register.inclusion_tag('mostrar.html')
#def mostrar_depoimento():
#    return {
#        'depoimento':Depoimento.objects.all().order_by('?')[0]
#    }
#
#
## import code for encoding urls and generating md5 hashes
#
#
## Set your variables here
#email = "someone@somewhere.com"
#default = "http://www.example.com/default.jpg"
#size = 40
#
## construct the url
#gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
#gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
#
