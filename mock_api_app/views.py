from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import HttpResponse
from mock_api_app.serializers import personSerializers
from mock_api_app.models import Person,Student

@api_view(['GET'])
def index(self):
    return HttpResponse("Home Page !!");

#==========================================================

class PersonList(APIView):

    def get(self,request):
        if request.GET.get('id') != None :
            idd=request.GET.get('id')
            P=Person.objects.filter(id=idd)
            if P:
                P1= Person.objects.get(id=idd)
                s=personSerializers(P1)
                return  Response(s.data)
            else:
                return Response("No Record Found !!")
        else:
            p = Person.objects.all()
            s = personSerializers(p, many=True)
            return Response(s.data)

# ==========================================================

    def post(self,request):
        name = request.GET.get('name')
        id = request.GET.get('id')
        salary = request.GET.get('salary')
        p = Person(name=name, id=id, salary=salary)
        p.save()
        return HttpResponse("data posted sucessfully!!!")


#==========================================================

    def put(self,request):
        idd=request.GET.get('id')
        name=request.POST.get('name')
        P= Person.objects.get(id=idd)
        P.name=name
        P.save()
        return HttpResponse("Record Updated sucessfully!!!")

#==========================================================

    def delete(self,request):
        idd=request.POST.get('id')
        Person.objects.filter(id=idd).delete()
        return HttpResponse( " Record Deleted  !!")

#==========================================================

    def patch(self,request):
        return HttpResponse('patch method !!')
