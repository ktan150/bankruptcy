#!/usr/bin/env python
# coding: utf-8

# In[22]:


from flask import Flask


# In[23]:


app = Flask(__name__)


# In[24]:


from flask import request, render_template #request data from front end and post back 
from keras.models import load_model

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        NPTA = request.form.get("NPTA")
        TLTA = request.form.get("TLTA")
        WCTA = request.form.get("WCTA")
        print(NPTA,TLTA,WCTA)
        model=load_model("bankruptcy")
        pred=model.predict([[float(NPTA),float(TLTA),float(WCTA)]])
        s = "The predicted bankruptcy score is:" + str(pred)
        return(render_template("index.html",result=s))
    else:
        return(render_template("index.html",result="2"))


# In[ ]:


if __name__=="__main__":
    app.run()
    
#only if it is ur program, then it can run 


# In[ ]:




