from flask import Flask
myapp = Flask(__name__)
# help
name="Lisa"
city_names=["Paris","London","Rome","Tahiti"]

@myapp.route("/")
def home():
	return f'''
	<html>
	<body>
		<h1>Welcome {name}!</h1>
		<a href="www.google.com">not google</a>
	<ul>
	<li>{city_names[0]}</li>
	<li>{city_names[1]}</li>
	<li>{city_names[2]}</li>
	<li>{city_names[3]}</li>
	</ul>
	</body>
	</html>
	'''
# myapp.run()
