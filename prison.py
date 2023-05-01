import pymysql
from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import SelectField, SubmitField
from flask_bootstrap import Bootstrap5
#from modules import make_ordinal

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy()
# create the app
app = Flask(__name__)

# make sure the database username, database password and
# database name are correct
username = 'root'
password = ''
userpass = 'mysql+pymysql://' + username + ':' + password + '@'
# keep this as is for a hosted website
server  = '127.0.0.1'
# CHANGE to YOUR database name, with a slash added as shown
dbname   = '/prisoners'
# this socket is going to be very different on a WINDOWS computer
# try 'C:/xampp/mysql/mysql.sock'
socket   = '?unix_socket=/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock'


# CHANGE NOTHING BELOW
# put them all together as a string that shows SQLAlchemy where the database is
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SECRET_KEY'] = 'm0neYbUsH5cOpY'

# initialize the app with Flask-SQLAlchemy
db.init_app(app)

bootstrap = Bootstrap5(app)

csrf = CSRFProtect(app)

# each table in the database needs a class to be created for it
# this class is named Prison because the database contains info about prisons
# and the table in the database is named: socks
# db.Model is required - don't change it
# identify all columns by name and their data type

class Prison(db.Model):
	__tablename__ = 'pris4'
	id = db.Column(db.Integer, primary_key=True)
	state = db.Column(db.String)
	total_2021 = db.Column(db.Integer)
	male_2021 = db.Column(db.Integer)
	female_2021 = db.Column(db.Integer)
	rate_2021 = db.Column(db.Integer)
	white_2021 = db.Column(db.Integer)
	black_2021 = db.Column(db.Integer)
	hispanic_2021 = db.Column(db.Integer)
	asian_2021 = db.Column(db.Integer)
	native_2021 = db.Column(db.Integer)
	white_state_pop_2021 = db.Column(db.String)
	white_pris_pop_2021 = db.Column(db.String)
	black_state_pop_2021 = db.Column(db.String)
	black_prison_pop_2021 = db.Column(db.String)
	hispanic_state_pop_2021 = db.Column(db.String)
	hispanic_prison_pop_2021 = db.Column(db.String)
	native_state_pop_2021 = db.Column(db.String)
	native_prison_pop_2021 = db.Column(db.String)
	asian_state_pop_2021 = db.Column(db.String)
	asian_prison_pop_2021 = db.Column(db.String)
	total_2020 = db.Column(db.Integer)
	male_2020 = db.Column(db.Integer)
	female_2020 = db.Column(db.Integer)
	rate_2020 = db.Column(db.Integer)
	white_2020 = db.Column(db.Integer)
	black_2020 = db.Column(db.Integer)
	hispanic_2020 = db.Column(db.Integer)
	asian_2020 = db.Column(db.Integer)
	native_2020 = db.Column(db.Integer)
	total_2019 = db.Column(db.Integer)
	male_2019 = db.Column(db.Integer)
	female_2019 = db.Column(db.Integer)
	rate_2019 = db.Column(db.Integer)
	white_2019 = db.Column(db.Integer)
	black_2019 = db.Column(db.Integer)
	hispanic_2019 = db.Column(db.Integer)
	asian_2019 = db.Column(db.Integer)
	native_2019 = db.Column(db.Integer)
	total_2018 = db.Column(db.Integer)
	male_2018 = db.Column(db.Integer)
	female_2018 = db.Column(db.Integer)
	rate_2018 = db.Column(db.Integer)
	white_2018 = db.Column(db.Integer)
	black_2018 = db.Column(db.Integer)
	hispanic_2018 = db.Column(db.Integer)
	asian_2018 = db.Column(db.Integer)
	native_2018 = db.Column(db.Integer)
	total_2017 = db.Column(db.Integer)
	male_2017 = db.Column(db.Integer)
	female_2017 = db.Column(db.Integer)
	rate_2017 = db.Column(db.Integer)
	white_2017 = db.Column(db.Integer)
	black_2017 = db.Column(db.Integer)
	hispanic_2017 = db.Column(db.Integer)
	asian_2017 = db.Column(db.Integer)
	native_2017 = db.Column(db.Integer)
	total_2016 = db.Column(db.Integer)
	male_2016 = db.Column(db.Integer)
	female_2016 = db.Column(db.Integer)
	rate_2016 = db.Column(db.Integer)
	white_2016 = db.Column(db.Integer)
	black_2016 = db.Column(db.Integer)
	hispanic_2016 = db.Column(db.Integer)
	asian_2016 = db.Column(db.Integer)
	native_2016 = db.Column(db.Integer)
	total_2015 = db.Column(db.Integer)
	male_2015 = db.Column(db.Integer)
	female_2015 = db.Column(db.Integer)
	rate_2015 = db.Column(db.Integer)
	white_2015 = db.Column(db.Integer)
	black_2015 = db.Column(db.Integer)
	hispanic_2015 = db.Column(db.Integer)
	asian_2015 = db.Column(db.Integer)
	native_2015 = db.Column(db.Integer)
	total_2014 = db.Column(db.Integer)
	male_2014 = db.Column(db.Integer)
	female_2014 = db.Column(db.Integer)
	rate_2014 = db.Column(db.Integer)
	total_2013 = db.Column(db.Integer)
	male_2013 = db.Column(db.Integer)
	female_2013 = db.Column(db.Integer)
	rate_2013 = db.Column(db.Integer)
	total_2012 = db.Column(db.Integer)
	male_2012 = db.Column(db.Integer)
	female_2012 = db.Column(db.Integer)
	rate_2012 = db.Column(db.Integer)
	total_2011 = db.Column(db.Integer)
	male_2011 = db.Column(db.Integer)
	female_2011 = db.Column(db.Integer)
	rate_2011 = db.Column(db.Integer)
	total_2010 = db.Column(db.Integer)
	male_2010 = db.Column(db.Integer)
	female_2010 = db.Column(db.Integer)
	rate_2010 = db.Column(db.Integer)
	white_state_pop_2010 = db.Column(db.String)
	white_pris_pop_2010 = db.Column(db.String)
	black_state_pop_2010 = db.Column(db.String)
	black_prison_pop_2010 = db.Column(db.String)
	hispanic_state_pop_2010 = db.Column(db.String)
	hispanic_prison_pop_2010 = db.Column(db.String)
	native_state_pop_2010 = db.Column(db.String)
	native_prison_pop_2010 = db.Column(db.String)
	total_2009 = db.Column(db.Integer)
	male_2009 = db.Column(db.Integer)
	female_2009 = db.Column(db.Integer)
	rate_2009 = db.Column(db.Integer)
	total_2008 = db.Column(db.Integer)
	male_2008 = db.Column(db.Integer)
	female_2008 = db.Column(db.Integer)
	rate_2008 = db.Column(db.Integer)
	total_2007 = db.Column(db.Integer)
	male_2007 = db.Column(db.Integer)
	female_2007 = db.Column(db.Integer)
	rate_2007 = db.Column(db.Integer)
	total_2006 = db.Column(db.Integer)
	male_2006 = db.Column(db.Integer)
	female_2006 = db.Column(db.Integer)
	rate_2006 = db.Column(db.Integer)
	total_2005 = db.Column(db.Integer)
	male_2005 = db.Column(db.Integer)
	female_2005 = db.Column(db.Integer)
	rate_2005 = db.Column(db.Integer)
	total_2004 = db.Column(db.Integer)
	male_2004 = db.Column(db.Integer)
	female_2004 = db.Column(db.Integer)
	rate_2004 = db.Column(db.Integer)
	total_2003 = db.Column(db.Integer)
	male_2003 = db.Column(db.Integer)
	female_2003 = db.Column(db.Integer)
	rate_2003 = db.Column(db.Integer)
	total_2002 = db.Column(db.Integer)
	male_2002 = db.Column(db.Integer)
	female_2002 = db.Column(db.Integer)
	rate_2002 = db.Column(db.Integer)
	total_2001 = db.Column(db.Integer)
	male_2001 = db.Column(db.Integer)
	female_2001 = db.Column(db.Integer)
	rate_2001 = db.Column(db.Integer)
	total_2000 = db.Column(db.Integer)
	male_2000 = db.Column(db.Integer)
	female_2000 = db.Column(db.Integer)
	rate_2000 = db.Column(db.Integer)
	white_state_pop_2000 = db.Column(db.String)
	white_pris_pop_2000 = db.Column(db.String)
	black_state_pop_2000 = db.Column(db.String)
	black_prison_pop_2000 = db.Column(db.String)
	hispanic_state_pop_2000 = db.Column(db.String)
	hispanic_prison_pop_2000 = db.Column(db.String)
	native_state_pop_2000 = db.Column(db.String)
	native_prison_pop_2000 = db.Column(db.String)

