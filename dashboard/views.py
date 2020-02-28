from datetime import date, datetime
from time import strftime

from django.contrib.auth.hashers import make_password
from django.db.models import Count
from django.db.models.functions import TruncMonth, TruncDate
from django.shortcuts import render, redirect
# from pipenv.vendor.tomlkit import item

from users.models import CustomUser


def dashboard(request):
    if request.user.is_authenticated and request.user.userType == 'Client':
        totalPatients = CustomUser.objects.filter(userType='Patient').count()
        totalNurses = CustomUser.objects.filter(userType='Nurse').count()
        totalDoctors = CustomUser.objects.filter(userType='Doctor').count()
        today = date.today().strftime('%m')

        totalPatientsTodaysMonth = CustomUser.objects.annotate(month=TruncMonth('date_joined'))\
            .values('month').annotate(total=Count('date_joined')).filter(userType='Patient', date_joined__month=today)


        context = {
            'totalPatients': totalPatients,
            'totalNurses': totalNurses,
            'totalDoctors': totalDoctors,
            'totalPatientsTodaysMonth': totalPatientsTodaysMonth
        }
        return render(request, 'dashboards/views/patient_dashboard.html', context)
    elif request.user.is_authenticated and request.user.userType == 'Doctor':
        today = datetime.now()
        yearToday = today.strftime('%Y')
        totalPatientsForDoctor = CustomUser.objects.filter(userType='Patient', doctorPK=request.user.doctorPK).count()
        totalPatientsForDoctorThisMonth = CustomUser.objects.annotate(month=TruncMonth('date_joined')) \
            .values('month').annotate(total=Count('date_joined')) \
            .filter(userType='Patient', doctorPK=request.user.doctorPK)
        pJanTotal = CustomUser.objects.filter(userType='Patient', date_joined__month='01').count()
        pFebTotal = CustomUser.objects.filter(userType='Patient', date_joined__month='02').count()
        pMarTotal = CustomUser.objects.filter(userType='Patient', date_joined__month='03').count()
        pAprTotal = CustomUser.objects.filter(userType='Patient', date_joined__month='04').count()
        pMayTotal = CustomUser.objects.filter(userType='Patient', date_joined__month='05').count()
        pJunTotal = CustomUser.objects.filter(userType='Patient', date_joined__month='06').count()
        pJulTotal = CustomUser.objects.filter(userType='Patient', date_joined__month='07').count()
        pAugTotal = CustomUser.objects.filter(userType='Patient', date_joined__month='08').count()
        pSepTotal = CustomUser.objects.filter(userType='Patient', date_joined__month='09').count()
        pOctTotal = CustomUser.objects.filter(userType='Patient', date_joined__month='10').count()
        pNovTotal = CustomUser.objects.filter(userType='Patient', date_joined__month='11').count()
        pDecTotal = CustomUser.objects.filter(userType='Patient', date_joined__month='12').count()

        pJanTotalNew = CustomUser.objects.filter(userType='Patient', date_joined__month='01', date_joined__year=yearToday).count()
        pFebTotalNew = CustomUser.objects.filter(userType='Patient', date_joined__month='02', date_joined__year=yearToday).count()
        pMarTotalNew = CustomUser.objects.filter(userType='Patient', date_joined__month='03', date_joined__year=yearToday).count()
        pAprTotalNew = CustomUser.objects.filter(userType='Patient', date_joined__month='04', date_joined__year=yearToday).count()
        pMayTotalNew = CustomUser.objects.filter(userType='Patient', date_joined__month='05', date_joined__year=yearToday).count()
        pJunTotalNew = CustomUser.objects.filter(userType='Patient', date_joined__month='06', date_joined__year=yearToday).count()
        pJulTotalNew = CustomUser.objects.filter(userType='Patient', date_joined__month='07', date_joined__year=yearToday).count()
        pAugTotalNew = CustomUser.objects.filter(userType='Patient', date_joined__month='08', date_joined__year=yearToday).count()
        pSepTotalNew = CustomUser.objects.filter(userType='Patient', date_joined__month='09', date_joined__year=yearToday).count()
        pOctTotalNew = CustomUser.objects.filter(userType='Patient', date_joined__month='10', date_joined__year=yearToday).count()
        pNovTotalNew = CustomUser.objects.filter(userType='Patient', date_joined__month='11', date_joined__year=yearToday).count()
        pDecTotalNew = CustomUser.objects.filter(userType='Patient', date_joined__month='12', date_joined__year=yearToday).count()

        pDTjan = CustomUser.objects.filter(userType='Patient', date_joined__month='01',
                                        medicalProblems__contains='Stroke').count()
        pDTfeb = CustomUser.objects.filter(userType='Patient', date_joined__month='02',
                                        medicalProblems__contains='Stroke').count()
        pDTmar = CustomUser.objects.filter(userType='Patient', date_joined__month='03',
                                        medicalProblems__contains='Stroke').count()
        pDTapr = CustomUser.objects.filter(userType='Patient', date_joined__month='04',
                                        medicalProblems__contains='Stroke').count()
        pDTmay = CustomUser.objects.filter(userType='Patient', date_joined__month='05',
                                        medicalProblems__contains='Stroke').count()
        pDTjun = CustomUser.objects.filter(userType='Patient', date_joined__month='06',
                                        medicalProblems__contains='Stroke').count()
        pDTjul = CustomUser.objects.filter(userType='Patient', date_joined__month='07',
                                        medicalProblems__contains='Stroke').count()
        pDTaug = CustomUser.objects.filter(userType='Patient', date_joined__month='08',
                                        medicalProblems__contains='Stroke').count()
        pDTsep = CustomUser.objects.filter(userType='Patient', date_joined__month='09',
                                        medicalProblems__contains='Stroke').count()
        pDToct = CustomUser.objects.filter(userType='Patient', date_joined__month='10',
                                        medicalProblems__contains='Stroke').count()
        pDTnov = CustomUser.objects.filter(userType='Patient', date_joined__month='11',
                                        medicalProblems__contains='Stroke').count()
        pDTdec = CustomUser.objects.filter(userType='Patient', date_joined__month='12',
                                        medicalProblems__contains='Stroke').count()

        pDTjanw = CustomUser.objects.filter(userType='Patient', date_joined__month='01',
                                           medicalProblems__contains='Tuberculosis').count()
        pDTfebw = CustomUser.objects.filter(userType='Patient', date_joined__month='02',
                                           medicalProblems__contains='Tuberculosis').count()
        pDTmarw = CustomUser.objects.filter(userType='Patient', date_joined__month='03',
                                           medicalProblems__contains='Tuberculosis').count()
        pDTaprw = CustomUser.objects.filter(userType='Patient', date_joined__month='04',
                                           medicalProblems__contains='Tuberculosis').count()
        pDTmayw = CustomUser.objects.filter(userType='Patient', date_joined__month='05',
                                           medicalProblems__contains='Tuberculosis').count()
        pDTjunw = CustomUser.objects.filter(userType='Patient', date_joined__month='06',
                                           medicalProblems__contains='Tuberculosis').count()
        pDTjulw = CustomUser.objects.filter(userType='Patient', date_joined__month='07',
                                           medicalProblems__contains='Tuberculosis').count()
        pDTaugw = CustomUser.objects.filter(userType='Patient', date_joined__month='08',
                                           medicalProblems__contains='Tuberculosis').count()
        pDTsepw = CustomUser.objects.filter(userType='Patient', date_joined__month='09',
                                           medicalProblems__contains='Tuberculosis').count()
        pDToctw = CustomUser.objects.filter(userType='Patient', date_joined__month='10',
                                           medicalProblems__contains='Tuberculosis').count()
        pDTnovw = CustomUser.objects.filter(userType='Patient', date_joined__month='11',
                                           medicalProblems__contains='Tuberculosis').count()
        pDTdecw = CustomUser.objects.filter(userType='Patient', date_joined__month='12',
                                           medicalProblems__contains='Tuberculosis').count()

        pDTjanwe = CustomUser.objects.filter(userType='Patient', date_joined__month='01',
                                            medicalProblems__contains='Hypertension').count()
        pDTfebwe = CustomUser.objects.filter(userType='Patient', date_joined__month='02',
                                            medicalProblems__contains='Hypertension').count()
        pDTmarwe = CustomUser.objects.filter(userType='Patient', date_joined__month='03',
                                            medicalProblems__contains='Hypertension').count()
        pDTaprwe = CustomUser.objects.filter(userType='Patient', date_joined__month='04',
                                            medicalProblems__contains='Hypertension').count()
        pDTmaywe = CustomUser.objects.filter(userType='Patient', date_joined__month='05',
                                            medicalProblems__contains='Hypertension').count()
        pDTjunwe = CustomUser.objects.filter(userType='Patient', date_joined__month='06',
                                            medicalProblems__contains='Hypertension').count()
        pDTjulwe = CustomUser.objects.filter(userType='Patient', date_joined__month='07',
                                            medicalProblems__contains='Hypertension').count()
        pDTaugwe = CustomUser.objects.filter(userType='Patient', date_joined__month='08',
                                            medicalProblems__contains='Hypertension').count()
        pDTsepwe = CustomUser.objects.filter(userType='Patient', date_joined__month='09',
                                            medicalProblems__contains='Hypertension').count()
        pDToctwe = CustomUser.objects.filter(userType='Patient', date_joined__month='10',
                                            medicalProblems__contains='Hypertension').count()
        pDTnovwe = CustomUser.objects.filter(userType='Patient', date_joined__month='11',
                                            medicalProblems__contains='Hypertension').count()
        pDTdecwe = CustomUser.objects.filter(userType='Patient', date_joined__month='12',
                                            medicalProblems__contains='Hypertension').count()



        pDTjanq = CustomUser.objects.filter(userType='Patient', date_joined__month='01',
                                           medicalProblems__contains='Stroke', date_joined__year=yearToday).count()
        pDTfebq = CustomUser.objects.filter(userType='Patient', date_joined__month='02',
                                           medicalProblems__contains='Stroke', date_joined__year=yearToday).count()
        pDTmarq = CustomUser.objects.filter(userType='Patient', date_joined__month='03',
                                           medicalProblems__contains='Stroke', date_joined__year=yearToday).count()
        pDTaprq = CustomUser.objects.filter(userType='Patient', date_joined__month='04',
                                           medicalProblems__contains='Stroke', date_joined__year=yearToday).count()
        pDTmayq = CustomUser.objects.filter(userType='Patient', date_joined__month='05',
                                           medicalProblems__contains='Stroke', date_joined__year=yearToday).count()
        pDTjunq = CustomUser.objects.filter(userType='Patient', date_joined__month='06',
                                           medicalProblems__contains='Stroke', date_joined__year=yearToday).count()
        pDTjulq = CustomUser.objects.filter(userType='Patient', date_joined__month='07',
                                           medicalProblems__contains='Stroke', date_joined__year=yearToday).count()
        pDTaugq = CustomUser.objects.filter(userType='Patient', date_joined__month='08',
                                           medicalProblems__contains='Stroke', date_joined__year=yearToday).count()
        pDTsepq = CustomUser.objects.filter(userType='Patient', date_joined__month='09',
                                           medicalProblems__contains='Stroke', date_joined__year=yearToday).count()
        pDToctq = CustomUser.objects.filter(userType='Patient', date_joined__month='10',
                                           medicalProblems__contains='Stroke', date_joined__year=yearToday).count()
        pDTnovq = CustomUser.objects.filter(userType='Patient', date_joined__month='11',
                                           medicalProblems__contains='Stroke', date_joined__year=yearToday).count()
        pDTdecq = CustomUser.objects.filter(userType='Patient', date_joined__month='12',
                                           medicalProblems__contains='Stroke', date_joined__year=yearToday).count()

        pDTjanqw = CustomUser.objects.filter(userType='Patient', date_joined__month='01',
                                            medicalProblems__contains='Tuberculosis', date_joined__year=yearToday).count()
        pDTfebqw = CustomUser.objects.filter(userType='Patient', date_joined__month='02',
                                            medicalProblems__contains='Tuberculosis', date_joined__year=yearToday).count()
        pDTmarqw = CustomUser.objects.filter(userType='Patient', date_joined__month='03',
                                            medicalProblems__contains='Tuberculosis', date_joined__year=yearToday).count()
        pDTaprqw = CustomUser.objects.filter(userType='Patient', date_joined__month='04',
                                            medicalProblems__contains='Tuberculosis', date_joined__year=yearToday).count()
        pDTmayqw = CustomUser.objects.filter(userType='Patient', date_joined__month='05',
                                            medicalProblems__contains='Tuberculosis', date_joined__year=yearToday).count()
        pDTjunqw = CustomUser.objects.filter(userType='Patient', date_joined__month='06',
                                            medicalProblems__contains='Tuberculosis', date_joined__year=yearToday).count()
        pDTjulqw = CustomUser.objects.filter(userType='Patient', date_joined__month='07',
                                            medicalProblems__contains='Tuberculosis', date_joined__year=yearToday).count()
        pDTaugqw = CustomUser.objects.filter(userType='Patient', date_joined__month='08',
                                            medicalProblems__contains='Tuberculosis', date_joined__year=yearToday).count()
        pDTsepqw = CustomUser.objects.filter(userType='Patient', date_joined__month='09',
                                            medicalProblems__contains='Tuberculosis', date_joined__year=yearToday).count()
        pDToctqw = CustomUser.objects.filter(userType='Patient', date_joined__month='10',
                                            medicalProblems__contains='Tuberculosis', date_joined__year=yearToday).count()
        pDTnovqw = CustomUser.objects.filter(userType='Patient', date_joined__month='11',
                                            medicalProblems__contains='Tuberculosis', date_joined__year=yearToday).count()
        pDTdecqw = CustomUser.objects.filter(userType='Patient', date_joined__month='12',
                                            medicalProblems__contains='Tuberculosis', date_joined__year=yearToday).count()

        pDTjanqwr = CustomUser.objects.filter(userType='Patient', date_joined__month='01',
                                             medicalProblems__contains='Hypertension',
                                             date_joined__year=yearToday).count()
        pDTfebqwr = CustomUser.objects.filter(userType='Patient', date_joined__month='02',
                                             medicalProblems__contains='Hypertension',
                                             date_joined__year=yearToday).count()
        pDTmarqwr = CustomUser.objects.filter(userType='Patient', date_joined__month='03',
                                             medicalProblems__contains='Hypertension',
                                             date_joined__year=yearToday).count()
        pDTaprqwr = CustomUser.objects.filter(userType='Patient', date_joined__month='04',
                                             medicalProblems__contains='Tuberculosis',
                                             date_joined__year=yearToday).count()
        pDTmayqwr = CustomUser.objects.filter(userType='Patient', date_joined__month='05',
                                             medicalProblems__contains='Hypertension',
                                             date_joined__year=yearToday).count()
        pDTjunqwr = CustomUser.objects.filter(userType='Patient', date_joined__month='06',
                                             medicalProblems__contains='Hypertension',
                                             date_joined__year=yearToday).count()
        pDTjulqwr = CustomUser.objects.filter(userType='Patient', date_joined__month='07',
                                             medicalProblems__contains='Hypertension',
                                             date_joined__year=yearToday).count()
        pDTaugqwr = CustomUser.objects.filter(userType='Patient', date_joined__month='08',
                                             medicalProblems__contains='Hypertension',
                                             date_joined__year=yearToday).count()
        pDTsepqwr = CustomUser.objects.filter(userType='Patient', date_joined__month='09',
                                             medicalProblems__contains='Hypertension',
                                             date_joined__year=yearToday).count()
        pDToctqwr = CustomUser.objects.filter(userType='Patient', date_joined__month='10',
                                             medicalProblems__contains='Hypertension',
                                             date_joined__year=yearToday).count()
        pDTnovqwr = CustomUser.objects.filter(userType='Patient', date_joined__month='11',
                                             medicalProblems__contains='Hypertension',
                                             date_joined__year=yearToday).count()
        pDTdecqwr = CustomUser.objects.filter(userType='Patient', date_joined__month='12',
                                             medicalProblems__contains='Hypertension',
                                             date_joined__year=yearToday).count()



        m = 0
        for foo in totalPatientsForDoctorThisMonth:
            m = foo['total']
        context = {
            'totalPatientsForDoctor': totalPatientsForDoctor,
            'm': m,
            'pJanTotal': pJanTotal,
            'pFebTotal': pFebTotal,
            'pMarTotal': pMarTotal,
            'pAprTotal': pAprTotal,
            'pMayTotal': pMayTotal,
            'pJunTotal': pJunTotal,
            'pJulTotal': pJulTotal,
            'pAugTotal': pAugTotal,
            'pSepTotal': pSepTotal,
            'pOctTotal': pOctTotal,
            'pNovTotal': pNovTotal,
            'pDecTotal': pDecTotal,
            'pJanTotalNew': pJanTotalNew,
            'pFebTotalNew': pFebTotalNew,
            'pMarTotalNew': pMarTotalNew,
            'pAprTotalNew': pAprTotalNew,
            'pMayTotalNew:': pMayTotalNew,
            'pJunTotalNew': pJunTotalNew,
            'pJulTotalNew': pJulTotalNew,
            'pAugTotalNew': pAugTotalNew,
            'pSepTotalNew': pSepTotalNew,
            'pOctTotalNew': pOctTotalNew,
            'pNovTotalNew': pNovTotalNew,
            'pDecTotalNew': pDecTotalNew,
            'pDTjan': pDTjan,
            'pDTfeb': pDTfeb,
            'pDTmar': pDTmar,
            'pDTapr': pDTapr,
            'pDTmay': pDTmay,
            'pDTjun': pDTjun,
            'pDTjul': pDTjul,
            'pDTaug': pDTaug,
            'pDTsep': pDTsep,
            'pDToct': pDToct,
            'pDTnov': pDTnov,
            'pDTdec': pDTdec,
            'pDTjanq': pDTjanq,
            'pDTfebq': pDTfebq,
            'pDTmarq': pDTmarq,
            'pDTaprq': pDTaprq,
            'pDTmayq': pDTmayq,
            'pDTjunq': pDTjunq,
            'pDTjulq': pDTjulq,
            'pDTaugq': pDTaugq,
            'pDTsepq': pDTsepq,
            'pDToctq': pDToctq,
            'pDTnovq': pDTnovq,
            'pDTdecq': pDTdecq,
            'pDTjanw': pDTjanw,
            'pDTfebw': pDTfebw,
            'pDTmarw': pDTmarw,
            'pDTaprw': pDTaprw,
            'pDTmayw': pDTmayw,
            'pDTjunw': pDTjunw,
            'pDTjulw': pDTjulw,
            'pDTaugw': pDTaugw,
            'pDTsepw': pDTsepw,
            'pDToctw': pDToctw,
            'pDTnovw': pDTnovw,
            'pDTdecw': pDTdecw,
            'pDTjanqw': pDTjanqw,
            'pDTfebqw': pDTfebqw,
            'pDTmarqw': pDTmarqw,
            'pDTaprqw': pDTaprqw,
            'pDTmayqw': pDTmayqw,
            'pDTjunqw': pDTjunqw,
            'pDTjulqw': pDTjulqw,
            'pDTaugqw': pDTaugqw,
            'pDTsepqw': pDTsepqw,
            'pDToctqw': pDToctqw,
            'pDTnovqw': pDTnovqw,
            'pDTdecqw': pDTdecqw,
            'pDTjanwe': pDTjanwe,
            'pDTfebwe': pDTfebwe,
            'pDTmarwe': pDTmarwe,
            'pDTaprwe': pDTaprwe,
            'pDTmaywe': pDTmaywe,
            'pDTjunwe': pDTjunwe,
            'pDTjulwe': pDTjulwe,
            'pDTaugwe': pDTaugwe,
            'pDTsepwe': pDTsepwe,
            'pDToctwe': pDToctwe,
            'pDTnovwe': pDTnovwe,
            'pDTdecwe': pDTdecwe,
            'pDTjanqwr': pDTjanqwr,
            'pDTfebqwr': pDTfebqwr,
            'pDTmarqwr': pDTmarqwr,
            'pDTaprqwr': pDTaprqwr,
            'pDTmayqwr': pDTmayqwr,
            'pDTjunqwr': pDTjunqwr,
            'pDTjulqwr': pDTjulqwr,
            'pDTaugqwr': pDTaugqwr,
            'pDTsepqwr': pDTsepqwr,
            'pDToctqwr': pDToctqwr,
            'pDTnovqwr': pDTnovqwr,
            'pDTdecqwr': pDTdecqwr,







        }
        return render(request, 'dashboards/views/patient_dashboard.html', context)
    else:
        return redirect('users:login')
