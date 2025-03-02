from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout

# Set window size and color
Window.size = (800, 480)
Window.clearcolor = (0.98, 0.96, 0.89, 1)  # Cream background color

class BackgroundWidget(Widget):
    def __init__(self, **kwargs):
        super(BackgroundWidget, self).__init__(**kwargs)
        self.bind(size=self.update_canvas)
        self.bind(pos=self.update_canvas)
        self.update_canvas()
        
    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            # Background color
            Color(0.98, 0.96, 0.89, 1)
            Rectangle(pos=self.pos, size=self.size)
            
            # Left top blob
            Color(0.95, 0.85, 0.7, 1)  # Light beige
            Ellipse(pos=(0, self.height * 0.6), size=(self.width * 0.3, self.height * 0.8))
            
            # Bottom blob
            Color(0.95, 0.85, 0.7, 1)  # Light beige
            Ellipse(pos=(self.width * 0.1, -self.height * 0.4), size=(self.width * 0.5, self.height * 0.8))
            
            # Add small decorative elements
            Color(0.6, 0.7, 0.3, 1)  # Green for leaf
            Ellipse(pos=(self.width * 0.8, self.height * 0.7), size=(self.width * 0.1, self.height * 0.1))
            
            # Small decorative elements
            Color(0.7, 0.7, 0.7, 1)  # Gray
            for i in range(3):
                Ellipse(pos=(self.width * 0.4 + i * 10, self.height * 0.5), size=(5, 2))

# class FoodDecorationWidget(Widget):
#     def __init__(self, **kwargs):
#         super(FoodDecorationWidget, self).__init__(**kwargs)
#         self.bind(size=self.update_canvas)
#         self.bind(pos=self.update_canvas)
#         self.update_canvas()
        
#     def update_canvas(self, *args):
#         self.canvas.clear()
#         with self.canvas:
#             # Noodle bowl
#             Color(0.6, 0.4, 0.2, 1)  # Brown for bowl
#             Ellipse(pos=(self.width * 0.7, self.height * 0.6), size=(self.width * 0.25, self.height * 0.15))
            
#             Color(1, 0.7, 0.3, 1)  # Orange/yellow for noodles
#             Ellipse(pos=(self.width * 0.72, self.height * 0.62), size=(self.width * 0.21, self.height * 0.12))
            
#             # Small green bits for veggies in noodles
#             Color(0.4, 0.7, 0.3, 1)  # Green
#             for i in range(5):
#                 x = self.width * (0.75 + 0.03 * (i % 3))
#                 y = self.height * (0.64 + 0.01 * (i % 2))
#                 Ellipse(pos=(x, y), size=(5, 7))
            
#             # Orange food items (like the items in the plate in your image)
#             Color(0.6, 0.7, 0.3, 1)  # Green circle for plate
#             Ellipse(pos=(self.width * 0.65, self.height * 0.4), size=(self.width * 0.15, self.height * 0.15))
            
#             Color(1, 0.6, 0.2, 1)  # Orange for food
#             Ellipse(pos=(self.width * 0.67, self.height * 0.42), size=(self.width * 0.11, self.height * 0.11))
            
#             # Green bits on orange food
#             Color(0.4, 0.7, 0.3, 1)  # Green
#             for i in range(4):
#                 x = self.width * (0.69 + 0.03 * (i % 2))
#                 y = self.height * (0.45 + 0.01 * (i % 2))
#                 Ellipse(pos=(x, y), size=(3, 5))
            
#             # Green leaf at right bottom
#             Color(0.4, 0.7, 0.3, 1)  # Green
#             Ellipse(pos=(self.width * 0.85, self.height * 0.1), size=(self.width * 0.15, self.height * 0.2))
            
#             # Leaf details
#             Color(0.3, 0.6, 0.2, 1)  # Darker green
#             Ellipse(pos=(self.width * 0.88, self.height * 0.15), size=(self.width * 0.08, self.height * 0.02))

