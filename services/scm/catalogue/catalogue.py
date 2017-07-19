'''
Try & be generic for all asset types: audio, video, image, product?
    - cons:
        - give redundant data/schemas
Parameters
    - type: audio, video, image, podcast etc
    - parent: make them composable


Queues
    - <assetType>.created


'''


from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return 'catalogue home'

@app.route('/catalogue', methods=['POST'])
def catalogue_add():
    return 'catalogue add'


app.run(debug=True)