from flask import Flask, render_template, request

app = Flask(__name__)

# 메인 페이지
@app.route('/')
def home():
    return render_template('kor/main.html') 

# 튜토리얼 페이지
@app.route('/tutorial')
def tutorial():
    return render_template('kor/tutorial.html')  

# 악기 소개 페이지
@app.route('/instrument')
def instrument():
    return render_template('kor/instrument.html')  

# 합주 시작 페이지
@app.route('/compose_start')
def compose_start():
    return render_template('kor/Compose_Start.html')  

# 합주 완료 페이지
@app.route('/compose_finish')
def compose_finish():
    return render_template('kor/Compose_Finish.html')  

# 에러 페이지
@app.route('/error')
def error():
    return render_template('kor/error.html')  


############### 중국어 ###############
# 메인 페이지
@app.route('/zh_main')
def zh_home():
    return render_template('chs/zh_main.html') 

# 튜토리얼 페이지
@app.route('/zh_tutorial')
def zh_tutorial():
    return render_template('chs/zh_tutorial.html')  

# 악기 소개 페이지
@app.route('/zh_instrument')
def zh_instrument():
    return render_template('chs/zh_instrument.html')  

# 합주 시작 페이지
@app.route('/zh_compose_start')
def zh_compose_start():
    return render_template('chs/zh_Compose_Start.html')  

# 합주 완료 페이지
@app.route('/zh_compose_finish')
def zh_compose_finish():
    return render_template('chs/zh_Compose_Finish.html')  

# 에러 페이지
@app.route('/zh_error')
def zh_error():
    return render_template('chs/zh_error.html')  
#####################################################


############### 영어 ###############
# 메인 페이지
@app.route('/en_main')
def en_home():
    return render_template('eng/en_main.html') 

# 튜토리얼 페이지
@app.route('/en_tutorial')
def en_tutorial():
    return render_template('eng/en_tutorial.html')  

# 악기 소개 페이지
@app.route('/en_instrument')
def en_instrument():
    return render_template('eng/en_instrument.html')  

# 합주 시작 페이지
@app.route('/en_compose_start')
def en_compose_start():
    return render_template('eng/en_Compose_Start.html')  

# 합주 완료 페이지
@app.route('/en_compose_finish')
def en_compose_finish():
    return render_template('eng/en_Compose_Finish.html')  

# 에러 페이지
@app.route('/en_error')
def en_error():
    return render_template('eng/en_error.html')  
#####################################################


############### 일본어 ###############
# 메인 페이지
@app.route('/jpn')
def ja_home():
    return render_template('jpn/ja_main.html') 

# 튜토리얼 페이지
@app.route('/ja_tutorial')
def ja_tutorial():
    return render_template('jpn/ja_tutorial.html')  

# 악기 소개 페이지
@app.route('/ja_instrument')
def ja_instrument():
    return render_template('jpn/ja_instrument.html')  

# 합주 시작 페이지
@app.route('/ja_compose_start')
def ja_compose_start():
    return render_template('jpn/ja_Compose_Start.html')  

# 합주 완료 페이지
@app.route('/ja_compose_finish')
def ja_compose_finish():
    return render_template('jpn/ja_Compose_Finish.html')  

# 에러 페이지
@app.route('/ja_error')
def ja_error():
    return render_template('jpn/ja_error.html')  
#####################################################



# 404 에러 핸들러
@app.errorhandler(404)
def page_not_found(e):
    path = request.path
    if path.startswith('/zh'):
        return render_template('chs/zh_error.html'), 404
    elif path.startswith('/en'):
        return render_template('eng/en_error.html'), 404
    elif path.startswith('/ja'):
        return render_template('jpn/ja_error.html'), 404
    else:
        return render_template('kor/error.html'), 404


# 500 에러 핸들러
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('kor/error.html'), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
