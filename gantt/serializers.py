from .models import Task
from .models import Link
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    end_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Task
        fields = ('id', 'text', 'start_date', 'end_date', 'duration', 'progress', 'parent', 'sort_order')


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = ('id', 'source', 'target', 'type', 'lag')
