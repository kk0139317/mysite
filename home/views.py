from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import numpy as np
from PIL import Image
import os

from home.Sepia_algo import sepia

def index(request):
    return render(request, 'index.html')

def apply_sepia(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage('media')
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)

        # Load image and ensure it is in RGBA format
        img = Image.open(os.path.join(fs.location, filename)).convert('RGBA')
        img_np = np.array(img)
        sepia_img_np = sepia(img_np)
        sepia_img = Image.fromarray(sepia_img_np.astype(np.uint8))

        sepia_filename = 'sepia_' + filename
        sepia_img.save(os.path.join(fs.location, sepia_filename))
        sepia_file_url = fs.url(sepia_filename)

        return render(request, 'index.html', {
            'uploaded_file_url': uploaded_file_url,
            'sepia_file_url': sepia_file_url
        })
    return render(request, 'index.html')

def index_page(request):
    return redirect("apply_sepia/")