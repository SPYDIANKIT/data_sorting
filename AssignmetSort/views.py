# views.py

from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import PersonalInfo, ContactInfo
import csv
from django.http import HttpResponse
from reportlab.pdfgen import canvas

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect('display_data')
    else:
        form = UploadFileForm()
    return render(request, 'upload_file.html', {'form': form})

def update_personal_info(email, first_name, last_name):
    # Update or create PersonalInfo
    personal_info, created = PersonalInfo.objects.update_or_create(
        email=email,
        defaults={
            'first_name': first_name,
            'last_name': last_name,
        }
    )
    return personal_info

def update_contact_info(personal_info, row):
    # Remove duplicate ContactInfo based on email
    ContactInfo.objects.filter(UserInfo__email=row['Email']).delete()

    # Create or update ContactInfo
    contact_info, created = ContactInfo.objects.get_or_create(
        UserInfo=personal_info,
        defaults={
            'phone_no': row['Phone No'],
            'gender': row['Gender'],
            'dob': row['DOB'],
            'address1': row['Address 1'],
            'address2': row['Address 2'],
            'pincode': row['Pincode'],
            'state': row['State'],
            'country': row['Country'],
        }
    )

    if not created:
        # If ContactInfo already exists, update the data
        contact_info.phone_no = row['Phone No']
        contact_info.gender = row['Gender']
        contact_info.dob = row['DOB']
        contact_info.address1 = row['Address 1']
        contact_info.address2 = row['Address 2']
        contact_info.pincode = row['Pincode']
        contact_info.state = row['State']
        contact_info.country = row['Country']
        contact_info.save()

def handle_uploaded_file(file):
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    for row in reader:
        # Update PersonalInfo
        personal_info = update_personal_info(
            email=row['Email'],
            first_name=row['First Name'],
            last_name=row['Last Name'],
        )

        # Update ContactInfo
        update_contact_info(personal_info, row)

def display_data(request):
    data = ContactInfo.objects.all()
    return render(request, 'display_data.html', {'data': data})



# Your existing view functions...

def download_contact_info_csv(data):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contact_info.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email', 'Phone No', 'Gender', 'DOB', 'Address 1', 'Address 2', 'Pincode', 'State', 'Country'])

    for entry in data:
        writer.writerow([
            entry.UserInfo.first_name,
            entry.UserInfo.last_name,
            entry.UserInfo.email,
            entry.phone_no,
            entry.gender,
            entry.dob,
            entry.address1,
            entry.address2,
            entry.pincode,
            entry.state,
            entry.country,
        ])

    return response

def download_personal_info_csv(data):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="personal_info.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email'])

    for entry in data:
        writer.writerow([
            entry.UserInfo.first_name,
            entry.UserInfo.last_name,
            entry.UserInfo.email,
        ])

    return response

def download_combined_csv(data):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="combined_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email', 'Phone No', 'Gender', 'DOB', 'Address 1', 'Address 2', 'Pincode', 'State', 'Country'])

    for entry in data:
        writer.writerow([
            entry.UserInfo.first_name,
            entry.UserInfo.last_name,
            entry.UserInfo.email,
            entry.phone_no,
            entry.gender,
            entry.dob,
            entry.address1,
            entry.address2,
            entry.pincode,
            entry.state,
            entry.country,
        ])

    return response

def download_combined_pdf(data):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="combined_data.pdf"'

    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 12)

    data_headers = ['First Name', 'Last Name', 'Email', 'Phone No', 'Gender', 'DOB', 'Address 1', 'Address 2', 'Pincode', 'State', 'Country']
    p.drawString(100, 800, "Personal and Contact Info")

    y_position = 780
    for header in data_headers:
        p.drawString(100, y_position, header)
        y_position -= 20

    for entry in data:
        y_position -= 20
        p.drawString(100, y_position, entry.UserInfo.first_name)
        p.drawString(200, y_position, entry.UserInfo.last_name)
        p.drawString(300, y_position, entry.UserInfo.email)
        p.drawString(400, y_position, entry.phone_no)
        p.drawString(500, y_position, entry.gender)
        p.drawString(600, y_position, str(entry.dob))
        p.drawString(700, y_position, entry.address1)
        p.drawString(800, y_position, entry.address2)
        p.drawString(900, y_position, entry.pincode)
        p.drawString(1000, y_position, entry.state)
        p.drawString(1100, y_position, entry.country)

    p.showPage()
    p.save()

    return response

def download_data(request, option):
    data = ContactInfo.objects.all()

    if option == '1':
        return download_contact_info_csv(data)
    elif option == '2':
        return download_personal_info_csv(data)
    elif option == '3':
        return download_combined_csv(data)
    elif option == '4':
        return download_combined_pdf(data)
    else:
        return HttpResponse("Invalid option")