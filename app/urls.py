from .views import main, LoginView, RegisterView, LogoutView, DashboardView, TicketView

main.add_url_rule('/', view_func=LoginView.as_view('login_user'))
main.add_url_rule('/login', view_func=LoginView.as_view('submit_login'), methods=['POST'])
main.add_url_rule('/register', view_func=RegisterView.as_view('register_user'))
main.add_url_rule('/register-submit', view_func=RegisterView.as_view('submit_registration'), methods=['POST'])
main.add_url_rule('/logout', view_func=LogoutView.as_view('logout'))
main.add_url_rule("/dashboard", view_func=DashboardView.as_view('dashboard'))
main.add_url_rule('/create-ticket', view_func=TicketView.as_view('create-ticket'))
main.add_url_rule('/create-ticket-submit', view_func=TicketView.as_view('create-ticket-submit'), methods=['POST'])


