
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

hours = []
for i in range(16):
    hours_row = []
    for i in range(7):
        hours_row.append("0")
    hours.append(hours_row)
    
days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']   

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html', hours=hours)

@app.route('/calendar/<user_name> <user_last_name>')
def calendar_users(user_name, user_last_name):
    return render_template('calendar_users.html', hours=hours, name= user_name, last_name= user_last_name)



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
    user_name = request.form['name']
    user_last_name = request.form['last_name']
    print('yeeeeeeeeee', user_name, user_last_name)
    
    if hours[int(time)][int(day)] == "0":
        hours[int(time)][int(day)] = user_name + ' ' + user_last_name
        
        #return 'Has reservado la pista de tenis de Montesol para el  ' + days[int(day)] + ' de ' + str(int(time)+ 7) + ' a ' + str(int(time) + 8) 

    return redirect(url_for('calendar_users', user_name = user_name, user_last_name = user_last_name))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        
        user_name = request.form['users_name'] 
        user_last_name = request.form['surname']
        
        print(user_name)
        print(user_last_name)
        
        return redirect(url_for('calendar_users', user_name = user_name, user_last_name = user_last_name))
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')