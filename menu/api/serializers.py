from rest_framework import serializers

from menu.models import StaticPages


class StaticPagesSerializer(serializers.ModelSerializer):
	class Meta:
		model = StaticPages
		fields = '__all__'
