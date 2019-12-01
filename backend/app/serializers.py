from rest_framework.serializers import ModelSerializer

from .models import Entry


class EntrySerializer(ModelSerializer):
    '''Serializer for Entry model
    '''

    class Meta:
        model = Entry
        fields = '__all__'
