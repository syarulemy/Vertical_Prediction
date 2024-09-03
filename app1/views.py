from django.shortcuts import render
import pickle
import numpy as np
import os
from django.conf import settings
# Create your views here.

# Load the saved model, scaler, and label encoder


def result(request, prediction):
    return render(request, 'result.html', {'prediction': prediction})

def dashboard_view(request):
    return render(request, 'dashboard.html')


'''from django.shortcuts import render, redirect
import pickle
from .models import Record
from .forms import RecordForm

def predict(request):
    with open('naive_bayes_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    with open('label_encoder.pkl', 'rb') as f:
        label_encoder = pickle.load(f)

    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            try:
                # Collect user input from form using form.cleaned_data
                user_input = [
                    float(form.cleaned_data[col]) for col in model.feature_names_in_
                ]

                # Scale the input
                scaled_input = scaler.transform([user_input])

                # Predict using the model
                prediction = model.predict(scaled_input)

                # Convert the prediction back to the original label
                prediction = label_encoder.inverse_transform(prediction)[0]
                print(prediction)
                
                # Save the form data and prediction to the database
                record = Record(
                    No_KP=form.cleaned_data['No_KP'],
                    Nama=form.cleaned_data['Nama'],
                    No_Tel=form.cleaned_data['No_Tel'],
                    Nm_Syarikat=form.cleaned_data['Nm_Syarikat'],
                    Ind_Perniagaan=form.cleaned_data['Ind_Perniagaan'],
                    Julat_HasilJualan=form.cleaned_data['Julat_HasilJualan'],
                    Julat_Keuntungan=form.cleaned_data['Julat_Keuntungan'],
                    Julat_Pbelanja=form.cleaned_data['Julat_Pbelanja'],
                    Julat_PurataHargaProduk=form.cleaned_data['Julat_PurataHargaProduk'],
                    Lokasi_Sasaran_Audiens=form.cleaned_data['Lokasi_Sasaran_Audiens'],
                    Bil_Staf=int(form.cleaned_data['Bil_Staf']),
                    Bis_Mmpu_bthn=form.cleaned_data['Bis_Mmpu_bthn'],
                    Cara_Beli=form.cleaned_data['Cara_Beli'],
                    Slrn_Phbngn=form.cleaned_data['Slrn_Phbngn'],
                    K_Pghntrn=form.cleaned_data['K_Pghntrn'],
                    Plt_Talian=form.cleaned_data['Plt_Talian'],
                    Trmnl_Byrn=form.cleaned_data['Trmnl_Byrn'],
                    Cr_Byrn=form.cleaned_data['Cr_Byrn'],
                    Slrn_Fzkl=form.cleaned_data['Slrn_Fzkl'],
                    Mjrt_Kaum=form.cleaned_data['Mjrt_Kaum'],
                    Sjl_Halal=form.cleaned_data['Sjl_Halal'],
                    Cap_dgngn=form.cleaned_data['Cap_dgngn'],
                    Akt_Pmsrn=form.cleaned_data['Akt_Pmsrn'],
                    Kpst_Tgkt_Digital=form.cleaned_data['Kpst_Tgkt_Digital'],
                    Btn_kew_bank=form.cleaned_data['Btn_kew_bank'],
                    Btn_Pmsrn_Dgtl=form.cleaned_data['Btn_Pmsrn_Dgtl'],
                    Btn_Sjl=form.cleaned_data['Btn_Sjl'],
                    Btn_Prnct_Fzkl=form.cleaned_data['Btn_Prnct_Fzkl'],
                    Btn_Lgstk_Pghtrn=form.cleaned_data['Btn_Lgstk_Pghtrn'],
                    Jns_Btn_Kew=form.cleaned_data['Jns_Btn_Kew'],
                    SuggestedVerticals=prediction,  # Save the prediction
                )
                record.save()  # Save to the database

                # Redirect to the result page with the prediction
                return redirect('result', prediction=prediction)

            except Exception as e:
                error = str(e)
                return render(request, 'enterprenuer.html', {'form': form, 'error': error})
        else:
            # If the form is not valid, render the form with errors
            return render(request, 'enterprenuer.html', {'form': form})

    else:
        # If not POST, just render the empty form
        form = RecordForm()
        return render(request, 'enterprenuer.html', {'form': form})'''
