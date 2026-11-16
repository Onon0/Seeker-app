from flask import Flask, render_template
app = Flask(__name__)

@app.route('/watership/introduction')
def introduction():
    return render_template("watership/introduction.html", title="Watership python web development framework")



@app.route('/watership')
def getting_started():
    return render_template("watership/introduction.html", title="Watership documentation")

@app.route('/watership/tutorial/<int:chapter>')       
def tutorial_1(chapter):
    if chapter == 1:
        return render_template("watership/hello_world.html", title="Watership documentation")
    elif chapter == 2: 
        return render_template("watership/doc_variables.html", title="Watership documentation")
    elif chapter == 3: 
        return render_template("watership/doc_loops.html", title="Watership documentation")
    elif chapter == 4: 
        return render_template("watership/doc_functions.html", title="Watership documentation")
    elif chapter == 5: 
        return render_template("watership/doc_collections.html", title="Watership documentation")
    elif chapter == 6:
        return render_template("watership/doc_enum.html", title="Watership documentation")
    elif chapter == 7: 
        return render_template("watership/doc_oop.html", title="Watership documentation")
    elif chapter == 8: 
        return render_template("watership/pipelines.html", title="Watership documentation")
    elif chapter == 9: 
        return render_template("watership/doc_polymorphism.html", title="Watership documentation")
    elif chapter == 10: 
        return render_template("watership/doc_references.html", title="Watership documentation")

    else:
        return "invalid path"

