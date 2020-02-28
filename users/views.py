from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.template.defaultfilters import cut
from django.views.generic import ListView, CreateView

# Create your views here.
from users.models import UserProfile, CustomUser
from .forms import LoginForm, CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.hashers import make_password


def login_page(request):
    form = LoginForm(request.POST or None)

    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request,user)
            if user.is_superuser:
                return redirect('clientDashboard')
            elif user.userType == 'Client' or user.userType == 'Doctor':
                return redirect('dashboard')
            elif user.userType == 'Nurse':
                return redirect('nurseDashboard')

    context = {
        "form": form
    }

    return render(request, "authentication/views/loginpage.html", context)


def SignUp(request):
    if request.method == 'POST':
        if request.POST:
            if request.user.is_superuser:
                hashed = make_password(request.POST['password2'])
                obj = CustomUser.objects.create(username=request.POST['username'],
                                                 email=request.POST['email'],
                                                 password=hashed,
                                                 userType=request.POST['userType'],
                                                 hospitalName=request.POST['hospitalName']
                                                 )
                obj.save()
                if request.user.is_authenticated:
                    return redirect('users:addUser')
                else:
                    return render(request, 'authentication/views/error.html', {})
            elif request.user.userType == 'Client':
                hashed = make_password(request.POST['password2'])
                if request.POST['userType'] == 'Nurse':
                    specialization = 'N/A'
                    obj = CustomUser.objects.create(
                        username=request.POST['username'],
                        firstName=request.POST['firstName'],
                        middleName=request.POST['middleName'],
                        lastName=request.POST['lastName'],
                        gender=request.POST['gender'],
                        specialization=specialization,
                        email=request.POST['email'],
                        mobile_number=request.POST['mobile_number'],
                        homeAddress=request.POST['homeAddress'],
                        password=hashed,
                        userType=request.POST['userType'],
                        ward=request.POST['ward'],
                    )
                    obj.save()
                elif request.POST['userType'] == 'Doctor':
                    specialization = request.POST['specialization']
                    obj = CustomUser.objects.create(
                        username=request.POST['username'],
                        firstName=request.POST['firstName'],
                        middleName=request.POST['middleName'],
                        lastName=request.POST['lastName'],
                        gender=request.POST['gender'],
                        specialization=specialization,
                        email=request.POST['email'],
                        mobile_number=request.POST['mobile_number'],
                        homeAddress=request.POST['homeAddress'],
                        password=hashed,
                        userType=request.POST['userType'],
                        ward=request.POST['ward'],
                        doctorPK=request.POST['username']
                    )
                    obj.save()

                if request.user.is_authenticated:
                    return redirect('users:addUser')
                else:
                    return render(request, 'authentication/views/error.html', {})
            elif request.user.userType == 'Nurse':
                first_name = request.POST['firstName']
                lower_fname = first_name.replace(" ", "").lower()
                middle_name = request.POST['middleName']
                lower_mname = middle_name.replace(" ", "").lower()
                last_name = request.POST['lastName']
                lower_lname = last_name.replace(" ", "").lower()
                mobileNumber = request.POST['mobile_number']
                hashed_password = make_password(lower_mname)
                username = lower_fname + lower_lname + mobileNumber
                user_type = 'Patient'

                obj = CustomUser.objects.create(
                    username=username,
                    firstName=first_name,
                    middleName=middle_name,
                    lastName=last_name,
                    email=request.POST['email'],
                    mobile_number=mobileNumber,
                    gender=request.POST['gender'],
                    password=hashed_password,
                    userType=user_type,
                    ward=request.POST['ward'],
                    doctorPK=request.POST['doctorPK'],
                )
                obj.save()
                if request.user.is_authenticated:
                    return redirect('users:addUser')
                else:
                    return render(request, 'authentication/views/error.html', {})
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/views/add_user.html', {'form': form})



class ClientListView(ListView):
    template_name = "clients/views/clients_table.html"
    def get_queryset(self, *args, **kwargs):
        qs = CustomUser.objects.filter(userType="Client")
        print(qs)
        context = {
            'qs': qs
        }
        return context


