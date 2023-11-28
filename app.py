from flask import Flask, render_template
import winsound  # This is for Windows; for other platforms, you might need a different library

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/beep/<frequency>/<times>')
def beep(frequency, times):
    frequency = int(frequency)
    times = int(times)

    for _ in range(times):
        winsound.Beep(frequency, 500)  # Beep for 500 milliseconds

    return 'Beeped {} times at {} Hz'.format(times, frequency)

if __name__ == '__main__':
    app.run(debug=True)
