from flask import Flask, request

app = Flask(__name__)

HTML = """
<form method="POST">
    Maths: <input type="number" name="m1" required><br><br>
    Science: <input type="number" name="m2" required><br><br>
    English: <input type="number" name="m3" required><br><br>
    <button type="submit">Calculate</button>
</form>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        m1 = float(request.form["m1"])
        m2 = float(request.form["m2"])
        m3 = float(request.form["m3"])
        
        total = m1 + m2 + m3
        average = total / 3
        
        if average >= 90: grade = "A"
        elif average >= 75: grade = "B"
        elif average >= 50: grade = "C"
        else: grade = "F"
        
        return HTML + f"""
        <h3>Results:</h3>
        Total: {total}<br>
        Average: {average:.2f}<br>
        Grade: {grade}
        """
    return HTML

if __name__ == "__main__":
    app.run(debug=True)
