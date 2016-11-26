from flask import Blueprint,jsonify, request
from mongodb import db
import hashlib
bp = Blueprint('api',__name__ , url_prefix='/api')

@bp.route('/sketches', methods=['POST'])
def add_sketch():
    url = request.form.get('url', '')
    filename = request.form.get('filename', '')
    description = request.form.get('description', '')
    code = request.form.get('code', None)

    if not code:
        return 'You forgot to paste your sketch!', 400

    hashUrl = hashlib.sha1((code + filename + description).encode("UTF-8")).hexdigest();
    hashUrl[:10]

    db.sketches.insert({
        'url': hashUrl[:10],
        'filename': filename,
        'description': description,
        'code': code
    })

    return hashUrl[:10]

@bp.route('/sketches/<url_str>', methods=['GET'])
def get_sketch_by_url(url_str):
    sketch = db.sketches.find_one({
        'url': url_str
    })

    data = {'url': sketch['url'],
            'filename': sketch['filename'],
            'description': sketch['description'],
            'code': sketch['code']
    }

    return jsonify(**data)
