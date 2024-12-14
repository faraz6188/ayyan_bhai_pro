# import os
# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk

# from student import Student
# from train import Train
# from face_recognition import Face_Recognition


# class Face_Recognition_System:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition System")

#         # first image
#         img1 = Image.open(r"images\2.jpeg")
#         img1= img1.resize((500,130), Image.LANCZOS)
#         self.photoimg1=ImageTk.PhotoImage(img1)
#         f_lbl = Label(self.root, image=self.photoimg1)
#         f_lbl.place(x=0, y=0, width=500, height=130)

#         # second image
#         img2 = Image.open(r"images\1.jpg")
#         img2= img2.resize((500,130), Image.LANCZOS)
#         self.photoimg2=ImageTk.PhotoImage(img2)
#         f_lbl = Label(self.root, image=self.photoimg2)
#         f_lbl.place(x=500, y=0, width=500, height=130)

#          # Third image
#         img3 = Image.open(r"images\3.jpg")
#         img3= img3.resize((560,130), Image.LANCZOS)
#         self.photoimg3=ImageTk.PhotoImage(img3)
#         f_lbl = Label(self.root, image=self.photoimg3)
#         f_lbl.place(x=1000, y=0, width=560, height=130)

#          # bg image
#         img4 = Image.open(r"images\3.jpg")
#         img4= img4.resize((1530,710), Image.LANCZOS)
#         self.photoimg4=ImageTk.PhotoImage(img4)

#         bg_img = Label(self.root, image=self.photoimg4)
#         bg_img.place(x=0, y=130, width=1530, height=710)

#         title_lbl = Label(bg_img, text = "FACE RECOGNITION ATTENDANCE SYSTEM", font=("Times New Roman", 35, "bold"), bg="White", fg="red")
#         title_lbl.place(x=0, y=0,width=1530, height=45)

#         # Student button
#         img5 = Image.open(r"images\3.jpg")
#         img5= img5.resize((220,220), Image.LANCZOS)
#         self.photoimg5=ImageTk.PhotoImage(img5)
#         b1= Button(bg_img, image=self.photoimg5, command=self.student_details,cursor="hand2")
#         b1.place(x=200, y=100, width=220, height=220)

#         b1_1= Button(bg_img, text="Student Details", command=self.student_details ,cursor="hand2" , font=("Times New Roman", 15, "bold"), bg="darkblue", fg="white")
#         b1_1.place(x=200, y=300, width=220, height=40)

#          # Detect face button
#         img6 = Image.open(r"images\3.jpg")
#         img6= img6.resize((220,220), Image.LANCZOS)
#         self.photoimg6=ImageTk.PhotoImage(img6)
#         b1= Button(bg_img, image=self.photoimg6, command=self.face_data, cursor="hand2")
#         b1.place(x=500, y=100, width=220, height=220)

#         b1_1= Button(bg_img, text="Face Detector", command=self.face_data, cursor="hand2" , font=("Times New Roman", 15, "bold"), bg="darkblue", fg="white")
#         b1_1.place(x=500, y=300, width=220, height=40)

#          # Attendance button
#         img7 = Image.open(r"images\3.jpg")
#         img7= img7.resize((220,220), Image.LANCZOS)
#         self.photoimg7=ImageTk.PhotoImage(img7)
#         b1= Button(bg_img, image=self.photoimg7,cursor="hand2")
#         b1.place(x=800, y=100, width=220, height=220)

#         b1_1= Button(bg_img, text="Attendance",cursor="hand2" , font=("Times New Roman", 15, "bold"), bg="darkblue", fg="white")
#         b1_1.place(x=800, y=300, width=220, height=40)

#          # Train face button
#         img8 = Image.open(r"images\3.jpg")
#         img8= img8.resize((220,220), Image.LANCZOS)
#         self.photoimg8=ImageTk.PhotoImage(img8)
#         b1= Button(bg_img, image=self.photoimg8, command=self.train_data, cursor="hand2")
#         b1.place(x=200, y=380, width=220, height=220)

#         b1_1= Button(bg_img, text="Train Data", command=self.train_data, cursor="hand2" , font=("Times New Roman", 15, "bold"), bg="darkblue", fg="white")
#         b1_1.place(x=200, y=580, width=220, height=40)

