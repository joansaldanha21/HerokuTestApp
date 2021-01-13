from flask import Flask, render_template, request, app




# --- User Interface ---

app = Flask(__name__)

@app.route('/')
def home():
    global userID, userconvo
    userconvo = []
    userID = 123
    intro=[]
    intro.append("Bot : Hi, I am AssistBot. Your customer service agent. How may I help you?")
    mike_status="no"
    resp="Hi, I am AssistBot. Your customer service agent. How may I help you?"
    userconvo.append(str("Bot : Hi, I am AssistBot. Your customer service agent. How may I help you?"))
    killSession="no"
    return render_template('index.html', user_input=intro,mike_status=mike_status,botResp=resp,userID=userID,killSession=killSession,userconvo=userconvo)

@app.route('/process', methods=['POST'])
def process():  ##called when user input is given and submit button is pressed
    global userID
    print("Process Called")
    userconvoprev = request.form["userconvo"]
    user_input = request.form["user_input"]
    print("userconvoprev :",userconvoprev)
    #userconvo.append(userconvoprev)
    userconvo.append("You : " + user_input)
    if (user_input == "TimeOut"):
       resp="Goodbye"
       userconvo.append("Bot : " + resp)
    else:
        resp = "Hello testing"
        userconvo.append("Bot : " + resp)
        print("Bot resp : ",resp)

    mike_status =  "yes" if request.form["mic_status"] ==  "on" else "no"
    print("mike_status : ",mike_status,request.form["mic_status"])
    userID = request.form["userID"]
    killSession = request.form["killSession"]
    print("killSession : ",killSession)
    rlist=userconvo
    print ("rlist",rlist)
    return render_template("index.html", user_input=rlist,mike_status=mike_status,botResp=resp,userID=userID,killSession=killSession,userconvo=userconvo)

#---- Kicking of the main program ----

if __name__ == "__main__":
    app.run(threaded=True,debug=True)






