'''
#def result(request, prediction):
   # return render(request, 'result.html', {'prediction': prediction})
import os
import pickle
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Record
from django.urls import reverse

# Load model, scaler, and label encoder
MODEL_PATH = os.path.join(settings.BASE_DIR, 'app1', 'naive_bayes_model.pkl')
SCALER_PATH = os.path.join(settings.BASE_DIR, 'app1', 'scaler.pkl')
LABEL_ENCODER_PATH = os.path.join(settings.BASE_DIR, 'app1', 'label_encoder.pkl')

# Load once at startup
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

with open(SCALER_PATH, 'rb') as f:
    scaler = pickle.load(f)

with open(LABEL_ENCODER_PATH, 'rb') as f:
    label_encoder = pickle.load(f)

def predict(request):
    if request.method == 'POST':
        try:
            # Extract form data
            form_data = request.POST

            # Prepare input data for prediction
            input_features = [
                int(form_data.get('Ind_Perniagaan')),
                int(form_data.get('Julat_HasilJualan')),
                int(form_data.get('Julat_Keuntungan')),
                int(form_data.get('Julat_Pbelanja')),
                int(form_data.get('Julat_PurataHargaProduk')),
                int(form_data.get('Lokasi_Sasaran_Audiens')),
                int(form_data.get('Bil_Staf')),
                int(form_data.get('Bis_Mmpu_bthn')),
                int(form_data.get('Cara_Beli')),
                int(form_data.get('Slrn_Phbngn')),
                int(form_data.get('K_Pghntrn')),
                int(form_data.get('Plt_Talian')),
                int(form_data.get('Trmnl_Byrn')),
                int(form_data.get('Cr_Byrn')),
                int(form_data.get('Slrn_Fzkl')),
                int(form_data.get('Mjrt_Kaum')),
                int(form_data.get('Sjl_Halal')),
                int(form_data.get('Cap_dgngn')),
                int(form_data.get('Akt_Pmsrn')),
                int(form_data.get('Kpst_Tgkt_Digital')),
                int(form_data.get('Btn_kew_bank')),
                int(form_data.get('Btn_Pmsrn_Dgtl')),
                int(form_data.get('Btn_Sjl')),
                int(form_data.get('Btn_Prnct_Fzkl')),
                int(form_data.get('Btn_Lgstk_Pghtrn')),
                int(form_data.get('Jns_Btn_Kew'))
            ]

            # Reshape and scale input
            scaled_input = scaler.transform([input_features])

            # Make prediction
            prediction = model.predict(scaled_input)
            predicted_vertical = label_encoder.inverse_transform(prediction)[0]

            # Save data to database
            record = Record(
                No_KP=form_data.get('No_KP'),
                Nama=form_data.get('Nama'),
                No_Tel=form_data.get('No_Tel'),
                Nm_Syarikat=form_data.get('Nm_Syarikat'),
                Ind_Perniagaan=form_data.get('Ind_Perniagaan'),
                Julat_HasilJualan=form_data.get('Julat_HasilJualan'),
                Julat_Keuntungan=form_data.get('Julat_Keuntungan'),
                Julat_Pbelanja=form_data.get('Julat_Pbelanja'),
                Julat_PurataHargaProduk=form_data.get('Julat_PurataHargaProduk'),
                Lokasi_Sasaran_Audiens=form_data.get('Lokasi_Sasaran_Audiens'),
                Bil_Staf=form_data.get('Bil_Staf'),
                Bis_Mmpu_bthn=form_data.get('Bis_Mmpu_bthn'),
                Cara_Beli=form_data.get('Cara_Beli'),
                Slrn_Phbngn=form_data.get('Slrn_Phbngn'),
                K_Pghntrn=form_data.get('K_Pghntrn'),
                Plt_Talian=form_data.get('Plt_Talian'),
                Trmnl_Byrn=form_data.get('Trmnl_Byrn'),
                Cr_Byrn=form_data.get('Cr_Byrn'),
                Slrn_Fzkl=form_data.get('Slrn_Fzkl'),
                Mjrt_Kaum=form_data.get('Mjrt_Kaum'),
                Sjl_Halal=form_data.get('Sjl_Halal'),
                Cap_dgngn=form_data.get('Cap_dgngn'),
                Akt_Pmsrn=form_data.get('Akt_Pmsrn'),
                Kpst_Tgkt_Digital=form_data.get('Kpst_Tgkt_Digital'),
                Btn_kew_bank=form_data.get('Btn_kew_bank'),
                Btn_Pmsrn_Dgtl=form_data.get('Btn_Pmsrn_Dgtl'),
                Btn_Sjl=form_data.get('Btn_Sjl'),
                Btn_Prnct_Fzkl=form_data.get('Btn_Prnct_Fzkl'),
                Btn_Lgstk_Pghtrn=form_data.get('Btn_Lgstk_Pghtrn'),
                Jns_Btn_Kew=form_data.get('Jns_Btn_Kew'),
                SuggestedVerticals=predicted_vertical
            )
            record.save()

            # Redirect to result page with prediction
            return redirect(reverse('result', kwargs={'prediction': predicted_vertical}))

        except Exception as e:
            error_message = f"An error occurred during prediction: {str(e)}"
            return render(request, 'enterprenuer.html', {'error': error_message})

    else:
        return render(request, 'enterprenuer.html')'''
