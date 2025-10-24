"""
Greene Genie Chatbot - Your Personal Assistant
"""
import tkinter as tk
from tkinter import Canvas, Entry, Text, Scrollbar, Frame, Label
import math
import sys
import os
import winsound
import threading
from datetime import datetime
from PIL import Image, ImageTk

class RoundedEntry(tk.Canvas):
    """Custom rounded entry widget"""
    def __init__(self, parent, **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self.configure(highlightthickness=0, bg='white')
        
        # Create rounded rectangle background
        self.create_rounded_rectangle(1, 1, kwargs.get('width', 250)-1, 
                                     kwargs.get('height', 45)-1, 
                                     radius=22, fill='white', outline='#D0D0D0', width=1)
        
        # Create entry widget on top
        self.entry = tk.Entry(self, font=('Segoe UI', 11), relief=tk.FLAT,
                             bg='white', fg='#333333', bd=0)
        self.create_window(15, kwargs.get('height', 45)//2, 
                          anchor='w', window=self.entry, 
                          width=kwargs.get('width', 250)-30)
    
    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [
            x1+radius, y1,
            x2-radius, y1,
            x2, y1,
            x2, y1+radius,
            x2, y2-radius,
            x2, y2,
            x2-radius, y2,
            x1+radius, y2,
            x1, y2,
            x1, y2-radius,
            x1, y1+radius,
            x1, y1
        ]
        return self.create_polygon(points, **kwargs, smooth=True)

class GreeneGenieChat:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Greene Genie Chat")
        
        # Make window borderless
        self.root.attributes('-topmost', True)
        self.root.overrideredirect(True)
        
        # Window size - 15% wider with header
        self.window_width = 357
        self.window_height = 470
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Position at bottom right
        x_position = screen_width - self.window_width - 15
        y_position = screen_height - self.window_height - 60
        
        self.root.geometry(f'{self.window_width}x{self.window_height}+{x_position}+{y_position}')
        
        # Colors
        self.dark_green = '#005640'
        self.gold = '#C4975C'
        self.light_green = '#00684d'
        
        # Main container with white background
        self.main_frame = tk.Frame(self.root, bg='white')
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Build interface
        self.create_header()
        self.create_welcome_screen()
        self.create_modern_input_area()
        
        # Play notification sound
        self.play_notification_sound()
        
        # Slide in animation
        self.animate_entrance()
        
        # Chat started flag
        self.chat_started = False
    
    def play_notification_sound(self):
        """Play WhatsApp-style notification sound"""
        def play_sound():
            try:
                winsound.Beep(800, 100)
                winsound.Beep(1000, 150)
            except:
                pass
        
        threading.Thread(target=play_sound, daemon=True).start()
    
    def create_header(self):
        """Create dark green header with branding and logos"""
        header = tk.Frame(self.main_frame, bg=self.dark_green, height=65)
        header.pack(fill=tk.X, side=tk.TOP)
        header.pack_propagate(False)
        
        # Left logo - Greene Genie
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            logo_path = os.path.join(script_dir, "GK Logo.png")
            
            left_logo = Image.open(logo_path)
            left_logo = left_logo.resize((45, 45), Image.Resampling.LANCZOS)
            self.left_logo_photo = ImageTk.PhotoImage(left_logo)
            
            left_label = tk.Label(header, image=self.left_logo_photo, bg=self.dark_green)
            left_label.pack(side=tk.LEFT, padx=10, pady=10)
        except:
            pass
        
        # Title in center
        title_label = tk.Label(header, 
                              text="Greene Genie Chat",
                              font=('Segoe UI', 12, 'bold'),
                              fg='white',
                              bg=self.dark_green)
        title_label.pack(side=tk.LEFT, padx=5)
        
        # Close button in header
        close_btn = tk.Button(header, text="×", command=self.close_app,
                             bg=self.dark_green, fg='white', 
                             font=('Arial', 18, 'bold'),
                             borderwidth=0, cursor='hand2',
                             relief=tk.FLAT, 
                             activebackground=self.light_green,
                             width=2, height=1)
        close_btn.pack(side=tk.RIGHT, padx=5)
    
    def create_welcome_screen(self):
        """Create welcome screen with centered content"""
        self.content_frame = tk.Frame(self.main_frame, bg='white')
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Main content - centered
        content_container = tk.Frame(self.content_frame, bg='white')
        content_container.pack(expand=True, fill=tk.BOTH)
        
        # Centered text
        text_container = tk.Frame(content_container, bg='white')
        text_container.place(relx=0.5, rely=0.48, anchor='center')
        
        # Main heading
        heading = tk.Label(text_container,
                          text="Ask Greene Genie a question...",
                          font=('Segoe UI', 17, 'bold'),
                          fg='#2C3E50',
                          bg='white')
        heading.pack(pady=(0, 15))
        
        # Description
        description = tk.Label(text_container,
                              text="Greene Genie is an AI-powered assistant, here to help you\nquickly find the information you need and connect you with\nthe right department.",
                              font=('Segoe UI', 9),
                              fg='#5A6C7D',
                              bg='white',
                              justify='center')
        description.pack()
    
    def create_modern_input_area(self):
        """Create input area matching screenshot"""
        input_container = tk.Frame(self.main_frame, bg='white', height=75)
        input_container.pack(fill=tk.X, side=tk.BOTTOM)
        input_container.pack_propagate(False)
        
        # Inner frame
        input_frame = tk.Frame(input_container, bg='white')
        input_frame.pack(fill=tk.X, padx=15, pady=15)
        
        # Rounded input field
        self.input_canvas = RoundedEntry(input_frame, width=207, height=46)
        self.input_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.message_input = self.input_canvas.entry
        self.message_input.insert(0, "Type your message here...")
        self.message_input.config(fg='#999999')
        self.message_input.bind('<FocusIn>', self.clear_placeholder)
        self.message_input.bind('<FocusOut>', self.add_placeholder)
        self.message_input.bind('<Return>', lambda e: self.start_chat())
        
        # Send button - oval/rounded black button
        send_btn = tk.Button(input_frame, text="Send",
                            command=self.start_chat,
                            bg='#000000', fg='white',
                            font=('Segoe UI', 10, 'bold'),
                            relief=tk.FLAT,
                            cursor='hand2',
                            activebackground='#333333',
                            borderwidth=0,
                            padx=20, pady=12)
        send_btn.pack(side=tk.RIGHT, padx=(10, 0))
        
        self.send_btn = send_btn
    
    def clear_placeholder(self, event):
        if self.message_input.get() == "Type your message here...":
            self.message_input.delete(0, tk.END)
            self.message_input.config(fg='#333333')
    
    def add_placeholder(self, event):
        if not self.message_input.get():
            self.message_input.insert(0, "Type your message here...")
            self.message_input.config(fg='#999999')
    
    def start_chat(self):
        message = self.message_input.get()
        
        if message and message != "Type your message here...":
            if not self.chat_started:
                self.chat_started = True
                self.transition_to_chat(message)
    
    def transition_to_chat(self, first_message):
        self.content_frame.destroy()
        self.create_chat_area()
        
        self.add_bot_message("Hello! I'm Greene Genie 👋")
        self.root.after(600, lambda: self.add_bot_message("How can I help you today?"))
        self.root.after(1200, lambda: self.add_user_message(first_message))
        self.root.after(2000, lambda: self.generate_bot_response(first_message))
        
        self.send_btn.config(command=self.send_message)
    
    def create_chat_area(self):
        self.content_frame = tk.Frame(self.main_frame, bg='#F5F5F5')
        self.content_frame.pack(fill=tk.BOTH, expand=True, before=self.main_frame.winfo_children()[-1])
        
        scrollbar = Scrollbar(self.content_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.chat_display = Text(self.content_frame, 
                                wrap=tk.WORD,
                                bg='#F5F5F5',
                                font=('Segoe UI', 9),
                                relief=tk.FLAT,
                                padx=10,
                                pady=10,
                                spacing3=8,
                                state=tk.DISABLED,
                                yscrollcommand=scrollbar.set)
        self.chat_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.chat_display.yview)
        
        self.chat_display.tag_config('bot_bubble', 
                                     background='white',
                                     foreground='#333333',
                                     lmargin1=6,
                                     lmargin2=6,
                                     rmargin=60,
                                     spacing1=4,
                                     spacing3=4,
                                     relief=tk.SOLID,
                                     borderwidth=1)
        
        self.chat_display.tag_config('user_bubble',
                                     background=self.dark_green,
                                     foreground='white',
                                     lmargin1=60,
                                     lmargin2=60,
                                     rmargin=6,
                                     spacing1=4,
                                     spacing3=4,
                                     relief=tk.SOLID,
                                     borderwidth=0)
        
        self.chat_display.tag_config('timestamp',
                                     foreground='#999999',
                                     font=('Segoe UI', 7))
    
    def send_message(self):
        message = self.message_input.get()
        
        if message and message != "Type your message here...":
            self.add_user_message(message)
            self.message_input.delete(0, tk.END)
            self.root.after(1000, lambda: self.generate_bot_response(message))
    
    def add_bot_message(self, message):
        self.chat_display.config(state=tk.NORMAL)
        timestamp = datetime.now().strftime("%H:%M")
        self.chat_display.insert(tk.END, f"\n{message}\n", 'bot_bubble')
        self.chat_display.insert(tk.END, f"{timestamp}\n", 'timestamp')
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def add_user_message(self, message):
        self.chat_display.config(state=tk.NORMAL)
        timestamp = datetime.now().strftime("%H:%M")
        self.chat_display.insert(tk.END, f"\n{message}\n", 'user_bubble')
        self.chat_display.insert(tk.END, f"{timestamp}\n", 'timestamp')
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def generate_bot_response(self, user_message):
        user_msg_lower = user_message.lower()
        
        if any(word in user_msg_lower for word in ['hello', 'hi', 'hey']):
            response = "Hello! How can I assist you today? 😊"
        elif any(word in user_msg_lower for word in ['help', 'assist']):
            response = "I'm here to help! I can assist with:\n• Restaurant bookings\n• Menu information\n• Special events\n• General inquiries"
        elif any(word in user_msg_lower for word in ['menu', 'food', 'drink']):
            response = "We have an excellent selection! Would you like information about our food menu or drinks? 🍽️🍺"
        elif any(word in user_msg_lower for word in ['booking', 'reserve', 'table']):
            response = "I'd be happy to help with a reservation! What date and time work best for you? 📅"
        elif any(word in user_msg_lower for word in ['thanks', 'thank you']):
            response = "You're welcome! Is there anything else I can help you with? 😊"
        elif any(word in user_msg_lower for word in ['bye', 'goodbye']):
            response = "Goodbye! Have a wonderful day! Come back anytime! 👋"
        else:
            response = "That's a great question! Let me help you with that. Could you provide more details? 🤔"
        
        self.add_bot_message(response)
    
    def animate_entrance(self):
        self.animation_step = 0
        self.max_steps = 20
        self.slide_in()
    
    def slide_in(self):
        if self.animation_step < self.max_steps:
            progress = self.animation_step / self.max_steps
            eased = 1 - (1 - progress) ** 3
            
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            
            start_x = screen_width
            end_x = screen_width - self.window_width - 15
            
            current_x = int(start_x - (start_x - end_x) * eased)
            y_position = screen_height - self.window_height - 60
            
            self.root.geometry(f'{self.window_width}x{self.window_height}+{current_x}+{y_position}')
            
            self.animation_step += 1
            self.root.after(15, self.slide_in)
    
    def close_app(self):
        self.root.destroy()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    chatbot = GreeneGenieChat()
    chatbot.run()