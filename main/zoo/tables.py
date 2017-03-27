import django_tables2 as tables
from .models import Cage

class CageTable(tables.Table):
    created_at = tables.Column(attrs={"td": {"align": "left"}})
    name = tables.Column(attrs={"td": {"align": "left"}})
    zoo = tables.Column(attrs={"td": {"align": "left"}})

    class Meta:
        model = Cage
        attrs = {'class': 'paleblue','width':'50%'}