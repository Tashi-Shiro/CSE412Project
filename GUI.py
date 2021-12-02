import sys
from PyQt5.uic import loadUi
import psycopg2
from PyQt5 import QtWidgets, QtWebEngineWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from pandas import DataFrame
from urllib.request import urlopen
import plotly.express as px
import pandas as pd
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

#df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
#                   dtype={"fips": str})

hostname = "localhost"
dbname = "postgres"
username = "postgres"
pwd = "wyc19990323"
port_id = 5432

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main.ui", self)
        self.areabutton.clicked.connect(self.gotoArea)
        self.statebutton.clicked.connect(self.gotoState)
        self.countybutton.clicked.connect(self.gotoCounty)
        self.popbutton.clicked.connect(self.gotoPopulation)
        self.covidbutton.clicked.connect(self.gotoCovid)
        self.vaccinebutton.clicked.connect(self.gotoVaccine)
        self.vaccbrandbutton.clicked.connect(self.gotoVaccBrand)
        self.ratiobutton.clicked.connect(self.gotoRatio)
        self.stateCountybutton.clicked.connect(self.gotoStateCounty)

    def gotoArea(self):
        widget.setCurrentIndex(1)
    def gotoState(self):
        widget.setCurrentIndex(2)
    def gotoCounty(self):
        widget.setCurrentIndex(3)
    def gotoPopulation(self):
        widget.setCurrentIndex(4)
    def gotoCovid(self):
        widget.setCurrentIndex(5)
    def gotoVaccine(self):
        widget.setCurrentIndex(6)
    def gotoVaccBrand(self):
        widget.setCurrentIndex(7)
    def gotoRatio(self):
        widget.setCurrentIndex(9)
    def gotoStateCounty(self):
        widget.setCurrentIndex(10)




class Area(QDialog):
    def __init__(self):
        super(Area, self).__init__()
        loadUi("area.ui", self)
        self.backbutton1.clicked.connect(self.areaBack)
        self.Graph1.clicked.connect(self.gotoGraph1)
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 300)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["FIPS", "Area Name"])
        self.loadAreaData()


    def areaBack(self):
        widget.setCurrentIndex(0)

    def gotoGraph1(self):
        widget.setCurrentIndex(8)

    def loadAreaData(self):
        con = psycopg2.connect(
            host=hostname,
            database=dbname,
            user=username,
            password=pwd,
            port=port_id)

        cur = con.cursor()
        cur.execute('SELECT * FROM "Area"')

        tablerow = 0
        results = cur.fetchall()
        self.tableWidget.setRowCount(3196)

        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            tablerow += 1




class State(QDialog):
    def __init__(self):
        super(State, self).__init__()
        loadUi("state.ui", self)
        self.backbutton2.clicked.connect(self.stateBack)
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setHorizontalHeaderLabels(["date", "FIPS", "Total Case", "Total Death"])
        self.loadStateData()

    def stateBack(self):
        widget.setCurrentIndex(0)

    def loadStateData(self):
        con = psycopg2.connect(
            host=hostname,
            database=dbname,
            user=username,
            password=pwd,
            port=port_id)

        cur = con.cursor()
        cur.execute('SELECT * FROM "State"')

        tablerow = 0
        results = cur.fetchall()
        self.tableWidget.setRowCount(51)

        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            tablerow += 1



class County(QDialog):
    def __init__(self):
        super(County, self).__init__()
        loadUi("county.ui", self)
        self.backbutton3.clicked.connect(self.countyBack)
        self.tableWidget.setColumnWidth(0, 150)
        self.loadCountyData()

    def countyBack(self):
        widget.setCurrentIndex(0)

    def loadCountyData(self):
        con = psycopg2.connect(
            host=hostname,
            database=dbname,
            user=username,
            password=pwd,
            port=port_id)

        cur = con.cursor()
        cur.execute('SELECT * FROM "County"')

        tablerow = 0
        results = cur.fetchall()
        self.tableWidget.setRowCount(3145)

        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            tablerow += 1



