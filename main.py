from flask import Flask,render_template,request
from PyMovieDb import IMDB
import json
app=Flask(__name__,template_folder='templates')
@app.route('/',methods=['POST','GET'])
@app.route('/search',methods=['POST','GET'])
def home():
    data=[]
    if request.method=='POST' and request.form['title']!="":
        title=request.form['title']
        try:
            results=search_by_title(title)
            for result in results:
                data.append(search_by_id(result['id']))
            return render_template('results.html',title=f"{title} data",data=data)
        except:
            return render_template('results.html',title="error")
    else:
        return render_template('home.html',title="Home Page")
def search_by_title(title):
    imdb = IMDB()
    res=imdb.search(title)
    res=json.loads(res)
    return res['results']
def search_by_id(id):
    imdb = IMDB()
    res = imdb.get_by_id(id)
    res=json.loads(res)
    return res
if __name__=='__main__':
    app.run(debug=True)