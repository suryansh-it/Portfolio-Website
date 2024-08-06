# This script ensures that when the application is initialized,
# the necessary database tables are created, 
# and an initial adminuser is set up if it doesn't already exist


from app import create_app, db, create_admin_user, AdminData

# Create the Flask application instance
app = create_app()

# Enter the application context
with app.app_context():
    # Create all the database tables if they don't exist
    db.create_all()
    
    # Check if an admin user with the username 'admin' already exists
    if not AdminData.query.filter_by(username='suryansh').first():
        # If no admin user exists, create one with the specified username and password
        create_admin_user('suryansh', 'sharma')
        print("Admin user created.")
    else:
        # If an admin user already exists, print a message
        print("Admin user already exists.")

    # Create an admin user
    if not AdminData.query.filter_by(username='admin').first():
        create_admin_user('suryansh', 'sharma')
        print("Admin user created.")
    else:
        print("Admin user already exists.")
