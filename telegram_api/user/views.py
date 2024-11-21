from rest_framework import viewsets
from . import models
from django.http import JsonResponse
import datetime


class UserInfo(viewsets.ModelViewSet):
    def create(self, request):
        try:
            id = request.data['id']
            temporary = request.data['temporary']
            rec_data = request.data['init']
            # result,username,tel_id = validate_telegram_data(data=rec_data)
            result = True
            username = 'test'
            tel_id = 12345 
            if result == True:
                try:
                    
                    # print(models.UserApp.objects.all().order_by('-point'))


                    # if datetime.datetime.now().day == 19:
                    #     for userParam in models.UserApp.objects.all():
                    #         print(userParam.point)
                            # userParam.point = 0
                            # userParam.save()
                    user = models.UserApp.objects.get(id=id)
                    print(user.user_image)

                    if user.user_telid == tel_id:
                        user.point += temporary
                        user.save()
                        return JsonResponse({'id':user.id,'point':user.point},status=200)
                    else:
                        raise Exception('user id is not true')
                    
                except Exception as e:
                    print(e)
                    return JsonResponse({'status':'error'},status = 401)
                
            else:
                return JsonResponse({'status':'validation error'},status = 401)

        except models.UserApp.DoesNotExist as e:
            return JsonResponse({'status':'user not found'},status = 402)

        
        except Exception as e:
            return JsonResponse({'status':e.__str__()},status = 402)

class SignUpUser(viewsets.ModelViewSet):

    def create(self, request):

        referral = request.data['referral']
        user_name = request.data['user_name']
        user_id = request.data['user_id']

        try:
            newUser = models.UserApp.objects.create(user_name=user_name,user_telid=user_id)
            newUser.save()
            if referral != 0:
                try:
                    ref_user = models.UserApp.objects.get(id=referral)
                    ref_user.referral_count += 1
                    ref_user.point += 700
                    print(ref_user)
                    print(ref_user.referral_count)
                    ref_user.save()

                except Exception as e:
                    return JsonResponse({'status':e.__str__()},status= 402)

            return JsonResponse({'status':'User Created','id':newUser.id},status= 200)


        except Exception as e:
            return JsonResponse({'status':e.__str__()},status= 401)

