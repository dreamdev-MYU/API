from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


    def validate_phone_number(self, value):
        if not value.startswith("+998"):
            raise serializers.ValidationError("Phone number  '+998' bilan bolishi kerak")
        
        if len(value) != 13:
            raise serializers.ValidationError(" Phone number notogri kiritildi ")
        
        if not value[1:].isdigit():
            raise serializers.ValidationError("Phone number raqamlardan iboratligiga tekshiring")
        return value


    def validate_location(self, value):

        if value not in dict(Student.LOCATION_TYPE_CHOISE).keys():
            raise serializers.ValidationError("Joy ttopilmadi.")
        return value

