from flask import Flask
myapp = Flask(__name__)

name="jimbo"
city_names=["Paris","London","Rome","Tahiti"]

@myapp.route("/")
def home():
	html= '''
	<html>
	<body>
		<h1>Welcome '''+ name + '''</h1>
		<a href="www.google.com">not google</a>
		<ul>'''
	for city in city_names:
		html=html+"<li>"+city+"</li>"
	html=html+'''
	</ul>
	</body>
	</html>
	'''
	return html
# myapp.run()
