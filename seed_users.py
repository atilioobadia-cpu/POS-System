from app import create_app, db, bcrypt
from app.models import User

app = create_app()

with app.app_context():
    # Check if users already exist
    admin_exists = User.query.filter_by(email='admin@amram.com').first()
    cashier_exists = User.query.filter_by(email='cashier@amram.com').first()
    
    if not admin_exists:
        admin = User(
            username='admin',
            email='admin@amram.com',
            password=bcrypt.generate_password_hash('amram@2025').decode('utf-8'),
            role='admin'
        )
        db.session.add(admin)
        print("✅ Admin user created: admin@amram.com")
    else:
        print("⚠️  Admin user already exists")
    
    if not cashier_exists:
        cashier = User(
            username='cashier',
            email='cashier@amram.com',
            password=bcrypt.generate_password_hash('cashier@2025').decode('utf-8'),
            role='cashier'
        )
        db.session.add(cashier)
        print("✅ Cashier user created: cashier@amram.com")
    else:
        print("⚠️  Cashier user already exists")
    
    db.session.commit()
    print("\n✅ Database seeded successfully!")