class DoctorListView(ListView):
    template_name = "doctors/views/doctors_table.html"
    def get_queryset(self, *args, **kwargs):
        qs = CustomUser.objects.filter(userType="Doctor")
        context = {
            'qs': qs
        }
        return context
class NurseListView(ListView):
    template_name = "nurses/views/nurses_table.html"
    def get_queryset(self, *args, **kwargs):
        qs = CustomUser.objects.filter(userType="Nurse")
        context = {
            'qs': qs
        }
        return context

class PatientListView(ListView):
    template_name = "patients/views/patients_table.html"
    def get_queryset(self, *args, **kwargs):

        qs = CustomUser.objects.filter(userType="Patient")
        context = {
            'qs': qs
        }
        return context
def PatientList(request):
    if request.user.is_authenticated and request.user.userType == 'Nurse':
        sentryWards = request.user.ward
        print(sentryWards)
        qs = CustomUser.objects.filter(userType='Patient', ward=sentryWards)
        print(qs)
        context = {
            'qs': qs
        }
        return render(request, 'patients/views/patients_table.html', context)
    elif request.user.is_authenticated and request.user.userType == 'Doctor':
        docPK = request.user.username
        print(docPK)
        qs = CustomUser.objects.filter(userType='Patient', doctorPK=docPK)
        print(qs)
        context = {
            'qs': qs
        }
        return render(request, 'patients/views/patients_table.html', context)
    else:
        return render(request, 'authentication/views/error.html', {})

def edit_profile(request, username):
    if request.user.is_superuser:
        user = CustomUser.objects.get(username=username)
    else:
        user = CustomUser.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        # print(request.user.is_authenticated())
        if form.is_valid():
            # form.middle_name = request.POST['middle_name']
            # form.profile_image = request.FILES.get('profile_image', user.profile_image)
            form.save()
            return redirect('users:profile', user)
    else:
        form = CustomUserChangeForm(instance=user)
        args = {
            'form': form,
            'user': user
            }
        if user.username == request.user.username or request.user.is_superuser:
            return render(request, 'users/edit_profile.html', args)
        else:
            return render(request, 'authentication/views/error.html', {})

class user_profile(ListView):
    model = UserProfile
    count_hit = True
    template_name = 'users/profile.html'

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)

def get_user_profile(request, username):
    user = CustomUser.objects.get(username=username)
    if request.user.username == user.username:
        return render(request, 'users/profile.html', {"user":user})
    elif user.userType == 'Patient' and request.user.userType == 'Doctor':
        return render(request, 'users/profile.html', {"user": user})
    elif user.userType == 'Patient' and request.user.userType == 'Nurse':
        return render(request, 'users/profile.html', {"user": user})
    elif user.userType == 'Patient' and request.user.userType == 'Client':
        return render(request, 'users/profile.html', {"user": user})
    elif user.userType == 'Doctor' and request.user.userType == 'Client':
        return render(request, 'users/profile.html', {"user": user})
    elif user.userType == 'Nurse' and request.user.userType == 'Client':
        return render(request, 'users/profile.html', {"user": user})
    elif user.userType == 'Nurse' and user.username != request.user.username and request.user.userType == 'Nurse':
        return render(request, 'authentication/views/error.html', {})
    elif user.userType == 'Doctor' and user.username != request.user.username and request.user.userType == 'Doctor':
        return render(request, 'authentication/views/error.html', {})
    elif user.userType == 'Client' and user.username != request.user.username and request.user.userType == 'Client':
        return render(request, 'authentication/views/error.html', {})
    else:
        return render(request, 'authentication/views/error.html', {})

def delete(request, username):
    user = CustomUser.objects.get(username=username)
    if request.user.is_superuser:
        user.delete()
        return redirect('users:clientList')
    elif request.user.userType == 'Client':
        user.delete()
        return redirect('users:doctorList')
    elif request.user.userType == 'Doctor':
        user.delete()
        return redirect('users:patientList')
    else:
        return render(request, 'authentication/views/error.html', {})

