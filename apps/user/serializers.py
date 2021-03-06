from rest_framework import serializers

from apps.relation.models import PersonRelations
from apps.user.models import User, Visitor
from apps.relation.serializers import PersonRelationsSerializer

class UserSerializer(serializers.ModelSerializer):
    relations = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ('password', 'last_login', 'is_superuser', 'date_joined', 'groups', 'user_permissions')

    def get_relations(self, obj):
        try:
            user = self.context['request'].user
            if user is not None:
                relations = PersonRelations.objects.get_or_create(act_one=user, target_one=obj)[0]
                return PersonRelationsSerializer(relations).data
        except Exception as e:
            print(e)
            return {}


class SelfSerializer(serializers.ModelSerializer):
    relations_obj = serializers.SerializerMethodField()
    fresh_notices = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ('password', 'last_login', 'is_superuser', 'date_joined', 'groups', 'user_permissions')

    def get_relations_obj(self, obj):
        user = self.context['request'].user
        if user is not None and user.is_active:
            friend_list = []
            block_list = []
            relation_list = PersonRelations.objects.filter(act_one=user)
            for relation in relation_list:
                user = relation.target_one
                if relation.is_follow:
                    friend_list.append(user)
                if relation.is_block:
                    block_list.append(user)

            relations_obj = {
                "friendList": UserSerializer(friend_list, many=True).data,
                "blockList": UserSerializer(block_list, many=True).data
            }
            return relations_obj


class UserSimpleSerializer(serializers.ModelSerializer):
    relations = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'avatar', 'fullname', 'relations']

    def get_relations(self, obj):
        user = self.context['request'].user
        if user is not None and user.is_active:
            relations = PersonRelations.objects.get_or_create(act_one=user, target_one=obj)[0]
            return PersonRelationsSerializer(relations).data
        return []


class UserMinimalismSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']




class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = '__all__'
