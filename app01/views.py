from django.core import serializers
from django.shortcuts import render, redirect,HttpResponse
from app01 import models
from bookmanager import urls


# Create your views here.
def publisher_list(reques):
    all_pulishers = models.Publisher.objects.all()
    for i in all_pulishers:
        print(i)
        print(i.id)
        print(i.pk)
        print(i.name)
    return render(reques, "p.html", {'all_pulishers': all_pulishers})
    # 返回

def book_list(request):
    all_books = models.Book.objects.all()
    for book in all_books:
        print(book)
        print(book.id)
        print(book.publisher_id)
        print(book.name)
    return render(request, "book_lists.html", {'all_books': all_books})
    # 返回

def index(reques):
    ret = models.User.objects.all()
    print(ret, type(ret))
    for i in ret:
        print(i, i.username, i.password)
    return render(reques, 'index.html')


def publisher_add(request):
    if request.method == "POST":
        p_name = request.POST.get("pub_name")
        print(p_name)
        ret = models.Publisher.objects.create(name=p_name)
        print(ret)
        return redirect("/publisher_list")
    return render(request, "p_add.html")
def publisher_del(request):
    pk=request.GET.get('id')
    models.Publisher.objects.filter(pk=pk).delete()
    return redirect("/publisher_list")


def answer_list(request):
    answer_lists=models.Answer.objects.all()
    for answer in answer_lists:
        print(answer)
        print("~~~~~~~~~~~~~~")
        print(answer.pk)
        print("++++++++++++++++")
        print(answer.answerPeople)
    return HttpResponse("answer_list")

#
def book_add(request):
    if request.method == "POST":
        book_name = request.POST.get("book_name")
        pub_id = request.POST.get("pub_id")
        # models.Book.objects.create(name=book_name,publisher=models.Publisher.objects.get(pk=pub_id))
        #输入内容为空
        if not book_name :
            all_publisher = models.Publisher.objects.all()
            return render(request,'book_add.html',{"all_pulishers":all_publisher,'error':"书名不能为空"})
        # 输入内容数据库存在
        if  models.Book.objects.filter(name=book_name):
            all_publisher = models.Publisher.objects.all()
            return render(request, 'book_add.html', {"all_pulishers": all_publisher, 'error': "书名不能为重复"})

        else:
            models.Book.objects.create(name=book_name,publisher_id=pub_id)
    all_publisher=models.Publisher.objects.all()

    return render(request,'book_add.html',{"all_pulishers":all_publisher,"success":"添加成功"})


def book_del(request):
    # id=request.GET.get('id')
    # models.Book.objects.filter(id=id).delete()
    # models.Book
    # return redirect('/pulisher_list/')
    pk = request.GET.get('id')
    models.Book.objects.filter(pk=pk).delete()
    return redirect('/book_list/')

# 编辑书单，待完成
def book_edit(request):
        # id=request.GET.get('id')
        # models.Book.objects.filter(id=id).delete()
        # models.Book
        # return redirect('/pulisher_list/')
        pk = request.GET.get('id')
        book_obj=models.Book.objects.get(pk=pk)
        return render(request,'book_edit.html',{'book_obj':book_obj})


def author_list(request):
    all_authors=models.Author.objects.all()
    for author in all_authors:
        print(author)
        print(author.name)
        print(author.id)
        print(author.book)
        print(author.book.all())
    return HttpResponse("authoer")



import json
from django.http import JsonResponse
def search(request):
    if request.method == "POST":
        # print(dir(request))
        # name=request.GET.get("name","")
        name=request.POST.get("name","")
        retQ = models.Question.objects.filter(questionName__icontains=name)
        # retQ = models.Question.objects.all()
        # searchQ=retQ.get(questionName="name")
        # print(retQ.query)

        # print(type(retQ))
        # for e in retQ:
        #     print(e.questionName)
        # print("----------")
        # print(request.GET.get("name",""))
        # retJoin=models.Question.objects.select_related('id')
        # print(retJoin)
    return JsonResponse({
        'data': json.loads(serializers.serialize('json', retQ, ensure_ascii=False))})
    #
    # if request.method == "POST":
    #     # print(dir(request))
    #     name=request.POST.get("name","")
    #     retQ = models.Question.objects.filter(questionName__icontains=name)
    #
    # return JsonResponse({
    #     'data': json.loads(serializers.serialize('json', retQ, ensure_ascii=False))})