class Total(db.Model):
	__tablename__ = 'tpris_2'
	id = db.Column(db.Integer, primary_key=True)
	state = db.Column(db.String)
	total_2021 = db.Column(db.Integer)
	male_2021 = db.Column(db.Integer)
	female_2021 = db.Column(db.Integer)
	rate_2021 = db.Column(db.Integer)
	white_2021 = db.Column(db.Integer)
	black_2021 = db.Column(db.Integer)
	hispanic_2021 = db.Column(db.Integer)
	asian_2021 = db.Column(db.Integer)
	native_2021 = db.Column(db.Integer)
	white_state_pop_2021 = db.Column(db.String)
	white_pris_pop_2021 = db.Column(db.String)
	black_state_pop_2021 = db.Column(db.String)
	black_prison_pop_2021 = db.Column(db.String)
	hispanic_state_pop_2021 = db.Column(db.String)
	hispanic_prison_pop_2021 = db.Column(db.String)
	native_state_pop_2021 = db.Column(db.String)
	native_prison_pop_2021 = db.Column(db.String)
	asian_state_pop_2021 = db.Column(db.String)
	asian_prison_pop_2021 = db.Column(db.String)
	other_prison_pop_2021 = db.Column(db.Integer)
	other_state_pop_2021 = db.Column(db.Integer)
	total_2020 = db.Column(db.Integer)
	male_2020 = db.Column(db.Integer)
	female_2020 = db.Column(db.Integer)
	rate_2020 = db.Column(db.Integer)
	white_2020 = db.Column(db.Integer)
	black_2020 = db.Column(db.Integer)
	hispanic_2020 = db.Column(db.Integer)
	asian_2020 = db.Column(db.Integer)
	native_2020 = db.Column(db.Integer)
	total_2019 = db.Column(db.Integer)
	male_2019 = db.Column(db.Integer)
	female_2019 = db.Column(db.Integer)
	rate_2019 = db.Column(db.Integer)
	white_2019 = db.Column(db.Integer)
	black_2019 = db.Column(db.Integer)
	hispanic_2019 = db.Column(db.Integer)
	asian_2019 = db.Column(db.Integer)
	native_2019 = db.Column(db.Integer)
	total_2018 = db.Column(db.Integer)
	male_2018 = db.Column(db.Integer)
	female_2018 = db.Column(db.Integer)
	rate_2018 = db.Column(db.Integer)
	white_2018 = db.Column(db.Integer)
	black_2018 = db.Column(db.Integer)
	hispanic_2018 = db.Column(db.Integer)
	asian_2018 = db.Column(db.Integer)
	native_2018 = db.Column(db.Integer)
	total_2017 = db.Column(db.Integer)
	male_2017 = db.Column(db.Integer)
	female_2017 = db.Column(db.Integer)
	rate_2017 = db.Column(db.Integer)
	white_2017 = db.Column(db.Integer)
	black_2017 = db.Column(db.Integer)
	hispanic_2017 = db.Column(db.Integer)
	asian_2017 = db.Column(db.Integer)
	native_2017 = db.Column(db.Integer)
	total_2016 = db.Column(db.Integer)
	male_2016 = db.Column(db.Integer)
	female_2016 = db.Column(db.Integer)
	rate_2016 = db.Column(db.Integer)
	white_2016 = db.Column(db.Integer)
	black_2016 = db.Column(db.Integer)
	hispanic_2016 = db.Column(db.Integer)
	asian_2016 = db.Column(db.Integer)
	native_2016 = db.Column(db.Integer)
	total_2015 = db.Column(db.Integer)
	male_2015 = db.Column(db.Integer)
	female_2015 = db.Column(db.Integer)
	rate_2015 = db.Column(db.Integer)
	white_2015 = db.Column(db.Integer)
	black_2015 = db.Column(db.Integer)
	hispanic_2015 = db.Column(db.Integer)
	asian_2015 = db.Column(db.Integer)
	native_2015 = db.Column(db.Integer)
	total_2014 = db.Column(db.Integer)
	male_2014 = db.Column(db.Integer)
	female_2014 = db.Column(db.Integer)
	rate_2014 = db.Column(db.Integer)
	total_2013 = db.Column(db.Integer)
	male_2013 = db.Column(db.Integer)
	female_2013 = db.Column(db.Integer)
	rate_2013 = db.Column(db.Integer)
	total_2012 = db.Column(db.Integer)
	male_2012 = db.Column(db.Integer)
	female_2012 = db.Column(db.Integer)
	rate_2012 = db.Column(db.Integer)
	total_2011 = db.Column(db.Integer)
	male_2011 = db.Column(db.Integer)
	female_2011 = db.Column(db.Integer)
	rate_2011 = db.Column(db.Integer)
	total_2010 = db.Column(db.Integer)
	male_2010 = db.Column(db.Integer)
	female_2010 = db.Column(db.Integer)
	rate_2010 = db.Column(db.Integer)
	white_state_pop_2010 = db.Column(db.String)
	white_pris_pop_2010 = db.Column(db.String)
	black_state_pop_2010 = db.Column(db.String)
	black_prison_pop_2010 = db.Column(db.String)
	hispanic_state_pop_2010 = db.Column(db.String)
	hispanic_prison_pop_2010 = db.Column(db.String)
	native_state_pop_2010 = db.Column(db.String)
	native_prison_pop_2010 = db.Column(db.String)
	total_2009 = db.Column(db.Integer)
	male_2009 = db.Column(db.Integer)
	female_2009 = db.Column(db.Integer)
	rate_2009 = db.Column(db.Integer)
	total_2008 = db.Column(db.Integer)
	male_2008 = db.Column(db.Integer)
	female_2008 = db.Column(db.Integer)
	rate_2008 = db.Column(db.Integer)
	total_2007 = db.Column(db.Integer)
	male_2007 = db.Column(db.Integer)
	female_2007 = db.Column(db.Integer)
	rate_2007 = db.Column(db.Integer)
	total_2006 = db.Column(db.Integer)
	male_2006 = db.Column(db.Integer)
	female_2006 = db.Column(db.Integer)
	rate_2006 = db.Column(db.Integer)
	total_2005 = db.Column(db.Integer)
	male_2005 = db.Column(db.Integer)
	female_2005 = db.Column(db.Integer)
	rate_2005 = db.Column(db.Integer)
	total_2004 = db.Column(db.Integer)
	male_2004 = db.Column(db.Integer)
	female_2004 = db.Column(db.Integer)
	rate_2004 = db.Column(db.Integer)
	total_2003 = db.Column(db.Integer)
	male_2003 = db.Column(db.Integer)
	female_2003 = db.Column(db.Integer)
	rate_2003 = db.Column(db.Integer)
	total_2002 = db.Column(db.Integer)
	male_2002 = db.Column(db.Integer)
	female_2002 = db.Column(db.Integer)
	rate_2002 = db.Column(db.Integer)
	total_2001 = db.Column(db.Integer)
	male_2001 = db.Column(db.Integer)
	female_2001 = db.Column(db.Integer)
	rate_2001 = db.Column(db.Integer)
	total_2000 = db.Column(db.Integer)
	male_2000 = db.Column(db.Integer)
	female_2000 = db.Column(db.Integer)
	rate_2000 = db.Column(db.Integer)
	white_state_pop_2000 = db.Column(db.String)
	white_pris_pop_2000 = db.Column(db.String)
	black_state_pop_2000 = db.Column(db.String)
	black_prison_pop_2000 = db.Column(db.String)
	hispanic_state_pop_2000 = db.Column(db.String)
	hispanic_prison_pop_2000 = db.Column(db.String)
	native_state_pop_2000 = db.Column(db.String)
	native_prison_pop_2000 = db.Column(db.String)

