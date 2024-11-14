
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

hours = []
for i in range(16):
    hours_row = []
    for i in range(7):
        hours_row.append("0")
    hours.append(hours_row)
    
hours[5][6] = "Andreu Folch"
@app.route('/')
def home():
    return '<h1>¡Bienvenidos Montesoleros!</h1>\n esta es la web de reserva de la pista de tenis'

@app.route('/calendar')
def calendar():
    return render_template('calendar.html', hours=hours)
# Input thorugh URL example
@app.route('/<name>')
def user(name):
    return f'Hello {name}!'

# Redirection example
@app.route('/admin')
def admin():
    return redirect(url_for('user', name='Admin!'))

# Booking route
@app.route('/book', methods=['POST'])
def book():
    # Get the day and time from the form
    day = request.form['day']
    time = request.form['time']
    
    if hours[int(time)][int(day)] == "0":
        hours[int(time)][int(day)] = "Andreu Folch"
        return 'You have booked the tennis court for the day ' + day + ' at ' + time
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')