{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":21,"position":21,"stack":[[{"start":{"row":0,"column":0},"end":{"row":14,"column":23},"action":"insert","lines":["import os","from flask import Flask","","app = Flask(__name__)","","","@app.route('/')","def hello():","    return 'Hello World ...again'","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":1}],[{"start":{"row":12,"column":36},"end":{"row":12,"column":37},"action":"insert","lines":[","],"id":2}],[{"start":{"row":12,"column":37},"end":{"row":12,"column":38},"action":"insert","lines":[" "],"id":3}],[{"start":{"row":12,"column":38},"end":{"row":12,"column":40},"action":"insert","lines":["''"],"id":4}],[{"start":{"row":12,"column":39},"end":{"row":12,"column":40},"action":"insert","lines":["0"],"id":5},{"start":{"row":12,"column":40},"end":{"row":12,"column":41},"action":"insert","lines":["."]},{"start":{"row":12,"column":41},"end":{"row":12,"column":42},"action":"insert","lines":["0"]},{"start":{"row":12,"column":42},"end":{"row":12,"column":43},"action":"insert","lines":["."]},{"start":{"row":12,"column":43},"end":{"row":12,"column":44},"action":"insert","lines":["0"]},{"start":{"row":12,"column":44},"end":{"row":12,"column":45},"action":"insert","lines":["."]}],[{"start":{"row":12,"column":45},"end":{"row":12,"column":46},"action":"insert","lines":["0"],"id":6}],[{"start":{"row":13,"column":42},"end":{"row":13,"column":43},"action":"insert","lines":[","],"id":7}],[{"start":{"row":13,"column":43},"end":{"row":13,"column":44},"action":"insert","lines":[" "],"id":8}],[{"start":{"row":13,"column":44},"end":{"row":13,"column":46},"action":"insert","lines":["''"],"id":9}],[{"start":{"row":13,"column":45},"end":{"row":13,"column":46},"action":"insert","lines":["8"],"id":10},{"start":{"row":13,"column":46},"end":{"row":13,"column":47},"action":"insert","lines":["0"]},{"start":{"row":13,"column":47},"end":{"row":13,"column":48},"action":"insert","lines":["8"]},{"start":{"row":13,"column":48},"end":{"row":13,"column":49},"action":"insert","lines":["0"]}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":32},"action":"remove","lines":["Hello World ...again"],"id":18},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["I"]}],[{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["v"],"id":19},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":[" "],"id":20}],[{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"remove","lines":[" "],"id":21},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"remove","lines":["e"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"remove","lines":["v"]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"remove","lines":["'"]}],[{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["\\"],"id":22},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["'"]},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["v"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":[" "],"id":23},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":["e"]},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":["n"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":["a"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":["b"]}],[{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["l"],"id":24},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":["e"]},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":["d"]}],[{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":[" "],"id":25},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"insert","lines":["a"]},{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"insert","lines":["u"]},{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"insert","lines":["t"]},{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"insert","lines":["o"]},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["m"]},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"insert","lines":["a"]},{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"insert","lines":["t"]},{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"insert","lines":["i"]},{"start":{"row":8,"column":34},"end":{"row":8,"column":35},"action":"insert","lines":["c"]}],[{"start":{"row":8,"column":35},"end":{"row":8,"column":36},"action":"insert","lines":[" "],"id":26},{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["d"]},{"start":{"row":8,"column":37},"end":{"row":8,"column":38},"action":"insert","lines":["e"]},{"start":{"row":8,"column":38},"end":{"row":8,"column":39},"action":"insert","lines":["p"]},{"start":{"row":8,"column":39},"end":{"row":8,"column":40},"action":"insert","lines":["l"]},{"start":{"row":8,"column":40},"end":{"row":8,"column":41},"action":"insert","lines":["o"]},{"start":{"row":8,"column":41},"end":{"row":8,"column":42},"action":"insert","lines":["y"]}],[{"start":{"row":8,"column":42},"end":{"row":8,"column":43},"action":"insert","lines":["s"],"id":27},{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"insert","lines":["'"]}],[{"start":{"row":8,"column":13},"end":{"row":8,"column":15},"action":"remove","lines":["\\'"],"id":28}],[{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["\\"],"id":29},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["'"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":8,"column":15},"end":{"row":8,"column":15},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1563545320895,"hash":"b598ac4bc0f6488db8b295a289b030acf2afcc96"}