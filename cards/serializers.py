from rest_framework import serializers
from .models import Card
from users.serializers import UserSerializer
from django.contrib.auth.models import User




class CardSerializer(serializers.ModelSerializer):
    card_number = serializers.CharField(write_only=True)
    ccv = serializers.CharField(write_only=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        source='user',
    )

    class Meta:
        model = Card
        fields =  '__all__'

    

    def create(self, validated_data):
        censored_number = f'{validated_data['card_number'][0:4]}{ '*' * 8}{validated_data['card_number'][12:16]}'
        card = Card.objects.create(
            title=validated_data['title'],
            user = validated_data['user'],
            censored_number=censored_number,
            is_valid=True,
        )
        return card


    def validate(self, data):
        card_number = data['card_number']
        ccv = data['ccv']
       
        
        if not card_number.isdigit() or not len(card_number) == 16:
            raise serializers.ValidationError("Invalid Card Number")
             
        
        if not ccv.isdigit() or not 100 <= int(ccv) <= 999:
            raise serializers.ValidationError("Invalid Card CCV")
                

        ccv = int(ccv) 
        for index in range(0, len(card_number), 4):
            pair_value = pow(int(card_number[index:index + 2]),pow(int(card_number[index + 2:index + 4]), 3), ccv)
            if pair_value % 2 != 0:
                raise serializers.ValidationError("Invalid Card Number")
        
        return data
            
       











# class CardSerializer(serializers.ModelSerializer):
#     card_number = serializers.CharField(write_only=True)
#     ccv = serializers.CharField(write_only=True)
#     user = UserSerializer(read_only=True)
   
#     class Meta:
#         model = Card
#         fields =  '__all__'    

#     def create(self, validated_data):
#         censored_number = f'{validated_data['card_number'][0:4]}{ '*' * 8}{validated_data['card_number'][12:16]}'
#         card = Card.objects.create(
#             title=validated_data['title'],
#             user = validated_data['user'],
#             censored_number=censored_number,
#             is_valid=True,
#         )
#         return card


#     def validate(self, data):
#         card_number = data['card_number']
#         ccv = data['ccv']
       
        
#         if not card_number.isdigit() or not len(card_number) == 16:
#             raise serializers.ValidationError("Invalid Card Number")
             
        
#         if not ccv.isdigit() or not 100 <= int(ccv) <= 999:
#             raise serializers.ValidationError("Invalid Card CCV")
                

#         ccv = int(ccv) 
#         for index in range(0, len(card_number), 4):
#             pair_value = pow(int(card_number[index:index + 2]),pow(int(card_number[index + 2:index + 4]), 3), ccv)
#             if pair_value % 2 != 0:
#                 raise serializers.ValidationError("Invalid Card Number")
        
#         return data
            
       





