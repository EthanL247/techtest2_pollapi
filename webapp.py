
from flask import Flask, render_template,url_for, redirect,request
import requests
import json

#internal libraries
from classes.utility import HBar

app = Flask("App")


@app.route('/vote',methods=['GET'])
def retrieve_poll():
    """ Gets poll detail from PollAPI to display options"""
    response = requests.get('http://localhost:5000/polls')
    data = json.loads(response.text)
    return render_template('vote.html',data=data)


@app.route('/vote',methods=['GET','POST'])
def submit():
    """Submit to post poll_id and option_id"""
    option_id = request.form.get('option_id')
    poll_id = request.form.get('poll_id')
    
    # post vote: updates correct option count by 1 in local memory of API
    base_url = 'http://localhost:5000/votes/'+poll_id+'/'+option_id
    send = requests.post(base_url)
    
    # get vote data
    vote_data = requests.get(base_url+poll_id).json()  
    return redirect(url_for('confirm_page',data=vote_data))

# @app.route('/confirmation', methods=['GET','POST'])
# def confirm_page():
#     """ Gets the votes details and displays confirm after submission"""
#     form_data = request.form.get('vote_options')
#     votes_response = requests.get('http://localhost:5000/confirmation')
#     graph_data = percent_calc(votes_response.text)
    
#     # some function to handle this data 
#     return render_template('confirmation.html',form_data=form_data,
#                            votes_data=graph_data)

@app.route('/confirm')
def confirm_page():
    data = request.args.get('data',None)
    hbar = HBar()
    graph_data = hbar.etl(data)
    fig = hbar.fig(graph_data)
    res = hbar.export(fig)
    return render_template('confirm.html')
    

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=80)