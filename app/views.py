from flask import Blueprint, jsonify, render_template, redirect, url_for, request, flash
from flask.views import MethodView
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Ticket
from database import db 


router = Blueprint('main', __name__)

@router.route('/')
def index():
    return render_template('app/index.html')

class RegisterView(MethodView):
    def get(self):
        return render_template("app/register.html")
    
    def post(self):
        username = request.form['username']
        password1 = request.form['password1']
        password2 = request.form['password2']
        role = request.form['role']
        group = request.form['group']
        
        check_username = User.query.filter_by(username=username).first()
        print(check_username)
        if check_username:
            flash('Username is already taken')
            return redirect(url_for('main.register_user'))
        
        if role == 'admin':
            group = 'all'
        
        if password1 == password2:
            user = User(username=username, role=role, group=group)
            user.set_password(password=password1)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash("Passwords didn`t match")
            return redirect(url_for('main.register_user'))
        

class LoginView(MethodView):
    def get(self):
        return render_template('app/login.html')

    def post(self):
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password=password):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('main.login_user'))
        
class LogoutView(MethodView):
    decorators = [login_required]

    def get(self):
        logout_user()
        return redirect(url_for('main.login_user'))
        
    
class DashboardView(MethodView):
    decorators = [login_required]
    def get(self):
        if current_user.role == 'admin':
            tickets = Ticket.query.all()
        elif current_user.role == 'manager' or current_user.role == 'analyst':
            tickets = Ticket.query.filter_by(group=current_user.group)
        return render_template('app/dashboard.html',
                               tickets=tickets,
                               user=current_user,
                               admin_temp='app/admin_dashboard.html',
                               manager_temp='app/manager_dashboard.html', 
                               analyst_temp='app/analyst_dashboard.html',
                               ticket_dashboard='app/ticket_dashboard.html')
    

class TicketView(MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('app/create_ticket.html')
    
    def post(self):
        note = request.form['note']
        group = request.form['group']
        
        ticket = Ticket(status="pending", group=group, note=note)
        db.session.add(ticket)
        db.session.commit()

        flash('Ticket created successfully!')
        return render_template('app/create_ticket.html')
    
    
    
    
@router.route('/ticket/<string:ticket_id>')       
def ticket_details(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    return render_template('app/ticket_details.html', ticket=ticket, user=current_user)   

@router.route('/ticket/delete/<string:ticket_id>', methods=['POST'])
def delete_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    db.session.delete(ticket)
    db.session.commit()
    flash('Ticket deleted successfully!')
    return redirect('/dashboard')

@router.route('/ticket/update/<string:ticket_id>', methods=['POST'])
def update_ticket(ticket_id):
    status = request.form['status']
    group = request.form['group']
        
    ticket = Ticket.query.get_or_404(ticket_id)
    ticket.status = status
    ticket.group = group
    db.session.commit()
    return render_template('app/ticket_details.html', ticket=ticket, user=current_user)   