#         # Photos button
#         img9 = Image.open(r"images\3.jpg")
#         img9= img9.resize((220,220), Image.LANCZOS)
#         self.photoimg9=ImageTk.PhotoImage(img9)
#         b1= Button(bg_img, image=self.photoimg9, command=self.open_img, cursor="hand2")
#         b1.place(x=500, y=380, width=220, height=220)

#         b1_1= Button(bg_img, text="Photos", command=self.open_img, cursor="hand2" , font=("Times New Roman", 15, "bold"), bg="darkblue", fg="white")
#         b1_1.place(x=500, y=580, width=220, height=40)

#             #==============================Function buttons

#     def student_details(self):
#         self.new_window = Toplevel(self.root)
#         self.app= Student(self.new_window)
    
#     def train_data(self):
#         self.new_window = Toplevel(self.root)
#         self.app= Train(self.new_window)

#     def face_data(self):
#         self.new_window = Toplevel(self.root)
#         self.app= Face_Recognition(self.new_window)

#     def open_img(self):
#         os.startfile('data')

# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_Recognition_System(root)
#     root.mainloop()
import os
import streamlit as st
from PIL import Image
import subprocess
import threading

def run_app(app_name):
    """Function to run a Streamlit app using subprocess."""
    subprocess.run(["streamlit", "run", app_name])

# with st.sidebar:
#     if st.button("Home"):
#         st.write("Launching Home Page ...")
#     # Start a new thread to run App 1
#         threading.Thread(target=run_app, args=("quiz.py",)).start()

#     if st.button("Materials"):
#         st.write("Launching SQL Materials ...")
#     # Start a new thread to run App 1
#         threading.Thread(target=run_app, args=("material.py",)).start()  


# Import your modules for student, train, and face recognition
# from student import Student
# from train import Train
# from face_recognition import Face_Recognition

# Helper Function to Load Images
def load_image(image_path, size):
    image = Image.open(image_path)
    image = image.resize(size)
    return image

# ------------------------------ Streamlit Page Setup -------------------------------
st.set_page_config(page_title="Face Recognition System", layout="wide")

# Title
st.markdown(
    "<h1 style='text-align: center; color: red;'>Face Recognition Attendance System</h1>",
    unsafe_allow_html=True
)

# ----------------------------- Image Section --------------------------------------
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.image(load_image("images/2.jpeg", (500, 130)), use_column_width=True)
with col2:
    st.image(load_image("images/1.jpg", (500, 130)), use_column_width=True)
with col3:
    st.image(load_image("images/3.jpg", (500, 130)), use_column_width=True)

# Background Section
st.markdown("---")

# ----------------------------- Functional Buttons ----------------------------------

# Layout for Buttons
st.markdown(
    "<h3 style='text-align: center;'>Select an Operation</h3>",
    unsafe_allow_html=True
)

# Grid for Buttons
colA, colB, colC = st.columns([1, 1, 1])
colD, colE, colF = st.columns([1, 1, 1])

# Button Definitions
with colA:
    if st.button("📚 Student Details"):
        st.success("Student Details Window Opened")
        threading.Thread(target=run_app, args=("student.py",)).start()  

        # Replace with actual functionality
        # self.new_window = Toplevel(self.root)
        # self.app = Student(self.new_window)

with colB:
    if st.button("👁 Face Detector"):
        st.success("Face Detector Window Opened")
        threading.Thread(target=run_app, args=("face_recognition.py",)).start()  

        # Replace with actual functionality
        # self.new_window = Toplevel(self.root)
        # self.app = Face_Recognition(self.new_window)

with colC:
    if st.button("📋 Attendance"):
        st.success("Attendance Window Opened")
        # Replace with actual functionality

with colD:
    if st.button("📊 Train Data"):
        st.success("Train Data Window Opened")
        threading.Thread(target=run_app, args=("train.py",)).start()  

        # Replace with actual functionality
        # self.new_window = Toplevel(self.root)
        # self.app = Train(self.new_window)

with colE:
    if st.button("🖼 Photos"):
        st.success("Opening Photos Directory")
        os.startfile('data')

with colF:
    if st.button("❌ Exit"):
        st.stop()

# ----------------------------- Footer ---------------------------------------------
st.markdown("---")
st.markdown(
    "<h5 style='text-align: center; color: gray;'>Developed with ❤️ using Streamlit</h5>",
    unsafe_allow_html=True
)