import os
import pickle
import pandas as pd
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Record
from django.urls import reverse

# Load model, scaler, and label encoder
MODEL_PATH = os.path.join(settings.BASE_DIR, 'app1', 'naive_bayes_model.pkl')
SCALER_PATH = os.path.join(settings.BASE_DIR, 'app1', 'scaler.pkl')
LABEL_ENCODER_PATH = os.path.join(settings.BASE_DIR, 'app1', 'label_encoder.pkl')

# Load once at startup
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

with open(SCALER_PATH, 'rb') as f:
    scaler = pickle.load(f)

with open(LABEL_ENCODER_PATH, 'rb') as f:
    label_encoder = pickle.load(f)
import os
import pickle
import pandas as pd
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Record
from django.urls import reverse

# Load model, scaler, and label encoder
MODEL_PATH = os.path.join(settings.BASE_DIR, 'app1', 'naive_bayes_model.pkl')
SCALER_PATH = os.path.join(settings.BASE_DIR, 'app1', 'scaler.pkl')
LABEL_ENCODER_PATH = os.path.join(settings.BASE_DIR, 'app1', 'label_encoder.pkl')

# Load once at startup
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

with open(SCALER_PATH, 'rb') as f:
    scaler = pickle.load(f)

with open(LABEL_ENCODER_PATH, 'rb') as f:
    label_encoder = pickle.load(f)

# Features used for the model
FEATURE_NAMES = [
    'Ind_Perniagaan', 'Julat_HasilJualan', 'Julat_Keuntungan', 'Julat_Pbelanja', 
    'Julat_PurataHargaProduk', 'Lokasi_Sasaran_Audiens', 'Bil_Staf', 'Bis_Mmpu_bthn', 
    'Cara_Beli', 'Slrn_Phbngn', 'K_Pghntrn', 'Plt_Talian', 'Trmnl_Byrn', 'Cr_Byrn', 
    'Slrn_Fzkl', 'Mjrt_Kaum', 'Akt_Pmsrn', 'Kpst_Tgkt_Digital', 
    'Btn_kew_bank', 'Btn_Pmsrn_Dgtl', 'Btn_Sjl', 'Btn_Prnct_Fzkl', 'Btn_Lgstk_Pghtrn', 
    'Jns_Btn_Kew'
]

