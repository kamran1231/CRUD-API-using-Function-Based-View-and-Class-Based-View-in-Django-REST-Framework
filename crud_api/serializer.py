
from rest_framework import serializers
from .models import Student

#Model Serializer class:
class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['id','name','roll','city']
        # read_only_fields = ['name','roll']
        extra_kwargs = {'name':{'read_only':True}}


















# #Validators
# def starts_with_r(value):
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError('Name should be start with r')




# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100, validators=[starts_with_r])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)
#
#     #Post method
#     def create(self,validated_data):
#         return Student.objects.create(**validated_data)
#
#
#     #update method:
#     def update(self,instance,validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.roll = validated_data.get('roll',instance.roll)
#         instance.city = validated_data.get('city',instance.city)
#         instance.save()
#         return instance

    #field_level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat full')
        return value


    #object_level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rahul' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('city must be ranchi')
        return data