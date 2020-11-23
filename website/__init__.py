from flask import (
    Flask,
    render_template,
    redirect
)


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    @app.route('/', methods=["GET"])
    def home():
        """The index / home route of the website"""

        # Technology, Stars out of 5
        technologies = [
            ('Python', 5),
            ('Java', 5),
            ('C++', 5),
            ('CSS', 5),
            ('Javascript', 5),
            ('Git', 5),
            ('Docker', 5),
            ('LXC / LXD', 5),
            ('Ansible', 4),
            ('Open Computer Vision', 5),
            ('NGINX', 4),
            ('Flask', 5),
            ('Github', 5),
            ('Gitlab', 5),
            ('Elasticsearch', 3),
            ('Kibana', 3),
            ('Logstash', 3),
            ('REST APIs', 5),
            ('JSON', 5),
            ('YAML', 5),
            ('Kubernetes', 4)
        ]
        tools = [
            ('Proxmox', 5),
            ('Debian', 5),
            ('Ubuntu', 5),
            ('Visual Studio 2019', 4),
            ('Manjaro', 5),
            ('Windows', 5),
            ('VSCode', 5),
            ('VMWare', 5),
            ('ESXI', 5),
        ]

        technologies.sort(key=lambda x: x[1], reverse = True)
        tools.sort(key=lambda x: x[1], reverse = True)
        
        technologies_left=technologies[:len(technologies) // 2]
        technologies_right=technologies[len(technologies) // 2:]

        return render_template('home.html',
                               technologies_left=technologies_left,
                               technologies_right=technologies_right,
                               tools=tools)

    @app.route('/github', methods=["GET"])
    def github():
        """This route redirects to my github"""
        return redirect('https://github.com/santosderek')

    @app.route('/linkedin', methods=["GET"])
    def linkedin():
        """This route redirects to my linkedin"""
        return redirect('https://www.linkedin.com/in/santosderek/')

    return app
