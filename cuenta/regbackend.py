from registration.backends.default.views import RegistrationView
from .forms import ProfileForm
from .models import Profile


class MyRegistrationView(RegistrationView):

    form_class = ProfileForm

    def register(self, form_class):
        new_user = super(MyRegistrationView, self).register(form_class)
        tipo_usuario = form_class.cleaned_data['tipo_usuario']
        fist_name = form_class.cleaned_data['fist_name']
        apellido1 = form_class.cleaned_data['apellido1']
        apellido2 = form_class.cleaned_data['apellido2']
        rut = form_class.cleaned_data['rut']
        telefono = form_class.cleaned_data['telefono']
        colegio = form_class.cleaned_data['colegio']
        curso = form_class.cleaned_data['curso']
        foto = form_class.cleaned_data['foto']
        new_profile = Profile.objects.create(user=new_user,tipo_usuario=tipo_usuario,fist_name=fist_name,apellido1=apellido1,apellido2=apellido2,rut=rut,telefono=telefono,colegio=colegio,curso=curso,foto=foto)
        new_profile.save()
        return new_user
