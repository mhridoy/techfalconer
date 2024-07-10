from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    services = [
        {
            'name': 'Custom Software Development',
            'description': 'Tailored software solutions to meet your unique business needs.',
            'icon': 'code',
            'image': 'https://source.unsplash.com/random/800x600/?software'
        },
        {
            'name': 'IT Consulting',
            'description': 'Expert advice to optimize your IT infrastructure and processes.',
            'icon': 'users',
            'image': 'https://source.unsplash.com/random/800x600/?consulting'
        },
        {
            'name': 'Cloud Solutions',
            'description': 'Scalable and secure cloud services for your growing business.',
            'icon': 'cloud',
            'image': 'https://source.unsplash.com/random/800x600/?cloud'
        },
        {
            'name': 'Cybersecurity',
            'description': 'Robust security measures to protect your digital assets.',
            'icon': 'shield',
            'image': 'https://source.unsplash.com/random/800x600/?security'
        }
    ]
    team_members = [
        {'name': 'Jane Doe', 'role': 'CEO', 'image': 'https://source.unsplash.com/random/300x300/?woman'},
        {'name': 'John Smith', 'role': 'CTO', 'image': 'https://source.unsplash.com/random/300x300/?man'},
        {'name': 'Emily Brown', 'role': 'Lead Developer', 'image': 'https://source.unsplash.com/random/300x300/?developer'}
    ]
    return render_template('index.html', services=services, team_members=team_members)

if __name__ == '__main__':
    app.run(debug=True)