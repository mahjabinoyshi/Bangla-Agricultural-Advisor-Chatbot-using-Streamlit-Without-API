# Bangla-Agricultural-Advisor-Chatbot-using-Streamlit-Without-API
🌾 Bangla Agricultural Advisor Chatbot (Without API)
This project is a Bangla Agricultural Advisor Chatbot built using Streamlit. It helps Bangladeshi farmers by providing farming tips, plant disease solutions, fertilizer recommendations, and information on government schemes. The chatbot works offline without relying on any external APIs.

🚀 Features
✅ Bangla NLP Chatbot – Provides answers to agricultural questions
✅ Farming Tips & Disease Control – Offers guidance on farming techniques and plant disease prevention
✅ Smart Search (TF-IDF) – Uses AI-based text similarity for better responses
✅ Bangla Speech-to-Text – Allows farmers to ask questions by speaking
✅ Offline Dataset-Based Approach – No API is needed for responses
✅ Simple Streamlit UI – User-friendly interface for farmers

📂 Project Structure
📁 bangla_agriculture_chatbot/
│-- 📂 data/
│   ├── agriculture_data.csv  # Contains agricultural questions & answers
│-- 📄 app.py                 # Main Streamlit chatbot app
│-- 📄 requirements.txt       # Required Python libraries
│-- 📄 README.md              # Project documentation
🔧 Installation
1️⃣ Clone the repository
  git clone https://github.com/yourusername/bangla-agriculture-chatbot.git
  cd bangla-agriculture-chatbot
2️⃣ Install dependencies
  pip install -r requirements.txt
3️⃣ Run the chatbot
  streamlit run app.py
📊 Dataset Format
The chatbot uses a CSV file containing agricultural questions and answers in Bangla.

Example format (data/agriculture_data.csv):

Category	Question (Bangla)	Answer (Bangla)
Crop Advice	ধান চাষের জন্য উপযুক্ত সার কোনটি?	ধান চাষের জন্য ইউরিয়া, টি এস পি ও এমওপি ব্যবহার করুন।
Disease Control	গমের পাতায় হলুদ দাগ পড়লে কি করবো?	এটি পাতার মরিচা রোগ হতে পারে, প্রোপিকোনাজল স্প্রে করুন।
Government Scheme	কৃষকদের জন্য কি সরকারি স্কিম আছে?	বর্তমানে "কৃষক সহায়তা প্রকল্প" চালু রয়েছে। বিস্তারিত জানার জন্য স্থানীয় কৃষি অফিসে যোগাযোগ করুন।
🎨 User Interface
1️⃣ Enter a question in Bangla
2️⃣ Get instant answers based on the dataset
3️⃣ Use Speech-to-Text for voice queries
4️⃣ Upload an image (for future plant disease detection)

🔥 Future Enhancements
✅ Deep Learning-based Question Answering
✅ Image-Based Disease Detection
✅ Voice-Based Query for Easy Use

📜 License
This project is open-source under the MIT License. Feel free to contribute!
