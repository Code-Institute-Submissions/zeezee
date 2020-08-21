from .models import Comment
from .forms import CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


def comment(request):
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.save()
            messages.success(request, 'Comment successfully added!')
    else:
        comment_form = CommentForm()
    return render(request,
                  'comment/feedback.html',
                  {'comment': comment,
                   'new_comment': new_comment,
                   'comment_form': comment_form})


def comment_list(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    context = {
        'comment': comment,
    }

    return render(request, 'comment/feedback.html', context)
