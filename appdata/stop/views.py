from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import NoteForm
# Create your views here.
from .models import Note


# class Homeview(TemplateView):
#     template_name= 'note.html'

class DeleteNode(DeleteView):
    model = Note
    form_class = NoteForm
    success_url = '/stop'
    template_name = 'delete.html'


class NodeUpadte(UpdateView):
    model = Note
    form_class = NoteForm
    success_url = '/stop'
    template_name = 'note_form.html'


class CreateNodeView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    success_url = '/stop'
    template_name = 'note_form.html'
    login_url = '/admin'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.success_url('/stop'))


class NoteListview(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'note.html'
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.note.all()


# class DetailView:
#     pass


class NoteDetailsview(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'detail.html'

# def list(request):
#     all_notes= Note.objects.all()
#     return render(request, 'note.html', {'notes': all_notes})


# def details(request, pk):
#     try:
#
#         all_note = Note.objects.get(pk=pk)
#     except Note.DoesNotExist:
#         raise Http404('Does not exist')
#     return render(request, 'detail.html', {'note': all_note})
