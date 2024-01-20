from flask import Flask, render_template,url_for, redirect,request
import requests
import json
from classes.utility import percent_calc

app = Flask("App")


@app.route('/voting',methods=['GET'])
def retrieve_poll():
    """ Gets poll detail from PollAPI to display options"""
    response = requests.get('http://localhost:5000/voting')
    data = json.loads(response.text)
    return render_template('voting.html',data=data)


@app.route('/voting', methods=['Post'])
def submit_vote():
    """ Submit vote option to confirm page to display"""
    return redirect(url_for("confirm_page"))

@app.route('/confirmation', methods=['GET','POST'])
def confirm_page():
    """ Gets the votes details and displays confirm after submission"""
    form_data = request.form.get('vote_options')
    votes_response = requests.get('http://localhost:5000/confirmation')
    graph_data = percent_calc(votes_response.text)
    
    # some function to handle this data 
    return render_template('confirmation.html',form_data=form_data,
                           votes_data=graph_data)


# @app.route('/confirmation')
# def confirm_page():
#     pass

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=80)