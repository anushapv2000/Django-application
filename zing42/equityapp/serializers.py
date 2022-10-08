from rest_framework import serializers
from equityapp.models import equity1

class equityserializers(serializers.ModelSerializer):
    class Meta:
        model=equity1
        fields=('SYMBOL', 'NAME_OF_COMPANY', 'SERIES','DATE_OF_LISTING','PAID_UP_VALUE', 'MARKET_LOT', 'ISIN_NUMBER', 'FACE_VALUE')