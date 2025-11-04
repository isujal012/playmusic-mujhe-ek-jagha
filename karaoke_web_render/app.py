from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    lyrics = [
        (0.505, "Mujhe Ek Jagha"),
        (2.422, "Aaram Nahi"),
        (3.933, "Rukja Na Mera"),
        (5.545, "Kaam Nahi"),
        (7.253, "Mera Sath Kahan Tak"),
        (9.216, "Dogii Tum"),
        (10.823, "Mai Desh Videsh"),
        (12.467, "Ka Banjara"),
        (14.244, "Itna Na Mujse"),
        (16.347, "Tu Pyaar Badha"),
        (17.649, "Ki Mai Ek Baadal"),
        (19.678, "Aawara..."),
        (21.362, "Kaise kisi ka"),
        (22.974, "Sahara Banoon"),
        (24.055, "ki Mai Khud Beghar"),
        (26.986, "Becharaaa....")
    ]
    return render_template('index.html', lyrics=lyrics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
