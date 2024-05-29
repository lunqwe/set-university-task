from .views import router, LoginView, RegisterView, LogoutView, DashboardView, TicketView, ticket_details

router.add_url_rule('/login', view_func=LoginView.as_view('login_user'))
router.add_url_rule('/login-submit', view_func=LoginView.as_view('submit_login'), methods=['POST'])
router.add_url_rule('/register', view_func=RegisterView.as_view('register_user'))
router.add_url_rule('/register-submit', view_func=RegisterView.as_view('submit_registration'), methods=['POST'])
router.add_url_rule('/logout', view_func=LogoutView.as_view('logout'))
router.add_url_rule("/dashboard", view_func=DashboardView.as_view('dashboard'))
router.add_url_rule('/create-ticket', view_func=TicketView.as_view('create-ticket'))
router.add_url_rule('/create-ticket-submit', view_func=TicketView.as_view('create-ticket-submit'), methods=['POST'])





