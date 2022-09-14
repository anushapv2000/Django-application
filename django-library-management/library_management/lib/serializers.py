from dataclasses import field, fields
from rest_framework import serializers
from lib.models import library

class libraryserializers(serializers.ModelSerializer):
    class Meta:
        model=library
        fields=('userid','bookname','username','issuedate')

