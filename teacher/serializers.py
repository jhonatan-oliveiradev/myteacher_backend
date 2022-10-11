from rest_framework import serializers

from teacher.models import Professor, Aula


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class CadastrarAulaSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    nome = serializers.CharField(max_length=100)

    def validate_nome(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Nome deve ter pelo o menos 3 caracteres")
        return value

    def validate_email(self, value):
        if '@' not in value:
            raise serializers.ValidationError(
                "Por favor, insira um email válido")
        return value


class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'
