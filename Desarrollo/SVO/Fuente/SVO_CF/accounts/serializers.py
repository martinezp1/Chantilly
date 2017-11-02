from django.contrib.auth.models import Group
from django.db import transaction
from rest_framework import serializers
from accounts.models import User

__author__ = 'chris01'


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'cellphone', 'is_joined')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    @transaction.atomic
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        if user.is_joined:
            user.is_staff = True
            user.is_admin = True
        user.save()
        if user.is_joined:
            (group, is_created) = Group.objects.get_or_create(name='Propietarios')
            group.user_set.add(user)
        else:
            (group, is_created) = Group.objects.get_or_create(name='Suscritos')
            group.user_set.add(user)
        return user
