from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import upload_image_form
from django.core.files.storage import FileSystemStorage
from covid.test import model_prediction
from plotly.offline import plot
from plotly.graph_objs import Scatter
from covid.test import get_plot
# Create your views here.

# View for Index Page
def index_view(request):
    return render(request, "index.html")


# View for upload page
def upload_view(request):
    if request.method == "POST":
        # If Request Method is POST then redirected to the results page
        form = upload_image_form(request.POST,request.FILES)
        if form.is_valid():
            image = request.FILES['Image']
            fs = FileSystemStorage()
            filename = fs.save(image.name,image)
            # Path to the uploaded image file
            uploaded_file_url = fs.url(filename)
            # To get predicted result
            result = model_prediction(str(uploaded_file_url)[1:])
            # Image Name
            image_name = str(uploaded_file_url).split("/")[2]
            
            helpline_nums_states = {
                'Andhra Pradesh':'0866-2410978','Arunachal Pradesh':'9436055743','Assam':'6913347770','Bihar':'104','Chhattisgarh':'104','Goa':'104','Gujarat':'104','Haryana':'8558893911',
                'Madhya Pradesh':'104','Maharashtra':'020-26127394','Manipur':'3852411668','Manipur':'3852411668','Meghalaya':'108','Mizoram':'102','Nagaland':'7005539653','Odisha':'9439994859',
                'Punjab':'104','Rajasthan':'0141-2225624','Sikkim':'104','Tamil Nadu':'044-29510500','Telangana':'104','Tripura':'0381-2315879','Uttarakhand':'104','Uttar Pradesh':'18001805145',
                'West Bengal':'1800313444222, 03323412600'
            }
            helpline_nums_ut ={
                'Andaman and Nicobar Islands':'03192-232102','Chandigarh':'9779558282','Dadra and Nagar Haveli and Daman & Diu':'104','Delhi':'011-22307145','Jammu & Kashmir':'01912520982, 0194-2440283',
                'Ladakh':'01982256462','Lakshadweep':'104','Puducherry':'104'
            }
            context = {
                'form':form,'uploaded_file_url':uploaded_file_url,'result':result,'helpline_nums_states':helpline_nums_states,'helpline_nums_ut':helpline_nums_ut
            }
            return render(request,'result.html',context=context)
            #return render(request,'symptoms.html',context={'form':form})
    else:
        # If request method is not post then upload form is rendered using upload_image.html
        form = upload_image_form()
        return render(request,'upload_image.html',context={'form':form})