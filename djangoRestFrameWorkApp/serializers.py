from rest_framework import serializers
from .models import Student,Teacher
import re

class StudentSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)
    roll_no = serializers.IntegerField()
    grade  = serializers.IntegerField()
    age = serializers.IntegerField()
    email = serializers.EmailField()
    address = serializers.CharField(max_length=200)
    phone = serializers.CharField(max_length=20)


    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll_no = validated_data.get('roll_no', instance.roll_no)
        instance.grade = validated_data.get('grade', instance.grade)
        instance.age = validated_data.get('age', instance.age)
        instance.email = validated_data.get('email', instance.email)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance




################  Field Level Validation ###########################    
    # def validate_roll(self,value):
    #     if value >= 500:
    #         raise serializers.ValidationError("Roll number should be less than 500")
    #     return value

    # def validate_name(self,value):
    #     if  (any(map(str.isdigit, value))):
    #         raise serializers.ValidationError("Name should not be numeric")
    #     return value

    # def validate_grade(self,value):
    #     if (value > 12):
    #         raise serializers.ValidationError("Grade should be less than 12")
    #     return value

    # def validate_age(self,value):
    #     if (value < 23):
    #         raise serializers.ValidationError("Age should be greater than 18")
    #     return value

    # def validate_phone(self,value):
    #     Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
    #     if (Pattern.match(value) == None):
    #         raise serializers.ValidationError("Phone number should be valid")
    #     return value

    # def validate_email(self,value):
    #     Pattern = re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    #     if (Pattern.match(value) == None):
    #         raise serializers.ValidationError("Email should be valid")
    #     return value


################### Object Level Validation ########################
    def validate(self,data):
        phonePattern = re.compile("(0|91)?[7-9][0-9]{9}")
        emailPattern = re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

        if  (any(map(str.isdigit, data.get('name')))):
            raise serializers.ValidationError("Name should not be numeric")
        
        elif data.get('roll_no') >= 500:
            raise serializers.ValidationError("Roll number should be less than 500")
    
        elif (data.get('grade') > 12):
            raise serializers.ValidationError("Grade should be less than 13")

        elif (data.get('age') > 25):
            raise serializers.ValidationError("Age should be less than 26")
        
        elif (phonePattern.match(data.get('phone')) == None):
            raise serializers.ValidationError("Phone number should be valid")
        
        elif (emailPattern.match(data.get('email')) == None):
            raise serializers.ValidationError("Email should be valid")
        
        return data




################ Validation using function ########################
# Advantage this can be used across different serializers
# can we used as utility

def validate_phone(phoneno):
    phonePattern = re.compile("(0|91)?[7-9][0-9]{9}")
    if (phonePattern.match(phoneno) == None):
        raise serializers.ValidationError("Email should be valid")
    return phoneno

        

              



class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id','name','email','age','subject_teaches','phone')
        read_only_fields = ('id',)
        # exclude = ('created_at','updated_at')