with app.app_context():
    prisons = db.session.execute(db.select(Prison)
		 .order_by(Prison.state)).scalars()
    # create the list of tuples needed for the choices value
	#make a list using tuple (Prison.state, Prison.state)
    pris_list = []
    for prison in prisons:
        pris_list.append( (prison.id, prison.state) )

class PrisonSelect(FlaskForm):
    select = SelectField( 'Choose a state:',
      choices=pris_list
      )
    submit = SubmitField('Submit')

#routes

@app.route('/')
def index():
    form = PrisonSelect()
    totals = db.session.execute(db.select(Total)
    .order_by(Total.state)).scalar()
    ichart = '''
	Highcharts.chart('icontainer', {
	    data: {
	        table: 'idatatable'
	    },
	    chart: {
	        type: 'line'
	    },
	    title: {
	        text: 'Prison populations since 2000'
	    },
	    subtitle: {
	        text:
	            'Source: <a href="https://bjs.ojp.gov" target="_blank">Bureau of Justice Statistics</a>'
	    },
	    xAxis: {
	        type: 'category'
	    },
	    yAxis: {
	        allowDecimals: false,
	        title: {
	            text: 'Population'
	        }
	    },
	    tooltip: {
	        formatter: function () {
	            return '<b>' + this.series.name + '</b><br/>' +
	                this.point.y + ' ' + this.point.name.toLowerCase();
	        }
	    }
	});
	'''
    rchart = '''
	Highcharts.chart('irate_container', {
	    data: {
	        table: 'iratetable'
	    },
	    chart: {
	        type: 'line'
	    },
	    title: {
	        text: 'Incarceration rates since 2000'
	    },
	    subtitle: {
	        text:
	            'Source: <a href="https://bjs.ojp.gov" target="_blank">Bureau of Justice Statistics</a>'
	    },
	    xAxis: {
	        type: 'category'
	    },
	    yAxis: {
	        allowDecimals: false,
	        title: {
	            text: 'Population'
	        }
	    },
	    tooltip: {
	        formatter: function () {
	            return '<b>' + this.series.name + '</b><br/>' +
	                this.point.y + ' ' + this.point.name.toLowerCase();
	        }
	    }
	});
	'''
    pchart = '''
	Highcharts.chart('ipie_container', {
	    data: {
	        table: 'ipietable'
	    },
	    chart: {
	        type: 'pie'
	    },
	    title: {
	        text: 'Percent of Prison Population by Race'
	    },
	    subtitle: {
	        text:
	            'Source: <a href="https://bjs.ojp.gov" target="_blank">Bureau of Justice Statistics</a>'
	    },
	    xAxis: {
	        type: 'category'
	    },
	    yAxis: {
	        allowDecimals: false,
	        title: {
	            text: 'Population'
	        }
	    },
	    tooltip: {
	        formatter: function () {
	            return '<b>' + this.series.name + '</b><br/>' +
	                this.point.y + ' ' + this.point.name.toLowerCase();
	        }
	    }
	});
	'''
    pchart2 = '''
	Highcharts.chart('ipie_container2', {
	    data: {
	        table: 'ipietable2'
	    },
	    chart: {
	        type: 'pie'
	    },
	    title: {
	        text: 'Percent of State Population by Race 2021'
	    },
	    subtitle: {
	        text:
	            'Source: <a href="https://www.census.gov/quickfacts/fact/table/US/RHI825221" target="_blank">U.S. Census Bureau</a>'
	    },
	    xAxis: {
	        type: 'category'
	    },
	    yAxis: {
	        allowDecimals: false,
	        title: {
	            text: 'Population'
	        }
	    },
	    tooltip: {
	        formatter: function () {
	            return '<b>' + this.series.name + '</b><br/>' +
	                this.point.y + ' ' + this.point.name.toLowerCase();
	        }
	    }
	});
	'''
    pchart3 = '''
	Highcharts.chart('ipie_container3', {
	    data: {
	        table: 'ipietable3'
	    },
	    chart: {
	        type: 'pie'
	    },
	    title: {
	        text: 'Percent of Prison Population by Race 2010'
	    },
	    subtitle: {
	        text:
	            'Source: <a href="https://www.prisonpolicy.org/reports/rates.html" target="_blank">Prison Policy Initiative</a>'
	    },
	    xAxis: {
	        type: 'category'
	    },
	    yAxis: {
	        allowDecimals: false,
	        title: {
	            text: 'Population'
	        }
	    },
	    tooltip: {
	        formatter: function () {
	            return '<b>' + this.series.name + '</b><br/>' +
	                this.point.y + ' ' + this.point.name.toLowerCase();
	        }
	    }
	});
	'''
    pchart4 = '''
	Highcharts.chart('ipie_container4', {
	    data: {
	        table: 'ipietable4'
	    },
	    chart: {
	        type: 'pie'
	    },
	    title: {
	        text: 'Percent of State Population by Race 2010'
	    },
	    subtitle: {
	        text:
	            'Source: <a href="https://www.prisonpolicy.org/reports/rates.html" target="_blank">Prison Policy Initiative</a>'
	    },
	    xAxis: {
	        type: 'category'
	    },
	    yAxis: {
	        allowDecimals: false,
	        title: {
	            text: 'Population'
	        }
	    },
	    tooltip: {
	        formatter: function () {
	            return '<b>' + this.series.name + '</b><br/>' +
	                this.point.y + ' ' + this.point.name.toLowerCase();
	        }
	    }
	});
	'''
    pchart5 = '''
	Highcharts.chart('ipie_container5', {
	    data: {
	        table: 'ipietable5'
	    },
	    chart: {
	        type: 'pie'
	    },
	    title: {
	        text: 'Percent of Prison Population by Race 2000'
	    },
	    subtitle: {
	        text:
	            'Source: <a href="https://www.prisonpolicy.org/graphs/statepopulations.html" target="_blank">Prison Policy Initiative</a>'
	    },
	    xAxis: {
	        type: 'category'
	    },
	    yAxis: {
	        allowDecimals: false,
	        title: {
	            text: 'Population'
	        }
	    },
	    tooltip: {
	        formatter: function () {
	            return '<b>' + this.series.name + '</b><br/>' +
	                this.point.y + ' ' + this.point.name.toLowerCase();
	        }
	    }
	});
	'''
    pchart6 = '''
	Highcharts.chart('ipie_container6', {
	    data: {
	        table: 'ipietable6'
	    },
	    chart: {
	        type: 'pie'
	    },
	    title: {
	        text: 'Percent of State Population by Race 2000'
	    },
	    subtitle: {
	        text:
	            'Source: <a href="https://www.prisonpolicy.org/graphs/statepopulations.html" target="_blank">Prison Policy Initiative</a>'
	    },
	    xAxis: {
	        type: 'category'
	    },
	    yAxis: {
	        allowDecimals: false,
	        title: {
	            text: 'Population'
	        }
	    },
	    tooltip: {
	        formatter: function () {
	            return '<b>' + this.series.name + '</b><br/>' +
	                this.point.y + ' ' + this.point.name.toLowerCase();
	        }
	    }
	});
	'''
    return render_template('index.html', the_title='U.S. Prison Population', totals=totals, form=form, ichart=ichart, rchart=rchart, pchart=pchart, pchart2=pchart2, pchart3=pchart3, pchart4=pchart4, pchart5=pchart5, pchart6=pchart6)

