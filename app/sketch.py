from flask import Blueprint,render_template
from mongodb import db

bp = Blueprint("sketch", __name__, url_prefix='/sketch')

@bp.route('/')
def main():
    return render_template('index.html')

@bp.route('/<url>', methods=['GET'])
def view_sketch(url):
    sketch = db.sketches.find_one({
        'url' : url
    })
    data = {'url': sketch['url'],
            'filename': sketch['filename'],
            'description': sketch['description'],
            'code': sketch['code']}
         
    return render_template('index.html', url=data['url'], code=data['code'], filename=data['filename'], description=data['description'])