def edit(request, username):
    user = CustomUser.objects.get(username=username)
    if user.userType == 'Patient' and request.user.userType == 'Doctor':
        if request.method == 'POST':
            if request.POST:
                user.medicalProblems = request.POST['medicalProblems']
                user.medicalDirectives = request.POST['medicalDirectives']
                user.medications  = request.POST['medications']
                user.alkPhos = request.POST['alkPhos']
                user.bun = request.POST['bun']
                user.calcium = request.POST['calcium']
                user.chloride = request.POST['chloride']
                user.co2 = request.POST['co2']
                user.creatinine = request.POST['creatinine']
                user.po4 = request.POST['po4']
                user.potassium = request.POST['potassium']
                user.sgot = request.POST['sgot']
                user.biliTotal = request.POST['biliTotal']
                user.uricAcid = request.POST['uricAcid']
                user.ldhTotal = request.POST['ldhTotal']
                user.sodium = request.POST['sodium']
                user.bgRandom = request.POST['bgRandom']
                user.height = request.POST['height']
                user.weight = request.POST['weight']
                user.temperature = request.POST['temperature']
                user.tempSite = request.POST['tempSite']
                user.pulseRate = request.POST['pulseRate']
                user.pulseRhytm = request.POST['pulseRhytm']
                user.respRate = request.POST['respRate']
                user.bpSystolic = request.POST['bpSystolic']
                user.bpDiastolic = request.POST['bpDiastolic']
                user.cholesterol = request.POST['cholesterol']
                user.hdl = request.POST['hdl']
                user.ldl = request.POST['ldl']
                user.bgRandom = request.POST['bgRandom']
                user.cxr = request.POST['cxr']
                user.ekg = request.POST['ekg']
                user.papSmear = request.POST['papSmear']
                user.mammogram = request.POST['mammogram']
                user.hemoccult = request.POST['hemoccult']
                user.fluVax = request.POST['fluVax']
                user.pneumovax = request.POST['pneumovax']
                user.tdBooster = request.POST['tdBooster']
                user.footExam = request.POST['footExam']
                user.eyeExam = request.POST['eyeExam']
                user.save()
            return redirect('users:patientList')
        return render(request, 'authentication/views/edit_specific_profile.html', {'user': user})
    elif user.userType == 'Patient' and request.user.userType == 'Nurse':
        if request.method == 'POST':
            if request.POST:
                user.medicalProblems = request.POST['medicalProblems']
                user.medicalDirectives = request.POST['medicalDirectives']
                user.medications  = request.POST['medications']
                user.alkPhos = request.POST['alkPhos']
                user.bun = request.POST['bun']
                user.calcium = request.POST['calcium']
                user.chloride = request.POST['chloride']
                user.co2 = request.POST['co2']
                user.creatinine = request.POST['creatinine']
                user.po4 = request.POST['po4']
                user.potassium = request.POST['potassium']
                user.sgot = request.POST['sgot']
                user.biliTotal = request.POST['biliTotal']
                user.uricAcid = request.POST['uricAcid']
                user.ldhTotal = request.POST['ldhTotal']
                user.sodium = request.POST['sodium']
                user.bgRandom = request.POST['bgRandom']
                user.height = request.POST['height']
                user.weight = request.POST['weight']
                user.temperature = request.POST['temperature']
                user.tempSite = request.POST['tempSite']
                user.pulseRate = request.POST['pulseRate']
                user.pulseRhytm = request.POST['pulseRhytm']
                user.respRate = request.POST['respRate']
                user.bpSystolic = request.POST['bpSystolic']
                user.bpDiastolic = request.POST['bpDiastolic']
                user.cholesterol = request.POST['cholesterol']
                user.hdl = request.POST['hdl']
                user.ldl = request.POST['ldl']
                user.bgRandom = request.POST['bgRandom']
                user.cxr = request.POST['cxr']
                user.ekg = request.POST['ekg']
                user.papSmear = request.POST['papSmear']
                user.mammogram = request.POST['mammogram']
                user.hemoccult = request.POST['hemoccult']
                user.fluVax = request.POST['fluVax']
                user.pneumovax = request.POST['pneumovax']
                user.tdBooster = request.POST['tdBooster']
                user.footExam = request.POST['footExam']
                user.eyeExam = request.POST['eyeExam']
                user.save()
            return redirect('users:patientList')
        return render(request, 'authentication/views/edit_specific_profile.html', {'user': user})
    elif user.userType == 'Patient' and request.user.userType == 'Client':
        if request.method == 'POST':
            if request.POST:
                user.medicalProblems = request.POST['medicalProblems']
                user.medicalDirectives = request.POST['medicalDirectives']
                user.medications  = request.POST['medications']
                user.alkPhos = request.POST['alkPhos']
                user.bun = request.POST['bun']
                user.calcium = request.POST['calcium']
                user.chloride = request.POST['chloride']
                user.co2 = request.POST['co2']
                user.creatinine = request.POST['creatinine']
                user.po4 = request.POST['po4']
                user.potassium = request.POST['potassium']
                user.sgot = request.POST['sgot']
                user.biliTotal = request.POST['biliTotal']
                user.uricAcid = request.POST['uricAcid']
                user.ldhTotal = request.POST['ldhTotal']
                user.sodium = request.POST['sodium']
                user.bgRandom = request.POST['bgRandom']
                user.height = request.POST['height']
                user.weight = request.POST['weight']
                user.temperature = request.POST['temperature']
                user.tempSite = request.POST['tempSite']
                user.pulseRate = request.POST['pulseRate']
                user.pulseRhytm = request.POST['pulseRhytm']
                user.respRate = request.POST['respRate']
                user.bpSystolic = request.POST['bpSystolic']
                user.bpDiastolic = request.POST['bpDiastolic']
                user.cholesterol = request.POST['cholesterol']
                user.hdl = request.POST['hdl']
                user.ldl = request.POST['ldl']
                user.bgRandom = request.POST['bgRandom']
                user.cxr = request.POST['cxr']
                user.ekg = request.POST['ekg']
                user.papSmear = request.POST['papSmear']
                user.mammogram = request.POST['mammogram']
                user.hemoccult = request.POST['hemoccult']
                user.fluVax = request.POST['fluVax']
                user.pneumovax = request.POST['pneumovax']
                user.tdBooster = request.POST['tdBooster']
                user.footExam = request.POST['footExam']
                user.eyeExam = request.POST['eyeExam']
                user.save()
            return redirect('users:patientList')
        return render(request, 'authentication/views/edit_specific_profile.html', {'user': user})
    elif user.userType == 'Doctor' and request.user.userType == 'Client':
        if request.method == 'POST':
            if request.POST:
                user.medicalProblems = request.POST['medicalProblems']
                user.medicalDirectives = request.POST['medicalDirectives']
                user.medications  = request.POST['medications']
                user.alkPhos = request.POST['alkPhos']
                user.bun = request.POST['bun']
                user.calcium = request.POST['calcium']
                user.chloride = request.POST['chloride']
                user.co2 = request.POST['co2']
                user.creatinine = request.POST['creatinine']
                user.po4 = request.POST['po4']
                user.potassium = request.POST['potassium']
                user.sgot = request.POST['sgot']
                user.biliTotal = request.POST['biliTotal']
                user.uricAcid = request.POST['uricAcid']
                user.ldhTotal = request.POST['ldhTotal']
                user.sodium = request.POST['sodium']
                user.bgRandom = request.POST['bgRandom']
                user.height = request.POST['height']
                user.weight = request.POST['weight']
                user.temperature = request.POST['temperature']
                user.tempSite = request.POST['tempSite']
                user.pulseRate = request.POST['pulseRate']
                user.pulseRhytm = request.POST['pulseRhytm']
                user.respRate = request.POST['respRate']
                user.bpSystolic = request.POST['bpSystolic']
                user.bpDiastolic = request.POST['bpDiastolic']
                user.cholesterol = request.POST['cholesterol']
                user.hdl = request.POST['hdl']
                user.ldl = request.POST['ldl']
                user.bgRandom = request.POST['bgRandom']
                user.cxr = request.POST['cxr']
                user.ekg = request.POST['ekg']
                user.papSmear = request.POST['papSmear']
                user.mammogram = request.POST['mammogram']
                user.hemoccult = request.POST['hemoccult']
                user.fluVax = request.POST['fluVax']
                user.pneumovax = request.POST['pneumovax']
                user.tdBooster = request.POST['tdBooster']
                user.footExam = request.POST['footExam']
                user.eyeExam = request.POST['eyeExam']
                user.save()
            return redirect('users:patientList')
        return render(request, 'authentication/views/edit_specific_profile.html', {'user': user})
    elif user.userType == 'Nurse' and request.user.userType == 'Client':
        if request.method == 'POST':
            if request.POST:
                user.medicalProblems = request.POST['medicalProblems']
                user.medicalDirectives = request.POST['medicalDirectives']
                user.medications  = request.POST['medications']
                user.alkPhos = request.POST['alkPhos']
                user.bun = request.POST['bun']
                user.calcium = request.POST['calcium']
                user.chloride = request.POST['chloride']
                user.co2 = request.POST['co2']
                user.creatinine = request.POST['creatinine']
                user.po4 = request.POST['po4']
                user.potassium = request.POST['potassium']
                user.sgot = request.POST['sgot']
                user.biliTotal = request.POST['biliTotal']
                user.uricAcid = request.POST['uricAcid']
                user.ldhTotal = request.POST['ldhTotal']
                user.sodium = request.POST['sodium']
                user.bgRandom = request.POST['bgRandom']
                user.height = request.POST['height']
                user.weight = request.POST['weight']
                user.temperature = request.POST['temperature']
                user.tempSite = request.POST['tempSite']
                user.pulseRate = request.POST['pulseRate']
                user.pulseRhytm = request.POST['pulseRhytm']
                user.respRate = request.POST['respRate']
                user.bpSystolic = request.POST['bpSystolic']
                user.bpDiastolic = request.POST['bpDiastolic']
                user.cholesterol = request.POST['cholesterol']
                user.hdl = request.POST['hdl']
                user.ldl = request.POST['ldl']
                user.bgRandom = request.POST['bgRandom']
                user.cxr = request.POST['cxr']
                user.ekg = request.POST['ekg']
                user.papSmear = request.POST['papSmear']
                user.mammogram = request.POST['mammogram']
                user.hemoccult = request.POST['hemoccult']
                user.fluVax = request.POST['fluVax']
                user.pneumovax = request.POST['pneumovax']
                user.tdBooster = request.POST['tdBooster']
                user.footExam = request.POST['footExam']
                user.eyeExam = request.POST['eyeExam']
                user.save()
            return redirect('users:patientList')
        return render(request, 'authentication/views/edit_specific_profile.html', {'user': user})
    else:
        return render(request, 'authentication/views/error.html', {})


