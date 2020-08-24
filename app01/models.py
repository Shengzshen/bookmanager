from django.db import models

# Create your models here.
#创建数据库表，写对应的类即可
class Publisher(models.Model):
    name = models.CharField(max_length=32,null=False)

class Book(models.Model):
    name = models.CharField(max_length=32,null=False)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, blank=True, null=True)
    #, blank=True, null=True 强制执行
class Author(models.Model):
    name = models.CharField(max_length=32,null=False)
    #作者与书名是多对多关系
    book = models.ManyToManyField("Book")
# class Author_Book(models.Model):
#     name = models.CharField(max_length=32,null=False)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)


class User(models.Model):
    username = models.CharField(max_length=32)   #对应数据库的varchar
    password = models.CharField(max_length=32)

# 问题表字段：问题id，提问人，问题名称，提问时间
class Question(models.Model):
    questioner = models.TextField(max_length=32)
    # questionId = models.BigIntegerField()
    questionName = models.CharField(max_length=64,null=False)
    questionTime = models.DateTimeField()
# #答案表字段：id，问题id，答案内容，回答人，回答时间，答案收藏数，赞同数
class Answer(models.Model):
    # answerId = models.BigIntegerField()
    questionId = models.ForeignKey(Question,on_delete=models.CASCADE, blank=True, null=True)
    '''
    外键中on_delete参数
    models.CASCADE   级联删除
    models.PROTECT   有数据保护
    models.SET（v)   删除后设置某个值
    models.SETDEFAULT,default=1 删除后设置为默认值
    models.SET_NULLL  删除后为null
    '''
    answerContent = models.CharField(max_length=1024,null=False)
    answerPeople = models.CharField(max_length=32,null=False)
    answerTime = models.DateTimeField()
    answerCollection =  models.IntegerField(null=False)
    approvalNumber =  models.IntegerField(null=False)

# 评论表字段：id，答案id，评论人，评论时间
class Reviewtable(models.Model):
    # questionId = models.BigIntegerField()
    answerId = models.ForeignKey(Answer,on_delete=models.CASCADE,blank=True, null=True)
    reviewPeople = models.CharField(max_length=32,null=False)
    reviewTime = models.DateTimeField()
#
# # class Reviews(models.Model):
# # 然后每个评论下面还会有很多回复等等，你看看怎么设计表
# # 还有再写一个搜索的接口，我传给你用户要搜索的内容，你返回给我匹配的问题列表，
# # 包含问题的一些属性（提问时间，提问人等
