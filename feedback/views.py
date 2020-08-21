from .models import Comment
from .forms import CommentForm
from django.shortcuts import render, redirect


def comment(request):
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():      
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'feedback.html',
                  {'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})