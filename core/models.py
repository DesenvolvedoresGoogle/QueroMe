# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from random import sample
from string import ascii_letters, join
from django.core.urlresolvers import reverse
from django.core.mail import send_mail

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    verifying_code = models.CharField(max_length=40,unique=True,blank=True,null=True)
    def create_verifying_code(self):
        #Unique Verifying code
        flag = True
        while flag:
            verifying_code = join(sample(ascii_letters,40),"")
            users = User.objects.filter(verifying_code = verifying_code)
            if not users:
                self.verifying_code = verifying_code
                self.save()
                flag = False
    def enviar_email_ativacao(self):
        link = reverse('ativacao-cadastro',
            kwargs={
                'id':self.id,
                'verifying_code':self.verifying_code,
                }
        )
        mensagem_txt = u"""Bem vindo(a) Usuário %s %s,

                        Parabéns! Você acaba de se tornar nosso usuário !
                        É muito importante sua opinião para melhoria desta plataforma.
                        Seu cadastro foi efetuado com sucesso e você está a um passo de poder receber excelentes ofertas e preços
                        Por favor, ative sua conta. Para isso, clique no link abaixo para ativar o seu cadastro:

                        %s

                        Obrigado, e aproveite!
                        Equipe quero.me """
        mensagem_txt = mensagem_txt % (self.user.first_name,self.user.last_name,link)
        send_mail('[Quero.me]  Obrigado por se cadastrar',mensagem_txt,'contato@quero.me',[self.user.email])
    def save(self, *args, **kwargs):
        if not self.id and not self.user.is_active:
            #Se é a primeira vez é preciso gerar o código de verificação e enviar o e-mail de ativação
            super(UserProfile,self).save(*args,**kwargs)
            self.create_verifying_code()
            self.enviar_email_ativacao()
        super(UserProfile,self).save(*args,**kwargs)

class Categorie(models.Model):
    category = models.CharField(max_length=200)

class Wishlist(models.Model):
    user = models.ForeignKey(User)
    category =models.ForeignKey(Categorie, blank=True, null=True)
    product = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)