from rest_framework import serializers

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

class PublicPageOutSerializer(serializers.Serializer):
    '''
    page: {
      nuid: 1231,
      sid: "begum_rokey_univ",
      title: "Department of Computer Science and Engineering",
      subtitle: "One of the Departments at Begum Rokeya University, Rangpur",
      contact: "",
      short_description: "",
      quick_overview: "It is founded in 2008. At present 250 students are enrolled in this discipline. There are 10 world class faculty memebers.",
      lastest_events: [
        { title: "News: CSE BRUR started using IMS system.", details_link: "#" },
        { title: "Event: Inter batch programming contest on sunday, 9th oct.", details_link: "#" },
        { title: "Circular: Admission is open", details_link: "#" },
        { title: "Notice: New Policy for Scholarship.", details_link: "#" }
      ],
      sections: [
        { nuid: 1, comid: "contact", description: "Contact us" },
        { nuid: 2, comid: "gallery", description: "Visit galleries" },
        { nuid: 3, comid: "events", description: "Show events" },
        { nuid: 4, comid: "notices", description: "Can't find what I'm looking for." }
      ]
    }
    '''
    pass

class ServicesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()


class ServiceRequestSerializer(serializers.Serializer):
    service_name = serializers.CharField()
    task = serializers.JSONField()
