from django.shortcuts import render
from django.http import JsonResponse
from .bayesian_optimization import run_BO  # adjust the import based on where you put the function
from io import StringIO
import pandas as pd
import json
from django.contrib.auth.decorators import login_required
from globus_portal_framework.gclients import load_transfer_client
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse


def Team(request):
    return render(request, 'globus-portal-framework/v2/Team.html')

def Research(request):
    return render(request, 'globus-portal-framework/v2/Research.html')

def News(request):
    return render(request, 'globus-portal-framework/v2/News.html')

def Partners(request):
    return render(request, 'globus-portal-framework/v2/Partners.html')

def Repository(request):
    return render(request, 'globus-portal-framework/v2/Repository.html')

def Test_Tagging_System(request):
    return render(request, 'globus-portal-framework/v2/Test Tagging System.html')

def Graph_Visualization(request):
    return render(request, 'globus-portal-framework/v2/Graph_Visualization.html')

def ML_Computing_Toolbox(request):
    return render(request, 'globus-portal-framework/v2/ML_Computing_Toolbox.html')

def Upload_Tutorial(request):
    return render(request, 'globus-portal-framework/v2/Upload_Tutorial.html')

def Upload_Data(request):
    if not request.user.is_authenticated:
        # 如果未认证，添加一个消息提示用户登录
        messages.add_message(request, messages.INFO, 'Please log in to upload data.')
        # 使用命名空间构建Globus登录URL，并指定登录后的重定向地址
        login_url = reverse('social:begin', args=['globus']) + '?next=' + reverse('Upload_Data')
        return redirect(login_url)
    # 如果用户已认证，继续正常逻辑
    # ...（你的上传数据逻辑）...
    return render(request, 'globus-portal-framework/v2/Upload_Data.html')


# Add more views here...


def run_bayesian_optimization(request):
    if request.method == 'POST':
        
        feature_start = int(request.POST.get('featureStart'))
        feature_end = int(request.POST.get('featureEnd'))
        output_index = int(request.POST.get('outputIndex'))
        n_calls = int(request.POST.get('nCalls'))
        n_random_starts = int(request.POST.get('nRandomStarts'))
        acq_func = request.POST.get('acqFunc')
        seed = int(request.POST.get('seed'))
        print(feature_start,feature_end,output_index,n_calls,n_random_starts,acq_func,seed)
        # Reading uploaded file
        csv_file = request.FILES.get('csvFile')
        if csv_file is not None:
            csv_data = csv_file.read().decode('UTF-8')
            io_string = StringIO(csv_data)
            df = pd.read_csv(io_string)
            # Do whatever you want to do with df here
        print(request.POST)
        # Parsing bounds
        raw_bounds_str = request.POST.get('bounds')  # Get the JSON-formatted string
        print("Raw Bounds String:", raw_bounds_str)  # for debugging
        raw_bounds = json.loads(raw_bounds_str)  # Deserialize JSON to Python object
        print("Deserialized Bounds:", raw_bounds)  # for debugging

        bounds = [tuple(map(float, bound.split(','))) for bound in raw_bounds]
        print("Converted Bounds:", bounds)  # additional debug log

        # Run Bayesian Optimization
        best_params, best_value = run_BO(seed=seed, 
                                         csv_data=df,  # Passing DataFrame
                                         feature_indexes=(feature_start, feature_end), 
                                         output_index=output_index, 
                                         n_calls=n_calls, 
                                         n_random_starts=n_random_starts, 
                                         acq_func=acq_func, 
                                         bounds=bounds)

        return JsonResponse({
            'best_parameters': best_params,
            'best_objective': best_value
        })
    else:
        return JsonResponse({'error': 'Only POST method is allowed'})