from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import Note
from .forms import NoteForm
from django.http import HttpResponseRedirect

#Vista de todas las notas
class NoteListView(LoginRequiredMixin, generic.ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'note_list.html'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('-creation_date')

#Vista de el detalle de una nota
class NoteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Note
    template_name = 'mynotes/note_detail.html'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

#Vista de crear una nota 
class NoteCreateView(LoginRequiredMixin, generic.CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'mynotes/note_edit.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    #Al crearse la nota, abre el detalle de dicha nota
    def get_success_url(self):
        return reverse_lazy('mynotes:note_detail', kwargs={'pk': self.object.pk})

#Vista de edición de una nota
class NoteUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'mynotes/note_edit.html'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('mynotes:note_detail', kwargs={'pk': self.object.pk})

#Vista de eliminación de una nota
class NoteDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Note
    template_name = 'mynotes/note_confirm_delete.html'
    success_url = reverse_lazy('mynotes:note_list')

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
