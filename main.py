from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    services = [
        'Сервис 1', 'Сервис 2', 'Сервис 3', 'Сервис 4',
        'Сервис 5', 'Сервис 6', 'Сервис 7', 'Сервис 8'
    ]
    news = [f'Новость {i}' for i in range(1, 5)]
    return render_template('index.html', services=services, news=news)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/residents')
def residents_page():
    residents = [f'Резидент {i}' for i in range(1, 33)]

    return render_template('residents.html', residents=residents)


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/become_resident')
def become_resident():
    return render_template('become_resident.html')


@app.route('/events')
def events():
    return render_template('events.html')


@app.route('/map')
def maps():
    residents = [f'Резидент {i}' for i in range(1, 17)]
    return render_template('map.html', residents=residents)


if __name__ == '__main__':
    app.run(debug=True)