def nurse_dashboard(request):
    if request.user.userType == 'Nurse':
        wardOfNurse = request.user.ward
        print(wardOfNurse)
        totalPatients = CustomUser.objects.filter(userType='Patient').count()


        context = {
            'totalPatients': totalPatients,

        }

        return render(request, 'dashboards/views/nurse_dashboard.html', context)
    else:
        return render(request, 'authentication/views/error.html', {})
def analytic_dashbaord(request):
    if request.user.userType == 'Doctor' or request.user.userType == 'Client':
        return render(request, 'dashboards/views/analytics_dashboard.html', {})
    else:
        return render(request, 'authentication/views/error.html', {})

def client_dashboard(request):
    if request.user.is_superuser:
        today = date.today().strftime('%m')
        print(today)
        qs = CustomUser.objects.filter(userType='Client').count()
        sample = CustomUser.objects.annotate(month=TruncMonth('date_joined'))\
            .values('month').annotate(total=Count('date_joined')).filter(userType='Client', date_joined__month=today)
        set = CustomUser.objects.annotate(month=TruncMonth('date_joined')).values('month').annotate(total=Count('date_joined')).filter(userType='Client').values_list('total', flat=True)
        monthSet = CustomUser.objects.filter(userType='Client').annotate(month=TruncMonth('date_joined')).values_list('date_joined__month', flat=True).annotate(total=Count('date_joined__month'))
        arrayTotal = list(set)

        monthTotal = list(monthSet)
        months = []
        for month in sample:
            monthToday = month['month'].strftime('%b')

        context = {
            'qs': qs,
            'set': set,
            'sample': sample,
            'arrayTotal': arrayTotal,
            'monthTotal': monthTotal,
            'months': months,
            'monthToday': monthToday
        }
        return render(request, 'dashboards/views/client_dashboard.html', context)
    else:
        return render(request, 'authentication/views/error.html', {})