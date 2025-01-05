---

# **Vehicle Type Classification with MobileNetV2** 🚗🚚🏍️🚌  
This deep learning project aims to classify vehicle types based on images using the Convolutional Neural Network (CNN) approach. The main focus of this project is to evaluate the model's performance, improve accuracy, and provide recommendations for real-world applications in traffic management and road safety.

### **Introduction** 🌍  
Vehicles play a crucial role in public mobility, and accurate vehicle type recognition is essential for traffic management, such as regulating heavy vehicle lanes and monitoring traffic violations. This project develops a system to automatically classify vehicle types such as **Car**, **Truck**, **Motorcycle**, and **Bus** from images. The primary goal is to assist in smart traffic management and improve road safety.

### **Project Objectives** 🎯  
1. Build a **Convolutional Neural Network (CNN)**-based vehicle classification model to recognize vehicle types from images.  
2. The model will be used for:  
   - Reducing traffic congestion.  
   - Enhancing road safety for users.  
3. Evaluate the model's performance using accuracy and loss on the validation dataset to determine its effectiveness.

### **Dataset Overview** 📂  
The dataset used is the **Vehicle Type Recognition Dataset** from Kaggle, which contains images of vehicles in four categories: **Car**, **Truck**, **Motorcycle**, and **Bus**. The dataset includes 400 images with a relatively balanced distribution across each category (100 images per category).  
- **Dataset URL**: [Vehicle Type Recognition Dataset](https://www.kaggle.com/datasets/kaggleashwin/vehicle-type-recognition)

### **Model Performance** 🏆  
- The initial model using a simple CNN showed unsatisfactory results with an **accuracy of 59.38%** and **loss of 1.0070** on the test data.  
- After applying **MobileNetV2** as the base model and performing **data augmentation** and hyperparameter optimization, the model's performance significantly improved to **87.50% accuracy** with **loss of 0.1992**.  
- The model now classifies **Motorcycle** and **Truck** categories with high accuracy, though there are still some errors in the **Bus** and **Car** categories, likely due to visual similarities between the two categories.

### **Implementation and Deployment Readiness** 🚀  
- The model is ready for implementation and can be used for **inference**.  
- This solution is ready to be applied in **smart traffic systems** for efficient traffic monitoring and management, including the regulation of heavy vehicle lanes and quick response to traffic violations.

### **Streamlit Interface for User Interaction** 🚀  
For this project, a simple Streamlit interface has been developed to allow users to interact with the vehicle classification model in real-time. The interface provides two main sections:  
1. **Predictor Page**: Users can upload images of vehicles to classify the vehicle type based on the trained model.  
2. **EDA (Exploratory Data Analysis) Page**: Users can explore and visualize the dataset, gaining insights into the vehicle types and image distributions.

### **Recommendations** 💡  
#### For the Model:  
1. **Training Data Expansion**: Add more variations in images, such as artificial backgrounds and different vehicle poses, to improve the model’s ability to recognize patterns.  
2. **Fine-Tune MobileNetV2**: Perform additional training on the last layers of MobileNetV2 to enhance feature extraction.  
3. **Evaluation with External Datasets**: Test the model on different datasets or environments to ensure the model maintains good performance.

#### For Real-World Applications:  
1. **Traffic Management**: Use this model to automate vehicle type detection on the road, aiding in vehicle lane management and traffic violation monitoring.  
2. **Security and Surveillance Systems**: Apply it to enhance road safety by detecting vehicles that violate regulations.  
3. **Integration with Smart Systems**: This model can be integrated into smart traffic systems for analysis and optimization of vehicle flow.

### **Links** 🔗  
- **Model URL**: [View Model](https://drive.google.com/file/d/1dKua6wNV9w9--BpgKm_qfdKnlD3s-QMD/view?usp=sharing)  
- **Deployment URL**: [Hugging Face Space](https://huggingface.co/spaces/rafinadhiya/gc7)

---

## **About the Author** 👩‍💻  
**Rafina Dhiya Pradani** | 📧 [Email](mailto:rafina.pradani@gmail.com) | 🌐 [LinkedIn](https://www.linkedin.com/in/rafinadhiya/)

---

Feel free to reach out with any questions or feedback! 😊

---