def edit_profile(request, username):
    user = CustomUser.objects.get(username=username)
    if user.username == request.user.username:
        if request.method == 'POST':
            if request.POST:
                if request.POST['password2'] == "":
                    user.firstName = request.POST['firstName']
                    user.middleName = request.POST['middleName']
                    user.lastName = request.POST['lastName']
                    user.email = request.POST['email']
                    user.mobile_number = request.POST['mobile_number']
                    user.birthDate = request.POST['birthDate']
                    user.homeAddress = request.POST['homeAddress']
                    user.username = request.POST['username']
                    user.save()
                elif request.POST['password1'] != request.POST['password2']:
                    return redirect('users:edit_profile')
                else:
                    hashed = make_password(request.POST['password2'])
                    user.firstName = request.POST['firstName']
                    user.middleName = request.POST['middleName']
                    user.lastName = request.POST['lastName']
                    user.email = request.POST['email']
                    user.mobile_number = request.POST['mobile_number']
                    user.birthDate = request.POST['birthDate']
                    user.homeAddress = request.POST['homeAddress']
                    user.username = request.POST['username']
                    user.password = hashed
                    user.save()
                    login(request, user)
                return redirect('users:profile', request.user.username)
        else:
            return render(request, 'authentication/views/edit_profile.html', {'user': user})
    else:
        return render(request, 'authentication/views/error.html', {})
