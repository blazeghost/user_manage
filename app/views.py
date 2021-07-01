from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from .models import *

# Create your views here.


def LoginPage(request):
    return render(request, 'app/login.html')


def RegisterPage(request):
    return render(request, 'app/register.html')


def IndexPage(request):
    return render(request, 'app/index.html')


def SuperAdminLoginPage(request):
    return render(request, 'app/main/login.html')


def SuperAdminLogin(request):
    username = request.POST['username']
    password = request.POST['password']

    if username == "admin" and password == "admin":
        request.session['username'] = username
        request.session['password'] = password
        return render(request, "app/main/index.html")
    else:
        message = "Username or Password doesnot match"
        return render(request, "app/main/login.html", {'msg': message})


def SuperAdminLogout(request):

    del request.session['username']
    del request.session['password']

    return HttpResponseRedirect(reverse('loginpage'))

    # return render(request, "app/login.html")


def SuperIndex(request):
    return render(request, 'app/main/index.html')


def SuperAddUser(request):
    return render(request, 'app/main/add_user.html')


def Register(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    password = request.POST['password']
    cpass = request.POST['cpassword']
    role = request.POST['role']

    testuser = Master_Table.objects.filter(Email=email)
    if testuser:
        message = "User is already exist"
        return render(request, "app/register.html", {'msg': message})
    else:
        if password == cpass:
            masteruser = Master_Table.objects.create(
                Email=email, Password=password)
            user = User.objects.create(
                m_id=masteruser, Firstname=fname, Lastname=lname, Role=role)

            message = "User Successfully Registered"
            return render(request, "app/register.html", {'msg': message})
        else:
            message = "Password and Confirm Password doesnot match"
            return render(request, "app/register.html", {'msg': message})


def SuperAddUserDetail(request):
    u_fname = request.POST['u_fname']
    u_lname = request.POST['u_lname']
    u_email = request.POST['u_email']
    u_password = request.POST['u_password']
    u_role = request.POST['u_role']
    allow_create = request.POST['allow_create']
    allow_delete = request.POST['allow_delete']
    allow_edit = request.POST['allow_edit']

    testuser = Master_Table.objects.filter(Email=u_email)
    if testuser:
        message = "User is already exist"
        return render(request, "app/main/add_user.html", {'msg': message})
    else:

        masteruser = Master_Table.objects.create(
            Email=u_email, Password=u_password)
        user = User.objects.create(
            m_id=masteruser, Firstname=u_fname, Lastname=u_lname, Role=u_role, allow_create=allow_create, allow_delete=allow_delete, allow_edit=allow_edit)

        message = "User Successfully Registered"
        return render(request, "app/main/add_user.html", {'msg': message})


def SuperUserList(request):
    userlist = User.objects.all()
    context = {
        'key1': userlist
    }

    return render(request, 'app/main/user_list.html', context)


def SuperAdminDelete(request, pk):
    m_data = Master_Table.objects.get(id=pk)
    data = User.objects.get(m_id=m_data)

    m_data.delete()
    data.delete()
    return HttpResponseRedirect(reverse('superuserlist'))


def SuperAdminEditPage(request, pk):
    data = User.objects.get(pk=pk)
    context = {
        'key1': data
    }
    return render(request, 'app/main/edit_user.html', context)


def SuperAdminEdit(request, pk):
    data = User.objects.get(pk=pk)

    data.Firstname = request.POST['u_fname']
    data.Lastname = request.POST['u_lname']
    data.Role = request.POST['u_role']
    data.m_id.Email = request.POST['u_email']
    data.m_id.Password = request.POST['u_password']
    data.allow_create = request.POST['allow_create']
    data.allow_delete = request.POST['allow_delete']
    data.allow_edit = request.POST['allow_edit']

    data.save()
    # url = f'/supereditpage/{pk}'
    # return redirect(url)
    message = "Succesfully Saved"
    userlist = User.objects.all()
    context = {
        'key1': userlist,
        'msg': message
    }

    return render(request, 'app/main/user_list.html', context)


def Login(request):
    if request.POST['role'] == "Admin":
        email = request.POST['email']
        password = request.POST['password']

        testuser = Master_Table.objects.get(Email=email)
        user = User.objects.get(m_id=testuser)
        if testuser:
            if testuser.Password == password and user.Role == "Admin":

                request.session['Role'] = user.Role
                request.session['id'] = testuser.id
                request.session['is_verified'] = testuser.is_verified
                request.session['Firstname'] = user.Firstname
                request.session['Lastname'] = user.Lastname
                request.session['Email'] = testuser.Email
                request.session['allow_create'] = user.allow_create
                request.session['allow_delete'] = user.allow_delete
                request.session['allow_edit'] = user.allow_edit

                return render(request, "app/index.html")

            else:
                message = "User Password or Role Doesnot match"
                return render(request, "app/login.html", {'msg': message})

        else:
            message = "User not Found"
            return render(request, "app/login.html", {'msg': message})

    else:
        if request.POST['role'] == "Security":
            email = request.POST['email']
            password = request.POST['password']

            testuser = Master_Table.objects.get(Email=email)
            user = User.objects.get(m_id=testuser)
            if testuser:
                if testuser.Password == password and user.Role == "Security":

                    request.session['Role'] = user.Role
                    request.session['id'] = testuser.id
                    request.session['is_verified'] = testuser.is_verified
                    request.session['Firstname'] = user.Firstname
                    request.session['Lastname'] = user.Lastname
                    request.session['Email'] = testuser.Email
                    request.session['allow_create'] = user.allow_create
                    request.session['allow_delete'] = user.allow_delete
                    request.session['allow_edit'] = user.allow_edit

                    return render(request, "app/index.html")

                else:
                    message = "User Password or Role Doesnot match"
                    return render(request, "app/login.html", {'msg': message})

            else:
                message = "User not Found"
                return render(request, "app/login.html", {'msg': message})


def Logout(request):

    del request.session['Role']
    del request.session['id']
    del request.session['Firstname']
    del request.session['Lastname']
    del request.session['Email']
    del request.session['is_verified']
    del request.session['allow_create']
    del request.session['allow_delete']
    del request.session['allow_edit']

    # return render(request, "app/login.html")
    return HttpResponseRedirect(reverse('loginpage'))


def Profile(request, pk):
    m_data = Master_Table.objects.get(id=pk)
    u_data = User.objects.get(m_id=m_data)

    context = {
        'key1': u_data
    }
    return render(request, 'app/profile.html', context)


def VisitorDetails(request):

    return render(request, 'app/visitor_details.html')


def VisitorList(request):
    data_one = Table_one.objects.all()
    data_two = Table_two.objects.all()

    context = {
        'key1': data_one,
        'key2': data_two

    }
    return render(request, 'app/visitor_list.html', context)


def AddVisitor(request, pk):
    m_data = Master_Table.objects.get(id=pk)
    user = User.objects.get(m_id=m_data)

    role = request.POST['role']

    if role == 'Admin':
        vname = request.POST['v_name']
        vpurpose = request.POST['v_purpose']
        vcontact = request.POST['v_contact']
        concern_person = request.POST['concerned_p']
        datetime = request.POST['date_time']

        data_one = Table_one.objects.create(a_id=user, visitor_name=vname, visitor_purpose=vpurpose,
                                            visitor_contact=vcontact, concerned_person=concern_person, date_time=datetime)

        msg = "Added Successfuly"
        context = {
            'keymsg': msg,
            # 'check': user,
        }
        return render(request, 'app/visitor_details.html', context)

    elif role == 'Security':
        vname = request.POST['v_name']
        vpurpose = request.POST['v_purpose']
        vcontact = request.POST['v_contact']
        concern_person = request.POST['concerned_p']
        datetime = request.POST['date_time']

        vaddress = request.POST['v_address']
        v_vechicle = request.POST['v_vechicle']

        data_one = Table_one.objects.create(a_id=user, visitor_name=vname, visitor_purpose=vpurpose,
                                            visitor_contact=vcontact, concerned_person=concern_person, date_time=datetime)

        data_two = Table_two.objects.create(
            s_id=user, tableone_id=data_one, visitor_address=vaddress, visitor_vehicle_number=v_vechicle)

        msg = "Added Successfuly"
        context = {
            'keymsg': msg,
            # 'check': user,
        }
        return render(request, 'app/visitor_details.html', context)


def AdminEditPage(request, pk):
    data_one = Table_one.objects.get(id=pk)

    context = {
        'key1': data_one,

    }

    return render(request, 'app/visitor_edit.html', context)


def SecurityEditPage(request, pk):

    data_one = Table_one.objects.get(id=pk)
    data_two = Table_two.objects.get(tableone_id=data_one)

    context = {

        'key2': data_two,
    }

    return render(request, 'app/visitor_edit.html', context)


def AdminEditVisitor(request, pk):

    data = Table_one.objects.get(id=pk)
    data.visitor_name = request.POST['v_name']
    data.visitor_purpose = request.POST['v_purpose']
    data.visitor_contact = request.POST['v_contact']
    data.concerned_person = request.POST['concerned_p']
    data.date_time = request.POST['date_time']

    print("-------------->>", data.visitor_name)

    data.save()

    message = "Changed Sucessfully"
    context = {
        'key1': data,
        'msg': message

    }

    return render(request, 'app/visitor_edit.html', context)


def SecurityEditVisitor(request, pk):
    data_one = Table_one.objects.get(id=pk)
    data_two = Table_two.objects.get(tableone_id=data_one)

    data_one.visitor_name = request.POST['v_name']
    data_one.visitor_purpose = request.POST['v_purpose']
    data_one.visitor_contact = request.POST['v_contact']
    data_one.concerned_person = request.POST['concerned_p']
    data_one.date_time = request.POST['date_time']
    data_two.visitor_address = request.POST['v_address']
    data_two.visitor_vehicle_number = request.POST['v_vechicle']

    data_one.save()
    data_two.save()

    message = "Changed Sucessfully"
    context = {

        'key2': data_two,
        'msg': message
    }

    return render(request, 'app/visitor_edit.html', context)


def AdminDelete(request, pk):
    data = Table_one.objects.get(id=pk)
    data.delete()
    return HttpResponseRedirect(reverse('visitorlist'))


def SecurityDelete(request, pk):
    data_one = Table_one.objects.get(id=pk)
    data_two = Table_two.objects.get(tableone_id=data_one)

    data_one.delete()
    data_two.delete()
    return HttpResponseRedirect(reverse('visitorlist'))
