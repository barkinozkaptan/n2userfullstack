from rest_framework import serializers

# user/serializers.py
from core_user.models import User, Address, Geo, Company


class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = ['lat', 'lng']

class AddressSerializer(serializers.ModelSerializer):
    geo = GeoSerializer()
    class Meta:
        model = Address
        fields = ['street', 'suite', 'city', 'zipcode', 'geo']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):

    address = AddressSerializer()
    company = CompanySerializer()
    
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'phone', 'website', 'address', 'company']

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        company_data = validated_data.pop('company')
        geo_data = address_data.pop('geo')
        
        geo = Geo.objects.create(**geo_data)
        address = Address.objects.create(geo=geo, **address_data)
        company = Company.objects.create(**company_data)
        
        user = User.objects.create(address=address, company=company, **validated_data)
        return user

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)
        company_data = validated_data.pop('company', None)

        if address_data:
            geo_data = address_data.pop('geo', None)
            if geo_data:
                for attr, value in geo_data.items():
                    setattr(instance.address.geo, attr, value)
                instance.address.geo.save()
            for attr, value in address_data.items():
                setattr(instance.address, attr, value)
            instance.address.save()

        if company_data:
            for attr, value in company_data.items():
                setattr(instance.company, attr, value)
            instance.company.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
    
