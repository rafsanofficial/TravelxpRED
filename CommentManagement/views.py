from django.shortcuts import render

# Create your views here.


from .models import Comment
def showComment(request):
    commentList = Comment.objects.all()
    context = {
        'Comment' : commentList
    }
    return render(request, 'CommentManagement/CommentList.html', context)