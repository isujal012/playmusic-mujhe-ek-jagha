from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Playlist metadata: filename is the file you must place in /static/
# lyrics: list of (time_seconds, "text")
songs = [
    {
        "id": 0,
        "title": "Mujhe Ek Jagha",
        "filename": "song1.mp3",  # put this file in static/
        "lyrics": [
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
            (21.362, "Kaise Kisi Ka"),
            (22.974, "Sahara Banoon"),
            (24.055, "Ki Mai Khud Beghar"),
            (26.986, "Becharaaa....")
        ]
    },
    {
        "id": 1,
        "title": "Sample Song 2",
        "filename": "song2.mp3",  # put this file in static/
        "lyrics": [
            (0.3, "This is a sample"),
            (1.8, "Second line of sample"),
            (3.1, "Third line here"),
            (4.6, "And the chorus goes")
        ]
    }
]

@app.route("/")
def index():
    # We'll fetch /songs from the client; but embed small data if needed.
    return render_template("index.html")

@app.route("/songs")
def list_songs():
    # Provide minimal metadata to the client
    out = [
        {"id": s["id"], "title": s["title"], "filename": s["filename"]}
        for s in songs
    ]
    return jsonify(out)

@app.route("/song/<int:song_id>")
def song_data(song_id):
    for s in songs:
        if s["id"] == song_id:
            return jsonify({
                "id": s["id"],
                "title": s["title"],
                "filename": s["filename"],
                "lyrics": s["lyrics"]
            })
    return jsonify({"error": "song not found"}), 404

if __name__ == "__main__":
    # For Render use host=0.0.0.0 and choose port from env if needed (render overrides)
    app.run(host="0.0.0.0", port=10000, debug=True)
