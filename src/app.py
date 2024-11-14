
from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "fino"

hours = []
for i in range(16):
    hours_row = []
    for i in range(7):
        hours_row.append("0")
    hours.append(hours_row)
    
days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']  
max_bookings = 5 

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Calendar route, it will be called when the user presses the calendar button in the home page and it will show the calendar with the bookings made by all users and the option to login to go to calendar/users and unlock book and cancel options
@app.route('/calendar')
def calendar():
    return render_template('calendar.html', hours=hours)

# Calendar users route, it will be called when the user logs in and it will show the calendar with the bookings made by the user (and other users) and the book and cancel buttons
@app.route('/calendar/users')
def calendar_users():
    # If the user is not logged in, it will redirect to the login page
    if 'name' not in session:
        return redirect(url_for('login'))
    else:
        return render_template('calendar_users.html', hours=hours, name= session['name'], last_name= session['last_name'], bookings_count = session['bookings_count'], max_bookings = max_bookings)


# Booking route, it will be called when the user clicks on the book button in the calendar/users page
@app.route('/book', methods=['POST'])
def book():
    # Get the day and time from the form
    day = request.form['day']
    time = request.form['time']
    user_name = session['name']
    user_last_name = session['last_name']
    
    # Save the booking into the calendar list
    hours[int(time)][int(day)] = user_name + ' ' + user_last_name
    
    # Recount the bookings made by the user
    session['bookings_count'] = sum(row.count(user_name + ' ' + user_last_name) for row in hours)
        
        #return 'Has reservado la pista de tenis de Montesol para el  ' + days[int(day)] + ' de ' + str(int(time)+ 7) + ' a ' + str(int(time) + 8) 

    return redirect(url_for('calendar_users'))

# Cancel route, it will be called when the user clicks on the cancel button in the calendar/users page
@app.route('/cancel', methods=['POST'])
def cancel():
    day = request.form['day']
    time = request.form['time']
    
    hours[int(time)][int(day)] = "0"
    
    # Recount the bookings made by the user
    session['bookings_count'] = sum(row.count(session['name'] + ' ' + session['last_name']) for row in hours)
    
    return redirect(url_for('calendar_users'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'name' in session:
        return redirect(url_for('calendar_users'))
    
    if request.method == 'POST':
        
        user_name = request.form['users_name'].replace(" ", "")
        user_last_name = request.form['surname'].replace(" ", "")
        
        session['name'] = user_name
        session['last_name'] = user_last_name
        session['user'] = user_name.lower() + user_last_name.lower()
        session['bookings_count'] = sum(row.count(user_name + ' ' + user_last_name) for row in hours)
        
        return redirect(url_for('calendar_users'))
    else:
        return render_template('login.html')
    
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('name', None)
    session.pop('last_name', None)
    session.pop('user', None)
    session.pop('bookings_count', None)
    
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')