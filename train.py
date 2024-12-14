# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2
# import os
# import numpy as np

# class Train:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition System")


#         title_lbl = Label(self.root, text="TRAIN DATA SET", font=("Times New Roman", 35, "bold"), bg="white", fg="red")
#         title_lbl.place(x=0, y=0, width=1530, height=45)

#         img_top = Image.open(r"images\3.jpg")
#         img_top = img_top.resize((1530, 325), Image.LANCZOS)
#         self.photoimg_top = ImageTk.PhotoImage(img_top)
#         f_lbl = Label(self.root, image=self.photoimg_top)
#         f_lbl.place(x=0, y=55, width=1530, height=325)

#         # button
#         b1_1= Button(self.root, text="TRAIN DATA", command=self.train_classifier,cursor="hand2" , font=("Times New Roman", 30, "bold"), bg="red", fg="white")
#         b1_1.place(x=0, y=380, width=1530, height=60)

#         img_bottom = Image.open(r"images\3.jpg")
#         img_bottom = img_top.resize((1530, 325), Image.LANCZOS)
#         self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
#         f_lbl = Label(self.root, image=self.photoimg_bottom)
#         f_lbl.place(x=0, y=440, width=1530, height=325)

#     def train_classifier(self):
#         data_dir = ("data")
#         path = [os.path.join(data_dir,file)for file in os.listdir(data_dir)]
#         faces=[]
#         ids=[]
#         for image in path:
#             img=Image.open(image).convert("L") #Gray Scale image
         
#             imageNp = np.array(img, "uint8")

#             id = int(os.path.split(image)[1].split('.')[1])

#             faces.append(imageNp)
#             ids.append(id)
#             cv2.imshow("Training", imageNp)
#             cv2.waitKey(1)==13
#         ids=np.array(ids)

         
#         # ========== Train the classifier and save ==== 
#         clf=cv2.face.LBPHFaceRecognizer_create()
#         clf.train(faces, ids)
#         clf.write("classifier.xml")
#         cv2.destroyAllwindows()
#         messagebox.showinfo("Result","Training datasets completed!!")

    

       
# if __name__ == "__main__":
#     root = Tk()
#     obj = Train(root)
#     root.mainloop()
import os
import numpy as np
import cv2
from PIL import Image
import streamlit as st
import subprocess
import threading

def run_app(app_name):
    """Function to run a Streamlit app using subprocess."""
    subprocess.run(["streamlit", "run", app_name])

with st.sidebar:
    if st.button("Home"):
        st.write("Launching Home Page ...")
    # Start a new thread to run App 1
        threading.Thread(target=run_app, args=("main.py",)).start()


# Function to train the classifier
def train_classifier(data_dir):
    try:
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []
        
        # Loading and processing images
        for image in path:
            img = Image.open(image).convert("L")  # Convert to grayscale
            imageNp = np.array(img, "uint8")      # Convert to numpy array
            
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
        
        ids = np.array(ids)

        # Train the classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        
        return True, "Training datasets completed successfully!"
    except Exception as e:
        return False, f"Error occurred: {str(e)}"

# Streamlit App
def main():
    st.set_page_config(page_title="Train Dataset", layout="wide")
    st.title("Train Dataset for Face Recognition")
    
    # Top Image
    st.image("images/3.jpg", use_column_width=True)
    
    # Instructions
    st.info(
        "Click on the **Train Data** button to train your face recognition dataset.\n\n"
        "Ensure that the **data folder** contains images in the correct format (e.g., `User.ID.jpg`)."
    )
    
    # File Path Input
    st.subheader("Step 1: Confirm Data Directory")
    data_dir = st.text_input("Enter the path to the data folder:", "data")
    
    # Train Data Button
    st.subheader("Step 2: Train Dataset")
    if st.button("Train Data", key="train_btn"):
        with st.spinner("Training the dataset... This may take a moment."):
            success, message = train_classifier(data_dir)
            if success:
                st.success(message)
                st.balloons()
            else:
                st.error(message)
    
    # Bottom Image
    st.image("images/3.jpg", use_column_width=True)

if __name__ == "__main__":
    main()