class Population(QDialog):
    def __init__(self):
        super(Population, self).__init__()
        loadUi("population.ui", self)
        self.backbutton4.clicked.connect(self.popBack)
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(0, 150)
        self.loadPopData()

    def popBack(self):
        widget.setCurrentIndex(0)

    def loadPopData(self):
        con = psycopg2.connect(
            host=hostname,
            database=dbname,
            user=username,
            password=pwd,
            port=port_id)

        cur = con.cursor()
        cur.execute('SELECT * FROM "Population" LIMIT 200')

        tablerow = 0
        results = cur.fetchall()
        self.tableWidget.setRowCount(200)

        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
            tablerow += 1



class Covid(QDialog):
    def __init__(self):
        super(Covid, self).__init__()
        loadUi("covid.ui", self)
        self.backbutton5.clicked.connect(self.covidBack)
        self.tableWidget.setColumnWidth(0, 300)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setHorizontalHeaderLabels(["date", "FIPS", "Total Case", "Total Death"])
        self.loadCovidData()

    def covidBack(self):
        widget.setCurrentIndex(0)

    def loadCovidData(self):
        con = psycopg2.connect(
            host=hostname,
            database=dbname,
            user=username,
            password=pwd,
            port=port_id)

        cur = con.cursor()
        cur.execute('SELECT * FROM "Covid_Cases" LIMIT 200')

        tablerow = 0
        results = cur.fetchall()
        self.tableWidget.setRowCount(200)

        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            tablerow += 1


class Vaccine(QDialog):
    def __init__(self):
        super(Vaccine, self).__init__()
        loadUi("Vaccine.ui", self)
        self.backbutton6.clicked.connect(self.vaccineBack)
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 80)
        self.tableWidget.setColumnWidth(2, 60)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 200)
        self.tableWidget.setColumnWidth(5, 200)
        self.tableWidget.setColumnWidth(6, 200)
        self.tableWidget.setColumnWidth(7, 200)
        self.tableWidget.setColumnWidth(8, 200)
        self.loadVaccineData()

    def vaccineBack(self):
        widget.setCurrentIndex(0)

    def loadVaccineData(self):
        con = psycopg2.connect(
            host=hostname,
            database=dbname,
            user=username,
            password=pwd,
            port=port_id)

        cur = con.cursor()
        cur.execute('''SELECT * FROM "Vaccinations"
                    WHERE "Date" > '2021-05-01'
                    ORDER BY "Date" ASC, "FIPS" ASC LIMIT 200 ''')

        tablerow = 0
        results = cur.fetchall()
        self.tableWidget.setRowCount(200)

        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
            self.tableWidget.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row[8])))
            tablerow += 1



class VaccBrand(QDialog):
    def __init__(self):
        super(VaccBrand, self).__init__()
        loadUi("vaccbrand.ui", self)
        self.backbutton7.clicked.connect(self.vaccBrandBack)
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 80)
        self.tableWidget.setColumnWidth(2, 60)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 200)
        self.tableWidget.setColumnWidth(5, 200)
        self.tableWidget.setColumnWidth(6, 200)
        self.tableWidget.setColumnWidth(7, 200)
        self.tableWidget.setColumnWidth(8, 200)
        self.tableWidget.setColumnWidth(9, 200)
        self.tableWidget.setColumnWidth(10, 200)
        self.loadVaccBrandData()

    def vaccBrandBack(self):
        widget.setCurrentIndex(0)

    def loadVaccBrandData(self):
        con = psycopg2.connect(
            host=hostname,
            database=dbname,
            user=username,
            password=pwd,
            port=port_id)

        cur = con.cursor()
        cur.execute('SELECT * FROM "State_Vacc_Dist" LIMIT 200')

        tablerow = 0
        results = cur.fetchall()
        self.tableWidget.setRowCount(200)

        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
            self.tableWidget.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row[8])))
            self.tableWidget.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(str(row[8])))
            self.tableWidget.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(str(row[8])))
            tablerow += 1



