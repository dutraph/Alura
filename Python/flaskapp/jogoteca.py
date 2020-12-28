from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.debug = True
app.secret_key= 'mestra'
class Ticket:
  def __init__(self, name, category, description, severity):
    self.name = name
    self.category = category
    self.description = description
    self.severity = severity
   
tck1 = Ticket('Application Offline', 'IT', 'The billing system application is not working', 'HIGH')
tck2 = Ticket('Keybord Broken', 'IT', 'My keyboard isn`t work properly', 'LOW')
tck3 = Ticket('Printer Offline', 'IT', 'There are no connection to the main printer', 'MEDIUM')


lista = [tck1, tck2, tck3]

@app.route('/')
def index():
  if 'usuario_logado' not in session or session['usuario_logado'] == None:
    return redirect('/login')
  return render_template('lista.html', titulo='tickets', ticket=lista)

@app.route('/novo')
def novo():
  if 'usuario_logado' not in session or session['usuario_logado'] == None:
    return redirect('/login?proxima=novo')
  return render_template('novo.html', titulo='New Ticket')

@app.route('/criar', methods=['POST', ])
def criar():
  name = request.form['name']
  category = request.form['category']
  description = request.form['description']
  severity = request.form['severity']
  tckt = Ticket(name, category, description, severity)
  lista.append(tckt)
  flash('Ticket booked successfuly')
  return redirect('/')

@app.route('/login')
def login():
  proxima = request.args.get('proxima')
  return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
  if 'mestra' == request.form['senha']:
    session['usuario_logado'] = request.form['usuario']
    flash(request.form['usuario'] + ' logou com sucesso')
    proxima_pagina = request.form['proxima']
    return redirect('/{}'.format(proxima_pagina))
  else:
    flash('Falha na autenticaçao')
    return redirect('/login')

@app.route('/logout', methods=['POST',])
def logout():
  session['usuario_logado'] = None
  flash('Deslogado com sucesso')
  return redirect('/login')

app.run(debug=True, use_debugger=False, use_reloader=False)