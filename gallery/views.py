from django.shortcuts import render
from django.utils import timezone
from .models import Pictures
from forms import ImagePostForm
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def image_list(request):

    image = Pictures.objects.filter()
        # (published_date__lte=timezone.now()).order_by('-published_date')

    # paginator = Paginator(image, 6)
    #
    # try:
    #     page = int(request.GET.get('page', '1'))
    # except:
    #     page = 1
    #
    # try:
    #     image = paginator.page(page)
    # except(EmptyPage, InvalidPage):
    #     image = paginator.page(paginator.num_pages)
    #


    paginator = Paginator(image, 6)
    page = request.GET.get('page')
    try:
        image = paginator.page(page)
    except PageNotAnInteger:
        image = paginator.page(1)
    except EmptyPage:
        image = paginator.page(paginator.num_pages)





    return render(request, "ImageGallery.html", {'image': image})


# def new_image(request):
#     form = ImagePostForm()
#     return render(request, 'NewImageForm.html', {'form': form})
#

# def new_image(request):
#     if request.method == "POST":
#         form = ImagePostForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = form.save(commit=False)
#             image.author = request.user
#             image.published_date = timezone.now()
#             image.save()
#             return redirect(image_list, image.pk)
#     else:
#         form = ImagePostForm()
#     return render(request, 'ImageGallery.html', {'form': form})




def new_image(request):
    if request.method == 'POST':
        form = ImagePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(image_list)
    else:
        form = ImagePostForm()
    return render(request, 'NewImageForm.html', {
        'form': form
    })