def predict(request):
    if request.method == 'POST':
        try:
            # Extract form data
            form_data = request.POST
             
            no_kp = form_data.get('No_KP')

            # Check if No_KP already exists
            if Record.objects.filter(No_KP=no_kp).exists():
                error_message = "No_KP already exists in the database."
                return render(request, 'enterprenuer.html', {'error': error_message})

            # Prepare input data for prediction, using only relevant features
            input_features = [
                int(form_data.get(feature)) for feature in FEATURE_NAMES
            ]

            # Convert input_features to a DataFrame with the same columns as the original scaler
            input_df = pd.DataFrame([input_features], columns=FEATURE_NAMES)

            # Scale the input using the scaler
            scaled_input = scaler.transform(input_df)

            # Make prediction
            prediction = model.predict(scaled_input)
            predicted_vertical = label_encoder.inverse_transform(prediction)[0]

            # Save data to the database, including all the fields
            record = Record(
                No_KP=form_data.get('No_KP'),
                Nama=form_data.get('Nama'),
                No_Tel=form_data.get('No_Tel'),
                Nm_Syarikat=form_data.get('Nm_Syarikat'),
                Ind_Perniagaan=form_data.get('Ind_Perniagaan'),
                Julat_HasilJualan=form_data.get('Julat_HasilJualan'),
                Julat_Keuntungan=form_data.get('Julat_Keuntungan'),
                Julat_Pbelanja=form_data.get('Julat_Pbelanja'),
                Julat_PurataHargaProduk=form_data.get('Julat_PurataHargaProduk'),
                Lokasi_Sasaran_Audiens=form_data.get('Lokasi_Sasaran_Audiens'),
                Bil_Staf=form_data.get('Bil_Staf'),
                Bis_Mmpu_bthn=form_data.get('Bis_Mmpu_bthn'),
                Cara_Beli=form_data.get('Cara_Beli'),
                Slrn_Phbngn=form_data.get('Slrn_Phbngn'),
                K_Pghntrn=form_data.get('K_Pghntrn'),
                Plt_Talian=form_data.get('Plt_Talian'),
                Trmnl_Byrn=form_data.get('Trmnl_Byrn'),
                Cr_Byrn=form_data.get('Cr_Byrn'),
                Slrn_Fzkl=form_data.get('Slrn_Fzkl'),
                Mjrt_Kaum=form_data.get('Mjrt_Kaum'),
                Akt_Pmsrn=form_data.get('Akt_Pmsrn'),
                Kpst_Tgkt_Digital=form_data.get('Kpst_Tgkt_Digital'),
                Btn_kew_bank=form_data.get('Btn_kew_bank'),
                Btn_Pmsrn_Dgtl=form_data.get('Btn_Pmsrn_Dgtl'),
                Btn_Sjl=form_data.get('Btn_Sjl'),
                Btn_Prnct_Fzkl=form_data.get('Btn_Prnct_Fzkl'),
                Btn_Lgstk_Pghtrn=form_data.get('Btn_Lgstk_Pghtrn'),
                Jns_Btn_Kew=form_data.get('Jns_Btn_Kew'),
                SuggestedVerticals=predicted_vertical
            )
            record.save()
            try:
                record.save()
            except IntegrityError:
                error_message = "No_KP already exists in the database."
            # Redirect to result page with prediction
            return redirect(reverse('result', kwargs={'prediction': predicted_vertical}))

        except Exception as e:
            error_message = f"An error occurred during prediction: {str(e)}"
            return render(request, 'enterprenuer.html', {'error': error_message})

    else:
        return render(request, 'enterprenuer.html')
def search(request):
    query = request.GET.get('q')
    results = None
    if query:
        results = Record.objects.filter(No_KP__icontains=query)
    return render(request, 'search.html', {'results': results, 'query': query})