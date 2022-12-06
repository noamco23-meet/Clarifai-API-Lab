from flask import Flask, render_template, request
import json, requests
app = Flask(__name__)

headers = {'Authorization': 'Key 4496012e67ac46eeb75687504b4429d5'}
api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"

people = {"people", "person", "adult", "teen", "child", "children", "baby", "babies" "man", "men", "women", "woman"}


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
    image_url = request.form['url-input']

    data ={"inputs": [{"data": {
          "image": {"url": image_url}}}]}

    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    response_dict = json.loads(response.content)['outputs'][0]['data']['concepts']
    results = []
    for key in response_dict:
        print(key)
        results.append(key['name'])
    
    results_set = set(results)
    human = results_set.intersection(people)
    isHuman = False
    if len(human) != 0:
        isHuman = True
    if "no person" in results_set:
        isHuman = False
    return render_template('home.html', results=results, length=len(results), human=isHuman)

if __name__ == '__main__':
    app.run(debug=True)