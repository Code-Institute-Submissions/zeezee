from .models import Comment
from .forms import CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


def comment(request):
    '''
    View for add new comment and redirect a success message
    '''
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.save()
            messages.success(request, 'Review successfully added!')
    else:
        comment_form = CommentForm()
    return render(request,
                  'comment/feedback.html',
                  {'comment': comment,
                   'new_comment': new_comment,
                   'comment_form': comment_form})


def comment_list(request):
    '''
    View to render the list of comments
    '''
    comments = Comment.objects.all()
    context = {
        'comments': comments,
    }
    return render(request, 'comment/feedback_list.html', context)
