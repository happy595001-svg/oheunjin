from flask import Flask, render_template, request

from company_info import company_data
from news_api import get_news

app = Flask(__name__)

companies = list(company_data.keys())


@app.route('/')
def home():

    news = get_news("현대자동차 자동차 산업")

    return render_template(
        'index.html',
        companies=companies,
        news=news
    )



@app.route('/company/<name>')
def company_page(name):

    company = company_data[name]

    news = get_news(company['search_keyword'])

    return render_template(
        'company.html',
        name=name,
        company=company,
        news=news
    )


app.run(debug=True)