class GenderSelectionScreen(Screen):
    def __init__(self, **kwargs):
        super(GenderSelectionScreen, self).__init__(**kwargs)
        
        # Main layout
        main_layout = FloatLayout()
        
        # Add background
        bg = BackgroundWidget()
        main_layout.add_widget(bg)
        
        # Add food decorations
        food_decor = FoodDecorationWidget()
        main_layout.add_widget(food_decor)
        
        # Create buttons layout
        buttons_layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            size_hint=(0.4, 0.3),
            pos_hint={'center_x': 0.35, 'center_y': 0.5}
        )
        
        # Male button
        self.male_btn = Button(
            text="Male",
            font_size=24,
            background_normal="",
            background_color=(0.4, 0.7, 0.3, 0),  # Transparent
            color=(0.4, 0.7, 0.3, 1),  # Green text like in image
            size_hint_y=0.5
        )
        with self.male_btn.canvas.before:
            Color(0.95, 0.85, 0.7, 1)  # Light beige background
            self.male_rect = Rectangle(pos=self.male_btn.pos, size=self.male_btn.size)
        self.male_btn.bind(pos=self.update_male_rect, size=self.update_male_rect)
        self.male_btn.bind(on_release=lambda x: self.select_gender('male'))
        buttons_layout.add_widget(self.male_btn)
        
        # Female button
        self.female_btn = Button(
            text="Female",
            font_size=24,
            background_normal="",
            background_color=(0.4, 0.7, 0.3, 0),  # Transparent
            color=(0.4, 0.7, 0.3, 1),  # Green text like in image
            size_hint_y=0.5
        )
        with self.female_btn.canvas.before:
            Color(0.95, 0.85, 0.7, 1)  # Light beige background
            self.female_rect = Rectangle(pos=self.female_btn.pos, size=self.female_btn.size)
        self.female_btn.bind(pos=self.update_female_rect, size=self.update_female_rect)
        self.female_btn.bind(on_release=lambda x: self.select_gender('female'))
        buttons_layout.add_widget(self.female_btn)
        
        main_layout.add_widget(buttons_layout)
        self.add_widget(main_layout)
    
    def update_male_rect(self, instance, value):
        self.male_rect.pos = instance.pos
        self.male_rect.size = instance.size
    
    def update_female_rect(self, instance, value):
        self.female_rect.pos = instance.pos
        self.female_rect.size = instance.size
    
    def select_gender(self, gender):
        app = App.get_running_app()
        app.user_data['gender'] = gender
        print(f"Selected gender: {gender}")
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'age'

