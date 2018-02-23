from django.shortcuts import render, redirect
from models import User, Author, Review, Book
from django.contrib import messages
# Create your views here.

def dashboard(request):
    if 'name' not in request.session:
        return redirect('/')
    context={
        'user': User.objects.get(id=request.session['id']),
        'recent': Review.objects.recent_and_not()[0],
        'more': Review.objects.recent_and_not()[1]

    }
    return render(request, 'book_app/dashboard.html', context)

def new (request):
    if 'name' not in request.session:
        return redirect('/')
    context={
        'authors': Author.objects.all()
    }
    return render(request, 'book_app/new.html')

def create(request):
    results = Review.objects.validate(request.POST)
    
    if len(results['errors']) > 0:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/main/new')
    else:
        
        a = Author.objects.create(name=request.POST['author_name'])
        this_author = Author.objects.get(id=a.id)

        b= Book.objects.create(title=request.POST['title'], writer = this_author,)
       
        this_book = Book.objects.get(id=b.id)

        Review.objects.create(comment=request.POST['comment'], rating=request.POST['rating'], poster=User.objects.get(id=request.session['id']), book = this_book)

        

       


        
    


    return redirect('/main/dashboard')

def show_book(request, id):
    context={
        'books':Book.objects.get(id=id),
        'reviews': Review.objects.filter(book__id=id)
        
    }
    return render(request, 'book_app/show_book.html', context)


def show_user(request, id):
    context = {
        'user': User.objects.get(id=id),
        'reviews': Review.objects.filter(poster__id=id)
    }

    return render(request, 'book_app/show_user.html', context)

def add(request, id):
   Review.objects.create(comment=request.POST['comment'], rating=request.POST['rating'],   poster=User.objects.get(id=request.session['id']), book= Book.objects.get(id=id))

   return redirect('/main/dashboard')

