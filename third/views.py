from django.shortcuts import render

# Create your views here.


from django import views
from django.http import HttpResponse
from django.shortcuts import redirect, render
import datetime
from .models import Booklet

# Create your views here.
# def homepage(request,pk): 
#     print(request.method)
def homepage(request):  # request is a default args
    if request.method == "POST":
        # print(request.POST.get("bid"),"222222222222")
        book_id = request.POST.get("bid")
        book_name = request.POST.get("bname")
        book_price = request.POST.get("bprice")
        book_qty = request.POST.get("bqty")
        book_is_published = request.POST.get("bpub")
       
        if not book_id: 
                    # if book id is not present 
        # print(book_name, book_price, book_qty, book_is_published)
            if book_is_published == "Yes":
                 book_is_published = True
            else:
                book_is_published = False   
            book_obj = Booklet(name=book_name, price=float(book_price), qty=int(book_qty), is_published=book_is_published)  # here we create data so we make object
            book_obj.save()
            return HttpResponse("Book added successfully...")
        else:
            book_obj = Booklet.objects.get(id=book_id)  # if book_id is present 
            book_obj.name = book_name
            book_obj.price = book_price
            book_obj.qty = book_qty
            if book_is_published == "Yes":
                book_is_published = True
            else:
                book_is_published = False
            book_obj.is_published = book_is_published
            book_obj.save()
            # return HttpResponse("Book updated successfully...!")
            return redirect("show_books")

    else:
      return render(request, 'home.html')
    
def show_books(request):
    books = Booklet.objects.all()
    return render(request, "show_books.html", {"all_books": books})


def edit_book(request, pk):
    book_obj = Booklet.objects.get(id=pk)
    return render(request, "home.html", {"book": book_obj})


def delete_book(request, pk):
    book_obj = Booklet.objects.get(id=pk)
    book_obj.delete()
    # book_obj.is_active = False
    # book_obj.save()
    return redirect("show_books")  

def restore_book(request, pk):
    book_obj = Booklet.objects.get(id=pk)
    book_obj.restore()
    # book_obj.is_active = False
    # book_obj.save()
    return redirect("show_books")      



    # print(request.method)
    # print(dir(request))
    # print(request.user)
    # print(request.get_raw_url())
    # return HttpResponse("Hello welcome to homepage---!")
    # return render(request, 'home.html', {"language": "Python", "version":"3.8.2"})
    # data = {"language": "Python", "version":"3.8.2"}
    # print(id)
    # data = {"name": id}
    # data = {"flag": "Yes","lst":[10,20,30,40,50] }
    # try:
    #     book_obj = Booklet.objects.get(id=pk)
    # except Booklet.DoesNotExist:
    #     data = {"error": f"Book Does not exists with id number {pk}"}
    # data = {"booklet": book_obj}
    # return render(request, 'home.html', context=data)    
    # data = {"flag": "No","lst":[10,20,30,40,50], "today":datetime.datetime.now().date(), "name": "abcdfd dfdfdf dgg fgfdg fgfdg rr rgrg rr rtry yry " }
    # data = {"flag": "No","all_books":Booklet.objects.all(), "today":datetime.datetime.now().date(), "name": "abcdfd dfdfdf dgg fgfdg fgfdg rr rgrg rr rtry yry " }
    # data = {"flag": "No","all_books":Booklet.objects.filter(id__gt=1), "today":datetime.datetime.now().date(), "name": "abcdfd dfdfdf dgg fgfdg fgfdg rr rgrg rr rtry yry " }
    # return render(request, 'home.html', data)
    # return render(request, 'home.html', data)
    # data = {"booklet": book_obj}
    # return render(request, 'home.html', {"data":{1:10, 2:20, 3:30, 4:40, 5:50, 6:60}})
    # return render(request, 'home.html', context=data)


from django.views import View
from django.http import HttpResponse

class Home(View):
    def get(self,request):
        print("In get method")
        return HttpResponse("In get method")


    def post(self,request):
        print("In post method")
        return HttpResponse("In postmethod")


    def put(self,request):
        print("In put method")
        return HttpResponse("In put method")        


    def patch(self,request):
        print("In patch method")
        return HttpResponse("In patch method")


    def delete(self,request):
        print("In delete method")
        return HttpResponse("In delete method")    

    def product_video(request):
        print("In product view")
        return HttpResponse("video")    