class AreaGraph(QDialog):
    def __init__(self):
        super(AreaGraph, self).__init__()
        loadUi("AreaGraph.ui", self)
        self.graphBack1.clicked.connect(self.GraphBack1)
        self.graphButton1.clicked.connect(self.showGraph)

        self.browser = QtWebEngineWidgets.QWebEngineView(self)
        hlayout = QtWidgets.QVBoxLayout(self)
        hlayout.addWidget(self.graphButton1, alignment=QtCore.Qt.AlignHCenter)
        hlayout.addWidget(self.graphBack1, alignment=QtCore.Qt.AlignLeft)
        hlayout.addWidget(self.browser)

    def GraphBack1(self):
        widget.setCurrentIndex(1)

    def showGraph(self):
        #df = px.data.tips()
        #fig = px.box(df, x="day", y="total_bill", color="smoker")
        #fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
        #self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))

        con = psycopg2.connect(
            host=hostname,
            database=dbname,
            user=username,
            password=pwd,
            port=port_id)

        cur = con.cursor()
        cur.execute('''SELECT a."FIPS", c."Total_Cases" FROM "Area" a, "Covid_Cases" c
                                    WHERE a."FIPS" = c."FIPS"
                                    AND a."FIPS" > 100
                                    AND c."Date" = '2020-11-20' ''')

        results = cur.fetchall()
        dftemp = DataFrame(results)
        df = dftemp.rename(columns={0: 'FIPS', 1: 'Total_Cases'})

        fig = px.choropleth(df, geojson=counties, locations='FIPS', color='Total_Cases',
                            color_continuous_scale="Viridis",
                            range_color=(0, 12000),
                            scope="usa",
                            labels={'Total_Cases': 'case number'}
                            )
        #self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))
        fig.show()



class PopRatio(QDialog):
    def __init__(self):
        super(PopRatio, self).__init__()
        loadUi("ratio.ui", self)
        self.backbutton8.clicked.connect(self.ratioBack)
        self.searchbutton.clicked.connect(self.dataSearch)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 180)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.loadRatioData()

    def ratioBack(self):
        self.lineEdit.clear()
        self.textBrowser.clear()
        widget.setCurrentIndex(0)

    def loadRatioData(self):
        con = psycopg2.connect(
            host=hostname,
            database=dbname,
            user=username,
            password=pwd,
            port=port_id)

        cur = con.cursor()
        cur.execute('''SELECT s."Postal_Abbr", p."Total", p."Male", p."Female"
                    FROM "State" s, "Population" p
                    WHERE s."FIPS" = p."FIPS" ''')

        tablerow = 0
        results = cur.fetchall()
        self.tableWidget.setRowCount(51)

        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(round(row[2]/row[1], 2))))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(round(row[3]/row[1], 2))))
            tablerow += 1


    def dataSearch(self):
        self.textBrowser.clear()

        con = psycopg2.connect(
            host=hostname,
            database=dbname,
            user=username,
            password=pwd,
            port=port_id)

        cur = con.cursor()
        cur.execute('''SELECT s."Postal_Abbr", p."Total", p."Male", p."Female"
                            FROM "State" s, "Population" p
                            WHERE s."FIPS" = p."FIPS" ''')
        results = cur.fetchall()


        input = self.lineEdit.text()
        found = False

        for row in results:
            if input == row[0][:2]:
                found = True
                output = '''State: %s\nTotal: %s\nMale Ratio: %s\nFemale Ratio: %s'''\
                         %(row[0][:2], str(row[1]), str(row[2]), str(row[3]))
        if found:
            self.textBrowser.append(output)
        if not found:
            self.textBrowser.append("Data Not Found...")




class StateCounty(QDialog):
    def __init__(self):
        super(StateCounty, self).__init__()
        loadUi("stateCounty.ui", self)
        self.backbutton9.clicked.connect(self.statcountyBack)
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 300)
        self.loadStateCountyData()

    def statcountyBack(self):
        widget.setCurrentIndex(0)

    def loadStateCountyData(self):
        con = psycopg2.connect(
            host=hostname,
            database=dbname,
            user=username,
            password=pwd,
            port=port_id)

        cur = con.cursor()
        cur.execute('''SELECT s."Postal_Abbr", a."Area_Name"
                    FROM "Area" a, "State" s
                    WHERE a."FIPS"/1000 = s."FIPS" ''')

        tablerow = 0
        results = cur.fetchall()
        self.tableWidget.setRowCount(3145)

        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            tablerow += 1






app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

# add Dialogs
widget.addWidget(MainWindow())
widget.addWidget(Area())
widget.addWidget(State())
widget.addWidget(County())
widget.addWidget(Population())
widget.addWidget(Covid())
widget.addWidget(Vaccine())
widget.addWidget(VaccBrand())
widget.addWidget(AreaGraph())
widget.addWidget(PopRatio())
widget.addWidget(StateCounty())


widget.setFixedHeight(850)
widget.setFixedWidth(1120)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
