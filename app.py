import json
from flask import Flask, render_template, request
from learning import learning_blueprint
from models.item import Item
from views.items import item_blueprint

app = Flask(__name__)
app.register_blueprint(item_blueprint, url_prefix='/items')

if __name__ == '__main__':
    app.run(debug=True)


# url = 'https://www.johnlewis.com/asus-chromebook-flip-c433ta-intel-core-m3-4gb-ram-64gb-emmc-14-inch-full-hd-silver/p4811855'
# tag_name = 'p'
# query = {'class': 'price price--large'}
#
# asus_chrome = Item(url, tag_name, query)
# asus_chrome.save_to_mongo()
#
# items_loaded = Item.all()
# print(items_loaded[0].load_price())

# app = Flask(__name__)
#
# app.register_blueprint(learning_blueprint, url_prefix='/greetings')
#
# if __name__ == '__main__':
#     app.run()