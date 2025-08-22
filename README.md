# 🔍 Multi-Image Component Matching using SIFT + FLANN  

<p align="center">
  <img src="https://img.shields.io/badge/OpenCV-Feature_Matching-blue?style=for-the-badge&logo=opencv" />
  <img src="https://img.shields.io/badge/Python-3.9+-yellow?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Status-Experimental-green?style=for-the-badge" />
</p>

---

## 🚀 Overview  

This project demonstrates **component matching across multiple images** using OpenCV’s SIFT + FLANN feature matching.  
We implemented different strategies:  

- 🟢 **Brute Force Matching**  
- 🔵 **KNN Brute Force Matching**  
- 🟣 **FLANN Matching**  
- 🔥 **Multi-Image Comparison with Component Registry**  

---

## 📌 Results  

### 1️⃣ Using `bruthForce()`
<img width="1230" height="670" src="https://github.com/user-attachments/assets/9cc2f31e-b563-4ecf-8039-2c14fddf89fe" />

---

### 2️⃣ Using `knnBruteForce()`
<img width="1207" height="513" src="https://github.com/user-attachments/assets/46ad41ab-d1ff-4214-b0d6-eabbe3313219" />

---

### 3️⃣ Using `FLANN()`
<img width="1204" height="509" src="https://github.com/user-attachments/assets/6dc863aa-3136-4379-9817-0547754fb85d" />

---

### 4️⃣ Multi-Image Comparison (SIFT + FLANN)  
📌 Compare **img1, img2, img3, img4, img5**  

<img width="986" height="414" src="https://github.com/user-attachments/assets/d5c46bc0-71e7-4ca3-81a2-c02368d1b2ce" />  
<img width="667" height="273" src="https://github.com/user-attachments/assets/27e75bc0-ed09-4526-8f4d-e4900f3dc471" />

---

## 🧩 Component Registry  

**Steps Implemented:**  
✅ Step 1 → Compare every image pair  
✅ Step 2 → Build a registry (dictionary) of “unique components”  
✅ Step 3 → Record in which images each component appears  
✅ Step 4 → Generate final structured output  

🔽 Sample Outputs  

<img width="1043" height="450" src="https://github.com/user-attachments/assets/423850a9-fa58-4190-a028-1ae5a2db65c3" />  
<img width="1038" height="443" src="https://github.com/user-attachments/assets/2ab64585-4ef0-459c-ae34-448a94920d5a" />  
<img width="1035" height="444" src="https://github.com/user-attachments/assets/213e784d-b369-4753-9779-0f735536d86a" />  
<img width="1039" height="442" src="https://github.com/user-attachments/assets/ee21aec8-7c73-45b5-a7dc-d49ea75553e1" />  
<img width="1042" height="449" src="https://github.com/user-attachments/assets/da8a4bd2-b2b6-4559-a022-49a1712bedf9" />  
<img width="1033" height="443" src="https://github.com/user-attachments/assets/fe5274c2-179b-4076-b9b9-6bc8a6ca522e" />  
<img width="1037" height="443" src="https://github.com/user-attachments/assets/bdf708a1-40c6-48c2-ac34-4d5502a55461" />  
<img width="1041" height="449" src="https://github.com/user-attachments/assets/125cc8b8-7ba2-466f-8478-48d417804426" />  
<img width="1043" height="449" src="https://github.com/user-attachments/assets/4f2567c0-2a6d-49c1-b743-e131af07ce7f" />  

---

## 📂 Example: Component Registry Output  

<img width="663" height="308" src="https://github.com/user-attachments/assets/d28c1eca-3355-4cad-92d6-2bd075c8c082" />

---

## 🌱 Sample Environmental Tests  

### Test 1
<img width="1240" height="465" src="https://github.com/user-attachments/assets/33314e98-5cd6-4284-acce-c322fc87baa6" />  
<img width="1234" height="464" src="https://github.com/user-attachments/assets/be645c99-26c2-48aa-a895-261a80dd710e" />  
<img width="1237" height="468" src="https://github.com/user-attachments/assets/1b6a439a-81f1-41cd-9cc0-77c78715d147" />

### Test 2
<img width="1239" height="464" src="https://github.com/user-attachments/assets/5986ec24-bf0f-44ff-82a9-355a4d54b5fc" />  
<img width="1207" height="510" src="https://github.com/user-attachments/assets/2d3cb660-5e59-4c42-99d6-291fc9d38350" />  
<img width="1204" height="512" src="https://github.com/user-attachments/assets/dc9d615a-c0b9-40ed-906c-9a12a4b127d8" />

### Test 3
<img width="1240" height="467" src="https://github.com/user-attachments/assets/8f7055fa-2794-45fd-a4ae-726ac17f7a51" />  
<img width="1212" height="517" src="https://github.com/user-attachments/assets/88eeb53a-247e-49d8-a1f8-aff93dc5e902" />  
<img width="1210" height="517" src="https://github.com/user-attachments/assets/61195f47-5732-480e-967d-1dbddbe121aa" />

---

