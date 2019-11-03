from rest_framework import serializers
class JabinSerializer(serializers.Serializer):
  greetings = serializers.CharField()
class JabinSerializer2(serializers.Serializer):
  greetings = serializers.CharField()
class JabinSerializer3(serializers.Serializer):
  greetings = serializers.CharField()
class JabinSerializer4(serializers.Serializer):
  greetings = serializers.CharField()

class JabinParameterInput(serializers.Serializer):
    num1 = serializers.IntegerField()
    num2 = serializers.IntegerField()


class jabinParameterOutput(serializers.Serializer):
    sum = serializers.IntegerField()


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})
    name = serializers.CharField()
    phone_no = serializers.CharField(required=False)

class RegistrationOutputSerializer(serializers.Serializer):
    status_code = serializers.CharField()
    default_description = serializers.CharField()

class LoginInputSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})
    cookie = serializers.CharField(required=False)

class PublicPageSerializer(serializers.Serializer):
    page_title = serializers.CharField()
    type_of_institute = serializers.CharField()
    founding_date = serializers.CharField()
    address_district = serializers.CharField()
    address_upozila = serializers.CharField()
    no_of_stakeholder = serializers.CharField()
    description = serializers.CharField()

class ServicesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()


class ServiceRequestSerializer(serializers.Serializer):
    service_name = serializers.CharField()
    task_name = serializers.CharField()
    data = serializers.CharField()
