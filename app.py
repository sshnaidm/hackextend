from flask import Flask, render_template, request, abort
import os
from skills import get_info
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['post', 'get'])
def index():
    message = 'Please submit your LinkedIn profile here'
    if request.method == 'POST':
        link = request.form.get('linkedin')
        skills_years = get_info(link)

        #return render_template('months.html.j2', skills=skills_years)
    elif request.method == 'GET':
        return render_template('form.html.j2', message=message)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)),
            debug=True)
