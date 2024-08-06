from app import create_app, db, create_admin_user, AdminData

app = create_app()
with app.app_context():
    db.create_all()
    # Create an admin user
    if not AdminData.query.filter_by(username='admin').first():
        create_admin_user('suryansh', 'sharma')
        print("Admin user created.")
    else:
        print("Admin user already exists.")