class AgeScreen(Screen):
    def __init__(self, **kwargs):
        super(AgeScreen, self).__init__(**kwargs)
        
        # Main layout
        main_layout = FloatLayout()
        
        # Add background
        bg = BackgroundWidget()
        main_layout.add_widget(bg)
        
        # Add food decorations
        food_decor = FoodDecorationWidget()
        main_layout.add_widget(food_decor)
        
        # Create content layout
        content = BoxLayout(
            orientation='vertical',
            spacing=20,
            size_hint=(0.6, 0.4),
            pos_hint={'center_x': 0.35, 'center_y': 0.5}
        )
        
        # Title
        title = Label(
            text="Select Your Age",
            font_size=28,
            color=(0.4, 0.7, 0.3, 1),  # Green text
            size_hint_y=0.3
        )
        content.add_widget(title)
        
        # Age slider
        self.age_slider = Slider(
            min=1,
            max=100,
            value=25,  # Default age
            step=1,
            size_hint_y=0.3
        )
        content.add_widget(self.age_slider)
        
        # Age display label
        self.age_label = Label(
            text=f"Age: {int(self.age_slider.value)}",
            font_size=24,
            color=(0.4, 0.7, 0.3, 1),  # Green text
            size_hint_y=0.2
        )
        content.add_widget(self.age_label)
        
        # Update age label when slider value changes
        self.age_slider.bind(value=self.update_age_label)
        
        # Buttons
        buttons = BoxLayout(
            orientation='horizontal',
            spacing=20,
            size_hint_y=0.2
        )
        
        back_btn = Button(
            text="Back",
            font_size=20,
            background_normal="",
            background_color=(0.95, 0.85, 0.7, 1),  # Light beige
            color=(0.4, 0.7, 0.3, 1)  # Green text
        )
        back_btn.bind(on_release=self.go_back)
        buttons.add_widget(back_btn)
        
        next_btn = Button(
            text="Next",
            font_size=20,
            background_normal="",
            background_color=(0.95, 0.85, 0.7, 1),  # Light beige
            color=(0.4, 0.7, 0.3, 1)  # Green text
        )
        next_btn.bind(on_release=self.go_next)
        buttons.add_widget(next_btn)
        
        content.add_widget(buttons)
        main_layout.add_widget(content)
        self.add_widget(main_layout)
    
    def update_age_label(self, instance, value):
        self.age_label.text = f"Age: {int(value)}"
    
    def go_back(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'gender'
    
    def go_next(self, instance):
        app = App.get_running_app()
        app.user_data['age'] = int(self.age_slider.value)
        print(f"Age entered: {int(self.age_slider.value)}")
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'weight'

class WeightScreen(Screen):
    def __init__(self, **kwargs):
        super(WeightScreen, self).__init__(**kwargs)
        
        # Main layout
        main_layout = FloatLayout()
        
        # Add background
        bg = BackgroundWidget()
        main_layout.add_widget(bg)
        
        # Add food decorations
        food_decor = FoodDecorationWidget()
        main_layout.add_widget(food_decor)
        
        # Create content layout
        content = BoxLayout(
            orientation='vertical',
            spacing=20,
            size_hint=(0.6, 0.4),
            pos_hint={'center_x': 0.35, 'center_y': 0.5}
        )
        
        # Title
        title = Label(
            text="Select Your Weight (kg)",
            font_size=28,
            color=(0.4, 0.7, 0.3, 1),  # Green text
            size_hint_y=0.3
        )
        content.add_widget(title)
        
        # Weight slider
        self.weight_slider = Slider(
            min=30,
            max=150,
            value=70,  # Default weight
            step=1,
            size_hint_y=0.3
        )
        content.add_widget(self.weight_slider)
        
        # Weight display label
        self.weight_label = Label(
            text=f"Weight: {int(self.weight_slider.value)} kg",
            font_size=24,
            color=(0.4, 0.7, 0.3, 1),  # Green text
            size_hint_y=0.2
        )
        content.add_widget(self.weight_label)
        
        # Update weight label when slider value changes
        self.weight_slider.bind(value=self.update_weight_label)
        
        # Buttons
        buttons = BoxLayout(
            orientation='horizontal',
            spacing=20,
            size_hint_y=0.2
        )
        
        back_btn = Button(
            text="Back",
            font_size=20,
            background_normal="",
            background_color=(0.95, 0.85, 0.7, 1),  # Light beige
            color=(0.4, 0.7, 0.3, 1)  # Green text
        )
        back_btn.bind(on_release=self.go_back)
        buttons.add_widget(back_btn)
        
        next_btn = Button(
            text="Next",
            font_size=20,
            background_normal="",
            background_color=(0.95, 0.85, 0.7, 1),  # Light beige
            color=(0.4, 0.7, 0.3, 1)  # Green text
        )
        next_btn.bind(on_release=self.go_next)
        buttons.add_widget(next_btn)
        
        content.add_widget(buttons)
        main_layout.add_widget(content)
        self.add_widget(main_layout)
    
    def update_weight_label(self, instance, value):
        self.weight_label.text = f"Weight: {int(value)} kg"
    
    def go_back(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'age'
    
    def go_next(self, instance):
        app = App.get_running_app()
        app.user_data['weight'] = int(self.weight_slider.value)
        print(f"Weight entered: {int(self.weight_slider.value)} kg")
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'height'

class HeightScreen(Screen):
    def __init__(self, **kwargs):
        super(HeightScreen, self).__init__(**kwargs)
        
        # Main layout
        main_layout = FloatLayout()
        
        # Add background
        bg = BackgroundWidget()
        main_layout.add_widget(bg)
        
        # Add food decorations
        food_decor = FoodDecorationWidget()
        main_layout.add_widget(food_decor)
        
        # Create content layout
        content = BoxLayout(
            orientation='vertical',
            spacing=20,
            size_hint=(0.6, 0.4),
            pos_hint={'center_x': 0.35, 'center_y': 0.5}
        )
        
        # Title
        title = Label(
            text="Select Your Height (cm)",
            font_size=28,
            color=(0.4, 0.7, 0.3, 1),  # Green text
            size_hint_y=0.3
        )
        content.add_widget(title)
        
        # Height slider
        self.height_slider = Slider(
            min=100,
            max=250,
            value=170,  # Default height
            step=1,
            size_hint_y=0.3
        )
        content.add_widget(self.height_slider)
        
        # Height display label
        self.height_label = Label(
            text=f"Height: {int(self.height_slider.value)} cm",
            font_size=24,
            color=(0.4, 0.7, 0.3, 1),  # Green text
            size_hint_y=0.2
        )
        content.add_widget(self.height_label)
        
        # Update height label when slider value changes
        self.height_slider.bind(value=self.update_height_label)
        
                # Buttons
        buttons = BoxLayout(
            orientation='horizontal',
            spacing=20,
            size_hint_y=0.2
        )
        
        back_btn = Button(
            text="Back",
            font_size=20,
            background_normal="",
            background_color=(0.95, 0.85, 0.7, 1),  # Light beige
            color=(0.4, 0.7, 0.3, 1)  # Green text
        )
        back_btn.bind(on_release=self.go_back)
        buttons.add_widget(back_btn)
        
        next_btn = Button(
            text="Next",
            font_size=20,
            background_normal="",
            background_color=(0.95, 0.85, 0.7, 1),  # Light beige
            color=(0.4, 0.7, 0.3, 1)  # Green text
        )
        next_btn.bind(on_release=self.go_next)
        buttons.add_widget(next_btn)
        
        content.add_widget(buttons)
        main_layout.add_widget(content)
        self.add_widget(main_layout)
    
    def update_height_label(self, instance, value):
        self.height_label.text = f"Height: {int(value)} cm"
    
    def go_back(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'weight'
    
    def go_next(self, instance):
        app = App.get_running_app()
        app.user_data['height'] = int(self.height_slider.value)
        print(f"Height entered: {int(self.height_slider.value)} cm")
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'summary'

class SummaryScreen(Screen):
    def __init__(self, **kwargs):
        super(SummaryScreen, self).__init__(**kwargs)
        
        # Main layout
        main_layout = FloatLayout()
        
        # Add background
        bg = BackgroundWidget()
        main_layout.add_widget(bg)
        
        # Add food decorations
        food_decor = FoodDecorationWidget()
        main_layout.add_widget(food_decor)
        
        # Create content layout
        content = BoxLayout(
            orientation='vertical',
            spacing=15,
            size_hint=(0.7, 0.6),
            pos_hint={'center_x': 0.35, 'center_y': 0.5}
        )
        
        # Title
        title = Label(
            text="Summary",
            font_size=28,
            color=(0.4, 0.7, 0.3, 1),  # Green text
            size_hint_y=0.2
        )
        content.add_widget(title)
        
        # Create summary content
        self.summary_content = BoxLayout(
            orientation='vertical',
            spacing=10,
            size_hint_y=0.6,
            padding=[20, 20, 20, 20]
        )
        
        with self.summary_content.canvas.before:
            Color(0.95, 0.85, 0.7, 1)  # Light beige background
            self.summary_rect = Rectangle(pos=self.summary_content.pos, size=self.summary_content.size)
        self.summary_content.bind(pos=self.update_rect, size=self.update_rect)
        
        # Labels will be added in the on_pre_enter method
        self.gender_label = Label()
             
        self.summary_content.add_widget(self.gender_label)
        
        self.age_label = Label(
            text="Age: ",
            font_size=20,
            color=(0.4, 0.7, 0.3, 1),  # Green text
            halign='left',
            size_hint_y=0.25,
            text_size=(400, None))
        self.summary_content.add_widget(self.age_label)
        
        self.weight_label = Label(
            text="Weight: ",
            font_size=20,
            color=(0.4, 0.7, 0.3, 1),  # Green text
            halign='left',
            size_hint_y=0.25,
            text_size=(400, None))
        self.summary_content.add_widget(self.weight_label)
        
        self.height_label = Label(
            text="Height: ",
            font_size=20,
            color=(0.4, 0.7, 0.3, 1),  # Green text
            halign='left',
            size_hint_y=0.25,
            text_size=(400, None))
        self.summary_content.add_widget(self.height_label)
        
        content.add_widget(self.summary_content)
        
        # Buttons
        buttons = BoxLayout(
            orientation='horizontal',
            spacing=20,
            size_hint_y=0.2
        )
        
        back_btn = Button(
            text="Edit Information",
            font_size=20,
            background_normal="",
            background_color=(0.95, 0.85, 0.7, 1),  # Light beige
            color=(0.4, 0.7, 0.3, 1)  # Green text
        )
        back_btn.bind(on_release=self.go_back)
        buttons.add_widget(back_btn)
        
        finish_btn = Button(
            text="Finish",
            font_size=20,
            background_normal="",
            background_color=(0.95, 0.85, 0.7, 1),  # Light beige
            color=(0.4, 0.7, 0.3, 1)  # Green text
        )
        finish_btn.bind(on_release=self.finish)
        buttons.add_widget(finish_btn)
        
        content.add_widget(buttons)

        main_layout.add_widget(content)
        self.add_widget(main_layout)
    
    def update_rect(self, instance, value):
        self.summary_rect.pos = instance.pos
        self.summary_rect.size = instance.size
    
    def on_pre_enter(self, *args):
        app = App.get_running_app()
        self.gender_label.text = f"Gender: {app.user_data.get('gender', 'Not specified').capitalize()}"
        self.age_label.text = f"Age: {app.user_data.get('age', 'Not specified')}"
        self.weight_label.text = f"Weight: {app.user_data.get('weight', 'Not specified')} kg"
        self.height_label.text = f"Height: {app.user_data.get('height', 'Not specified')} cm"
    
    def go_back(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'height'
    
    def finish(self, instance):
        app = App.get_running_app()
        print("Data collection complete!")
        print(f"Collected data: {app.user_data}")
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'gender'  # Reset to start
        
        # Reset data
        app.user_data = {}

class FoodSelectionApp(App):
    def __init__(self, **kwargs):
        super(FoodSelectionApp, self).__init__(**kwargs)
        self.user_data = {}
    
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        
        # Add screens
        sm.add_widget(GenderSelectionScreen(name='gender'))
        sm.add_widget(AgeScreen(name='age'))
        sm.add_widget(WeightScreen(name='weight'))
        sm.add_widget(HeightScreen(name='height'))
        sm.add_widget(SummaryScreen(name='summary'))
        
        return sm

if __name__ == '__main__':
    FoodSelectionApp().run()