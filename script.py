from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import csv
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///card_status.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class CardStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_id = db.Column(db.String(50), nullable=False)
    user_contact = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    status_type = db.Column(db.String(20), nullable=False)
    comment = db.Column(db.String(200))


db.create_all()


def load_data():
    csv_files = ['pickup1.csv', 'returned.csv', 'delivery_exceptions.csv', 'pickup2.csv']

    for csv_file in csv_files:
        with open(f'data/{csv_file}', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                card_status = CardStatus(
                    card_id=row[1],
                    user_contact=row[2].strip('"'),
                    timestamp=datetime.strptime(row[3], '%d-%m-%Y %I:%M %p'),
                    status_type=csv_file.split('.')[0],
                    comment=row[4] if len(row) == 5 else None
                )
                try:
                    with app.app_context():
                        db.session.add(card_status)
                        db.session.commit()
                except IntegrityError:
                    with app.app_context():
                        db.session.rollback()



@app.route('/get_card_status', methods=['GET'])
def get_card_status():
    user_input = request.args.get('input')

    if not user_input:
        return jsonify({'error': 'Input parameter is required'}), 400

    with app.app_context():
        card_status = CardStatus.query.filter(
            (CardStatus.card_id == user_input) | (CardStatus.user_contact == user_input)
        ).order_by(CardStatus.timestamp.desc()).first()

    if not card_status:
        return jsonify({'error': 'Card not found'}), 404

    response_payload = {
        'card_id': card_status.card_id,
        'user_contact': card_status.user_contact,
        'timestamp': card_status.timestamp.strftime('%d-%m-%Y %I:%M %p'),
        'status_type': card_status.status_type,
        'comment': card_status.comment
    }

    return jsonify(response_payload)

if __name__ == '__main__':
    app.run(debug=True)
