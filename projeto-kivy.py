import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class NoteApp(BoxLayout):
    def __init__(self, **kwargs):
        super(NoteApp, self).__init__(**kwargs)
        self.orientation = 'horizontal'

        # Pasta para armazenar notas
        self.notes_folder = "notas"
        if not os.path.exists(self.notes_folder):
            os.makedirs(self.notes_folder)

        # Layout da lista de notas (lado esquerdo)
        self.notes_list = BoxLayout(orientation='vertical', size_hint=(0.3, 1))
        self.add_widget(self.notes_list)

        # Botão para carregar as notas
        self.load_notes_button = Button(text="Notas", size_hint_y=None, height=50)
        self.notes_list.add_widget(self.load_notes_button)

        # Scroll para exibir as notas
        self.notes_scroll = ScrollView(size_hint=(1, 1))
        self.notes_grid = GridLayout(cols=1, size_hint_y=None)
        self.notes_grid.bind(minimum_height=self.notes_grid.setter('height'))
        self.notes_scroll.add_widget(self.notes_grid)
        self.notes_list.add_widget(self.notes_scroll)

        # Layout principal da nota (lado direito)
        self.note_editor = BoxLayout(orientation='vertical', size_hint=(0.7, 1))
        self.add_widget(self.note_editor)



        # Campo para o título da nota
        self.note_title = TextInput(hint_text="Título da Nota", font_size=20, size_hint_y=None, height=50)
        self.note_editor.add_widget(self.note_title)

        # Campo para o conteúdo da nota
        self.note_content = TextInput(hint_text="Conteúdo da Nota", font_size=16, multiline=True)
        self.note_editor.add_widget(self.note_content)

        # Botões: Nova Nota, Salvar e Excluir
        self.buttons_layout = BoxLayout(size_hint_y=None, height=50)
        
        # Botão Nova Nota
        self.new_note_button = Button(text="Nova Nota")
        self.new_note_button.bind(on_press=self.new_note)
        self.buttons_layout.add_widget(self.new_note_button)
        
        # Botão Salvar
        self.save_button = Button(text="Salvar")
        self.save_button.bind(on_press=self.save_note)
        self.buttons_layout.add_widget(self.save_button)
        
        # Botão Excluir
        self.delete_button = Button(text="Excluir")
        self.delete_button.bind(on_press=self.delete_note)
        self.buttons_layout.add_widget(self.delete_button)

        self.note_editor.add_widget(self.buttons_layout)

        self.current_note_file = None  # Armazena o arquivo da nota em edição

        # Carrega as notas automaticamente
        self.load_notes()

    def load_notes(self):
        # Limpa a lista de notas
        self.notes_grid.clear_widgets()

        # Carrega os arquivos de notas
        for note_file in os.listdir(self.notes_folder):
            if note_file.endswith('.txt'):
                button = Button(
                    text=note_file.replace('.txt', ''),
                    size_hint_y=None,
                    height=40
                )
                button.bind(on_press=self.load_note)
                self.notes_grid.add_widget(button)

    def load_note(self, instance):
        # Carrega uma nota selecionada
        note_file = instance.text + ".txt"
        note_path = os.path.join(self.notes_folder, note_file)

        with open(note_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Atualiza os campos de edição
        self.note_title.text = instance.text
        self.note_content.text = content
        self.current_note_file = note_path

    def save_note(self, instance):
        # Salva ou atualiza a nota
        title = self.note_title.text.strip()
        content = self.note_content.text.strip()

        if not title:
            return  # Não salva se o título estiver vazio

        note_path = os.path.join(self.notes_folder, title + ".txt")

        with open(note_path, 'w', encoding='utf-8') as file:
            file.write(content)

        self.current_note_file = note_path
        self.load_notes()  # Atualiza a lista de notas

    def delete_note(self, instance):
        # Exclui a nota atual
        if self.current_note_file and os.path.exists(self.current_note_file):
            os.remove(self.current_note_file)

        # Limpa os campos
        self.note_title.text = ''
        self.note_content.text = ''
        self.current_note_file = None
        self.load_notes()  # Atualiza a lista de notas

    def new_note(self, instance):
        # Cria uma nova nota (limpa os campos)
        self.note_title.text = ''
        self.note_content.text = ''
        self.current_note_file = None


class NotebookApp(App):
    def build(self):
        return NoteApp()


if __name__ == '__main__':
    NotebookApp().run()
