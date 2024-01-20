from flask import Flask, render_template,url_for, redirect,request
import requests
import json
from classes.utility import percent_calc

app = Flask("App")


@app.route('/vote',methods=['GET'])
def retrieve_poll():
    """ Gets poll detail from PollAPI to display options"""
    response = requests.get('http://localhost:5000/voting')
    data = json.loads(response.text)
    return render_template('vote.html',data=data)


@app.route('/vote',methods=['GET','POST'])
def submit():
    """Submit to post poll_id and option_id"""
    option_id = request.form.get('option_id')
    poll_id = request.form.get('poll_id')
    
    # post vote
    base_url = 'http://localhost:5000/polls/'+poll_id+'/'+option_id
    send = requests.post(base_url)
    return option_id

# @app.route('/confirm',methods=['GET','POST'])
# def confirm_page(poll_id,option_id):
#     """ Recieves poll_id and option_id """
#     option_id = request.form.get('option_id')
#     poll_id = request.form.get('poll_id')
#     base_url = 'http://localhost:5000/polls/'
    
#     #post data
#     # param = [poll_id,option_id]
#     # send = requests.post(base_url+poll_id)
    
#     #get poll by id
#     response =requests.get(base_url+poll_id)
#     data = response.text
    
#     return data


# @app.route('/confirmation', methods=['GET','POST'])
# def confirm_page():
#     """ Gets the votes details and displays confirm after submission"""
#     form_data = request.form.get('vote_options')
#     votes_response = requests.get('http://localhost:5000/confirmation')
#     graph_data = percent_calc(votes_response.text)
    
#     # some function to handle this data 
#     return render_template('confirmation.html',form_data=form_data,
#                            votes_data=graph_data)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=80)