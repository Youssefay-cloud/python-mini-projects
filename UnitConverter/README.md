# 🔄 Unit Converter (Flask Web App)

A lightweight web-based converter built with Python and Flask to seamlessly convert units of **Length** and **Weight**.

---

## 🚀 Features

* **Length Conversion:** Convert between Meters, Kilometers, Feet, Miles, Inches, and Centimeters.
* **Weight Conversion:** Convert between Kilograms, Grams, Pounds, and milligrams.
* **Fast & Minimalist:** Clean routing and instant responses powered by a lightweight Flask backend.

---

## 🛠️ Prerequisites & Installation

Ensure you have Python 3.8+ installed on your system.

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/unit-converter.git
cd unit-converter

```


2. **Create and activate a virtual environment (optional but recommended):**
* **macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate

```


* **Windows:**
```bash
python -m venv venv
venv\Scripts\activate

```




3. **Install dependencies:**
```bash
pip install Flask

```



---

## 🚦 How to Run

1. **Start the local server:**
```bash
python app.py

```


2. **Access the application:**
The server will start at `[http://127.0.0.1:5000/](http://127.0.0.1:5000/)`.

---

## 🧭 Routes & Endpoints

| Route | Description | Example URL |
| --- | --- | --- |
| `/` | Application Home / Welcome page | `[http://127.0.0.1:5000/](http://127.0.0.1:5000/)` |
| `/length` | Interactive Length Converter | `[http://127.0.0.1:5000/length](http://127.0.0.1:5000/length)` |
| `/weight` | Interactive Weight Converter | `[http://127.0.0.1:5000/weight](http://127.0.0.1:5000/weight)` |

---

## 📂 Project Structure

```text
unit-converter/
├── app.py              # Main Flask application and routing logic
├── static/             # CSS styling and static assets
│   └── style.css
├── templates/          # HTML templates
│   ├── index.html      # Landing page
│   ├── length.html     # Length conversion form
│   └── weight.html     # Weight conversion form
└── README.md           # Project documentation

```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for additional conversion units (temperature, speed, volume).
