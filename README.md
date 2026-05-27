# Bangla Agricultural Advisor Chatbot using Streamlit (Without API)

A Bangla Agricultural Advisor Chatbot built using Streamlit to help Bangladeshi farmers with farming tips, fertilizer recommendations, plant disease solutions, and agricultural information. The chatbot works completely offline without using external APIs.

---

## Features

- Bangla NLP-based chatbot
- Farming tips and disease control guidance
- TF-IDF based smart search
- Bangla Speech-to-Text support
- Offline dataset-based response system
- Simple and user-friendly Streamlit interface

---

## Project Structure

```bash
bangla_agriculture_chatbot/
│── data/
│   └── agriculture_data.csv
│── app.py
│── requirements.txt
│── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/mahjabinoyshi/bangla-agriculture-chatbot.git
cd bangla-agriculture-chatbot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## Dataset Format

The chatbot uses a CSV file containing agricultural questions and answers in Bangla.

Example:

| Category | Question (Bangla) | Answer (Bangla) |
|---|---|---|
| Crop Advice | ধান চাষের জন্য উপযুক্ত সার কোনটি? | ধান চাষের জন্য ইউরিয়া, টি এস পি ও এমওপি ব্যবহার করুন। |
| Disease Control | গমের পাতায় হলুদ দাগ পড়লে কি করবো? | এটি পাতার মরিচা রোগ হতে পারে, প্রোপিকোনাজল স্প্রে করুন। |
| Government Scheme | কৃষকদের জন্য কি সরকারি স্কিম আছে? | বর্তমানে কৃষক সহায়তা প্রকল্প চালু রয়েছে। |

---

## User Interface

- Ask questions in Bangla
- Get instant responses from the dataset
- Use Speech-to-Text for voice queries
- Future support for image-based disease detection

---

## Future Enhancements

- Deep Learning-based Question Answering
- Image-based Plant Disease Detection
- Voice-based Query Support

---

## License

This project is open-source under the MIT License.
Contributions are welcome.
