from flask import Flask, render_template, request
from pandas import read_excel

app = Flask(__name__)

def read_xlsx(filename, sheet):
    df = read_excel(filename, sheet_name=sheet)
    return df

@app.route("/")
def get_map():
    schools = read_xlsx('data.xlsx', '2021')
    return render_template("index.html", schools=schools)

@app.route("/coords_log")
def get_coords():
    year = request.args.get('year')
    addrs = list(read_xlsx('data.xlsx', year)['addr'])
    return render_template("coords.html", addrs=addrs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1303)