from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Note
from django.utils import timezone

class NoteTestCase(TestCase):
    
    def setUp(self):
        # Creamos un usuario de prueba
        self.user = User.objects.create_user(username='testuser', password='12345')
        
        # Creamos una nota de prueba asociada al usuario
        self.note = Note.objects.create(user=self.user, title="Nota de prueba", content="Contenido de la nota de prueba", creation_date=timezone.now())

    def test_creacion_nota_correcta(self):
        # Creamos una nota asociada al usuario de prueba
        note = Note.objects.create(user=self.user, title="Nueva Nota Prueba", content="Contenido Nota Prueba", creation_date=timezone.now())
        
        # Comprobamos que la nota se ha creado correctamente
        self.assertEqual(note.title, "Nueva Nota Prueba")
        self.assertEqual(note.content, "Contenido Nota Prueba")
        self.assertEqual(note.user, self.user)
    
    def test_actualizacion_nota_correcta(self):
        # Actualizamos los datos de la nota
        new_title = "Nuevo título"
        new_content = "Nuevo contenido de la nota"
        self.note.title = new_title
        self.note.content = new_content
        self.note.save()

        # Obtenemos la nota actualizada desde la base de datos
        updated_note = Note.objects.get(pk=self.note.pk)

        # Comprobamos que los datos se han actualizado correctamente
        self.assertEqual(updated_note.title, new_title)
        self.assertEqual(updated_note.content, new_content)

    def test_visualizacion_detalles_nota(self):
        # Iniciamos sesión como el usuario de prueba
        self.client.login(username='testuser', password='12345')

        # Realizamos una solicitud GET al detalle de la nota
        response = self.client.get(reverse('mynotes:note_detail', kwargs={'pk': self.note.pk}))

        # Verificamos que la solicitud haya sido exitosa (código 200)
        self.assertEqual(response.status_code, 200)

        # Verificamos que la nota se muestre correctamente en el contexto de la respuesta
        self.assertContains(response, self.note.title)
        self.assertContains(response, self.note.content)
    
    def test_eliminacion_nota(self):
        # Iniciamos sesión como el usuario de prueba
        self.client.login(username='testuser', password='12345')

        # Realizamos una solicitud POST para eliminar la nota
        response = self.client.post(reverse('mynotes:note_delete', kwargs={'pk': self.note.pk}))

        # Verificamos que la nota haya sido eliminada correctamente (código 302 - redirección)
        self.assertEqual(response.status_code, 302)

        # Intentamos obtener la nota desde la base de datos para verificar que ha sido eliminada
        with self.assertRaises(Note.DoesNotExist):
            Note.objects.get(pk=self.note.pk)

    def test_carga_lista_notas(self):
        # Iniciamos sesión como el usuario de prueba
        self.client.login(username='testuser', password='12345')

        # Realizamos una solicitud GET a la lista de notas
        response = self.client.get(reverse('mynotes:note_list'))

        # Verificamos que la solicitud haya sido exitosa (código 200)
        self.assertEqual(response.status_code, 200)

        # Verificamos que todas las notas del usuario estén presentes en el contexto de la respuesta
        self.assertContains(response, self.note1.title)