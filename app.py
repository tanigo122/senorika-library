from flask import Flask, render_template, request

app = Flask(__name__)

books = [
    {"title": "1984", "description": "Дистопия Оруэлла", "image": "https://picsum.photos/id/101/300/400"},
    {"title": "JavaScript для чайников", "description": "Учебник по JS", "image": "https://picsum.photos/id/102/300/400"},
    {"title": "Акунин: Азазель", "description": "Детектив", "image": "https://picsum.photos/id/103/300/400"},
    {"title": "Python и машинное обучение", "description": "Нейросети и data science", "image": "https://picsum.photos/id/104/300/400"},
    # ... добавь сюда ещё
]

@app.route('/')
def home():
    q = request.args.get('q', '').lower()
    if q:
        filtered_books = [book for book in books if q in book["title"].lower()]
    else:
        filtered_books = books
    return render_template('index.html', books=filtered_books)
if __name__ == "__main__":
    app.run(debug=True)
