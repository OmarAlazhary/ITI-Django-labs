from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee
from course_app.models import Course
from .forms import  AddTraineeForm
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


courses = Course.objects.all()
class TraineeListView(ListView):
    model = Trainee
    template_name = 'trainee/trainee_list.html'
    context_object_name = 'trainees'

class TraineeDeleteView(DeleteView):
    model = Trainee
    template_name = 'trainee/trainee_confirm_delete.html'
    success_url = reverse_lazy('trainee_list')
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class AddTraineeView(View):
    template_name = 'trainee/add_trainee.html'
    
    def get(self, request):
        form = AddTraineeForm()
        return render(request, 'trainee/add_trainee.html', {'form': form, 'courses': courses})
    
    def post(self, request):
        form = AddTraineeForm(request.POST)
        if form.is_valid():
            Trainee.objects.create(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                email=form.cleaned_data['email'],
                course=Course.objects.get(id=form.cleaned_data['course'])
            )
            return redirect('trainee_list')
        return render(request, 'trainee/add_trainee.html', {'form': form, 'courses': courses})

class UpdateTraineeView(View):
    template_name = 'trainee/update_trainee.html'
    
    def get(self, request, id):
        trainee = get_object_or_404(Trainee, id=id)
        courses = Course.objects.all()
        context = {'courses': courses, 'trainee': trainee}
        return render(request, self.template_name, context)
    
    def post(self, request, id):
        trainee = get_object_or_404(Trainee, id=id)
        trainee.name = request.POST['name']
        trainee.age = request.POST['age']
        trainee.email = request.POST['email']
        trainee.course = Course.objects.get(id=request.POST['course'])
        trainee.save()
        return redirect('trainee_list')