@app.route('/prison_pop', methods=['POST'])
def prison_detail():
    pris_id = request.form['select']
    # get all columns for the one state with the supplied id
    the_state = db.get_or_404(Prison, pris_id)
	#connect the javascript
    #js_url = url_for('static', filename='main.js')
    # pass it to the template
    ichart = '''
	Highcharts.chart('container', {
	    data: {
	        table: 'datatable'
	    },
	    chart: {
	        type: 'line'
	    },
	    title: {
	        text: 'Prison populations since 2000'
	    },
	    subtitle: {
	        text:
	            'Source: <a href="https://bjs.ojp.gov" target="_blank">Bureau of Justice Statistics</a>'
	    },
	    xAxis: {
	        type: 'category'
	    },
	    yAxis: {
	        allowDecimals: false,
	        title: {
	            text: 'Population'
	        }
	    },
	    tooltip: {
	        formatter: function () {
	            return '<b>' + this.series.name + '</b><br/>' +
	                this.point.y + ' ' + this.point.name.toLowerCase();
	        }
	    }
	});
	'''
    rchart = '''
	Highcharts.chart('rate_container', {
	    data: {
	        table: 'ratetable'
	    },
	    chart: {
	        type: 'line'
	    },
	    title: {
	        text: 'Incarceration rates since 2000'
	    },
	    subtitle: {
	        text:
	            'Source: <a href="https://bjs.ojp.gov" target="_blank">Bureau of Justice Statistics</a>'
	    },
	    xAxis: {
	        type: 'category'
	    },
	    yAxis: {
	        allowDecimals: false,
	        title: {
	            text: 'Population'
	        }
	    },
	    tooltip: {
	        formatter: function () {
	            return '<b>' + this.series.name + '</b><br/>' +
	                this.point.y + ' ' + this.point.name.toLowerCase();
	        }
	    }
	});
	'''
    pchart = '''
	Highcharts.chart('pie_container', {
	    data: {
	        table: 'pietable'
	    },
	    chart: {
	        type: 'pie'
	    },
	    title: {
	        text: 'Percent of Prison Population by Race'
	    },
	    subtitle: {
	        text:
	            'Source: <a href="https://bjs.ojp.gov" target="_blank">Bureau of Justice Statistics</a>'
	    },
	    xAxis: {
	        type: 'category'
	    },
	    yAxis: {
	        allowDecimals: false,
	        title: {
	            text: 'Population'
	        }
	    },
	    tooltip: {
	        formatter: function () {
	            return '<b>' + this.series.name + '</b><br/>' +
	                this.point.y + ' ' + this.point.name.toLowerCase();
	        }
	    }
	});
	'''
    pchart2 = '''
	Highcharts.chart('pie_container2', {
	    data: {
	        table: 'pietable2'
	    },
	    chart: {
	        type: 'pie'
	    },
	    title: {
	        text: 'Percent of State Population by Race 2021'
	    },
	    subtitle: {
	        text:
	            'Source: <a href="https://www.census.gov/quickfacts/fact/table/US/RHI825221" target="_blank">U.S. Census Bureau</a>'
	    },
	    xAxis: {
	        type: 'category'
	    },
	    yAxis: {
	        allowDecimals: false,
	        title: {
	            text: 'Population'
	        }
	    },
	    tooltip: {
	        formatter: function () {
	            return '<b>' + this.series.name + '</b><br/>' +
	                this.point.y + ' ' + this.point.name.toLowerCase();
	        }
	    }
	});
	'''
    pchart3 = '''
	Highcharts.chart('pie_container3', {
	    data: {
	        table: 'pietable3'
	    },
	    chart: {
	        type: 'pie'
	    },
	    title: {
	        text: 'Percent of Prison Population by Race 2010'
	    },
	    subtitle: {
	        text:
	            'Source: <a href="https://www.prisonpolicy.org/reports/rates.html" target="_blank">Prison Policy Initiative</a>'
	    },
	    xAxis: {
	        type: 'category'
	    },
	    yAxis: {
	        allowDecimals: false,
	        title: {
	            text: 'Population'
	        }
	    },
	    tooltip: {
	        formatter: function () {
	            return '<b>' + this.series.name + '</b><br/>' +
	                this.point.y + ' ' + this.point.name.toLowerCase();
	        }
	    }
	});
	'''
    pchart4 = '''
	Highcharts.chart('pie_container4', {
	    data: {
	        table: 'pietable4'
	    },
	    chart: {
	        type: 'pie'
	    },
	    title: {
	        text: 'Percent of State Population by Race 2010'
	    },
	    subtitle: {
	        text:
	            'Source: <a href="https://www.prisonpolicy.org/reports/rates.html" target="_blank">Prison Policy Initiative</a>'
	    },
	    xAxis: {
	        type: 'category'
	    },
	    yAxis: {
	        allowDecimals: false,
	        title: {
	            text: 'Population'
	        }
	    },
	    tooltip: {
	        formatter: function () {
	            return '<b>' + this.series.name + '</b><br/>' +
	                this.point.y + ' ' + this.point.name.toLowerCase();
	        }
	    }
	});
	'''
    pchart5 = '''
	Highcharts.chart('pie_container5', {
	    data: {
	        table: 'pietable5'
	    },
	    chart: {
	        type: 'pie'
	    },
	    title: {
	        text: 'Percent of Prison Population by Race 2000'
	    },
	    subtitle: {
	        text:
	            'Source: <a href="https://www.prisonpolicy.org/graphs/statepopulations.html" target="_blank">Prison Policy Initiative</a>'
	    },
	    xAxis: {
	        type: 'category'
	    },
	    yAxis: {
	        allowDecimals: false,
	        title: {
	            text: 'Population'
	        }
	    },
	    tooltip: {
	        formatter: function () {
	            return '<b>' + this.series.name + '</b><br/>' +
	                this.point.y + ' ' + this.point.name.toLowerCase();
	        }
	    }
	});
	'''
    pchart6 = '''
	Highcharts.chart('pie_container6', {
	    data: {
	        table: 'pietable6'
	    },
	    chart: {
	        type: 'pie'
	    },
	    title: {
	        text: 'Percent of State Population by Race 2000'
	    },
	    subtitle: {
	        text:
	            'Source: <a href="https://www.prisonpolicy.org/graphs/statepopulations.html" target="_blank">Prison Policy Initiative</a>'
	    },
	    xAxis: {
	        type: 'category'
	    },
	    yAxis: {
	        allowDecimals: false,
	        title: {
	            text: 'Population'
	        }
	    },
	    tooltip: {
	        formatter: function () {
	            return '<b>' + this.series.name + '</b><br/>' +
	                this.point.y + ' ' + this.point.name.toLowerCase();
	        }
	    }
	});
	'''
    return render_template('prison.html', the_title=pris_id, the_state=the_state, ichart=ichart, rchart=rchart, pchart=pchart, pchart2=pchart2, pchart3=pchart3, pchart4=pchart4, pchart5=pchart5, pchart6=pchart6)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=4999, debug=True)
