from django.shortcuts import render

# Create your views here.
def feedback(request, *args, **kwargs):
   
    return render(request, "feedback/comment_detail.html", {"feedback": "comment"})