# Musu Flask serveris
from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
from flask import jsonify

app = Flask(__name__)

# Galvenā dekorācija. Izsauc ar http://127.0.0.1:5000/
@app.route('/',methods=['GET'])
def root():
    # metode render_template atgiež norādīto lapu, kas
    # atrodas mapē templates. Izsaucot var norādīt arī
    # parametru vērtības, kuras ievieto atbilstoši norādītajās
    # html dokumenta vietās. Piemēram:
    # render_template("vards.html",vards="Juris")
    # Mainīgā vards atrašanās vietu html dokumentā norāda ar {{ }}
    # Piemēram: <p>Mans vārds ir {{vards}}</p>
    # Rinda pārlūkā izskatīsies šādi: Mans vārds ir Juris
    return render_template("tests.html")
#----------------------------------------------------   
# Var veidot pēc vajadzības daudz dekorāciju.
# Šo izsauc ar http://127.0.0.1:5000/tests
@app.route('/tests')
def health():
  return render_template("tests.html")

@app.route('/gadalaiks')
def gadalaiks():
  return render_template("gadalaiks.html")

@app.route('/gadalaiki/<menesis>')
def gadalaiki(menesis):
    return render_template("menesis.html",menesis=menesis)
#----------------------------------------------------   
if __name__ == '__main__':
  app.run(debug=True,port=5000) # ,host='10.1.15.xx' host='0.0.0.0' - datora IP adrese

