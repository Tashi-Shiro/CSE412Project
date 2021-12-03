import sys
from PyQt5.QtCore import QDate
from PyQt5.uic import loadUi
import psycopg2
from PyQt5 import QtWidgets, QtWebEngineWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from pandas import DataFrame
from urllib.request import urlopen
import plotly.express as px
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

hostname = "localhost"

with open('setting.txt') as setting:
    lines = setting.readlines()

dbname = lines[0].replace(" ", "").replace("\n", "").split('=')[1]
username = lines[1].replace(" ", "").replace("\n", "").split('=')[1]
pwd = lines[2].replace(" ", "").replace("\n", "").split('=')[1]
port_id = lines[3].replace(" ", "").replace("\n", "").split('=')[1]


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("./GUI/main.ui", self)
        self.areabutton.clicked.connect(self.gotoArea)
        self.statebutton.clicked.connect(self.gotoState)
        self.countybutton.clicked.connect(self.gotoCounty)
        self.popbutton.clicked.connect(self.gotoPopulation)
        self.covidbutton.clicked.connect(self.gotoCovid)
        self.vaccinebutton.clicked.connect(self.gotoVaccine)
        self.vaccbrandbutton.clicked.connect(self.gotoVaccBrand)
        self.ratiobutton.clicked.connect(self.gotoRatio)
        self.stateCountybutton.clicked.connect(self.gotoStateCounty)
        self.vaccineCompletebutton.clicked.connect(self.gotoVaccineComplete)
        self.VaccBrandCompletebutton.clicked.connect(self.gotoVaccBrandComplete)

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
    def gotoVaccineComplete(self):
        widget.setCurrentIndex(11)
    def gotoVaccBrandComplete(self):
        widget.setCurrentIndex(12)


class Area(QDialog):
    def __init__(self):
        super(Area, self).__init__()
        loadUi("./GUI/area.ui", self)
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
        loadUi("./GUI/state.ui", self)
        self.backbutton2.clicked.connect(self.stateBack)
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setHorizontalHeaderLabels(["date", "FIPS", "Total Case", "Total Death"])
        self.loadStateData()

    def stateBack(self):
        widget.setCurrentIndex(0)

    def loadStateData(self):
        con = psycopg2.connect(
            host = hostname,
            database = dbname,
            user = username,
            password = pwd,
            port = port_id)

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
        loadUi("./GUI/county.ui", self)
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
        loadUi("./GUI/population.ui", self)
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
        loadUi("./GUI/covid.ui", self)
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
        loadUi("./GUI/Vaccine.ui", self)
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
        loadUi("./GUI/vaccbrand.ui", self)
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
        loadUi("./GUI/AreaGraph.ui", self)
        self.graphBack1.clicked.connect(self.GraphBack1)
        self.graphButton1.clicked.connect(self.showGraph)
        self.dateEdit.setMinimumDate(QDate(2020, 1, 1))
        self.dateEdit.setMaximumDate(QDate(2021, 12, 31))

        #self.browser = QtWebEngineWidgets.QWebEngineView(self)
        #hlayout = QtWidgets.QVBoxLayout(self)
        #hlayout.addWidget(self.graphButton1, alignment=QtCore.Qt.AlignHCenter)
        #hlayout.addWidget(self.graphBack1, alignment=QtCore.Qt.AlignLeft)
        #hlayout.addWidget(self.browser)


    def GraphBack1(self):
        widget.setCurrentIndex(1)


    def showGraph(self):
        #df = px.data.tips()
        #fig = px.box(df, x="day", y="total_bill", color="smoker")
        #fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
        #self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))

        year = self.dateEdit.date().year()
        month = self.dateEdit.date().month()
        day = self.dateEdit.date().day()

        if (year == 2020 and month != 2 and month != 1 and day <= 30) or \
            (year == 2021 and month != 2 and month <= 9 and day <= 30) or \
            (year == 2020 and month == 2 and 1 <= day <= 29) or \
            (year == 2021 and month == 2 and 1 <= day <= 28):
            year = str(year)
            month = str(month).zfill(2)
            day = str(day).zfill(2)
            date = "'%s-%s-%s'" % (year, month, day)

            self.errorText.clear()
            self.errorText.append("input correct, displaying graph...")

            con = psycopg2.connect(
                host=hostname,
                database=dbname,
                user=username,
                password=pwd,
                port=port_id)

            cur = con.cursor()
            SQL = '''SELECT a."FIPS", c."Total_Cases" FROM "Area" a, "Covid_Cases" c
                            WHERE a."FIPS" = c."FIPS"
                            AND a."FIPS" > 100
                            AND c."Date" = %s ''' % date
            cur.execute(SQL)

            results = cur.fetchall()
            dftemp = DataFrame(results)
            df = dftemp.rename(columns={0: 'FIPS', 1: 'Total_Cases'})

            for index, row in df.iterrows():
                number = str(df.loc[index, 'FIPS'])
                number = number.zfill(5)
                df.loc[index, 'FIPS'] = number

            fig = px.choropleth(df, geojson=counties, locations='FIPS', color='Total_Cases',
                                color_continuous_scale="Viridis",
                                range_color=(0, 12000),
                                scope="usa",
                                labels={'Total_Cases': 'case number'}
                                )
            fig.show()

        else:
            self.errorText.clear()
            self.errorText.append("Date input was wrong, please select again!")






class PopRatio(QDialog):
    def __init__(self):
        super(PopRatio, self).__init__()
        loadUi("./GUI/ratio.ui", self)
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
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(round(row[2]/row[1], 3))))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(round(row[3]/row[1], 3))))
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
                output = '''State: %s\nTotal: %s\nMale Ratio: %s%%\nFemale Ratio: %s%%'''\
                         %(row[0][:2], str(row[1]), str(round(row[2]/row[1], 3)*100), str(round(row[3]/row[1], 3)*100))
        if found:
            self.textBrowser.append(output)
        if not found:
            self.textBrowser.append("Data Not Found...")




class StateCounty(QDialog):
    def __init__(self):
        super(StateCounty, self).__init__()
        loadUi("./GUI/stateCounty.ui", self)
        self.backbutton9.clicked.connect(self.statcountyBack)
        self.searchButton2.clicked.connect(self.dataSearch2)
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 300)
        self.loadStateCountyData()

    def statcountyBack(self):
        self.lineEdit2.clear()
        self.textBrowser2.clear()
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

    def dataSearch2(self):
        self.textBrowser2.clear()

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
        table = cur.fetchall()
        input = self.lineEdit2.text()

        found = False

        for row in table:
            if(len(input) == 2):
                if input == row[0][:2]:
                    found = True
                    output = '''State: %s\nCounty: %s\n'''\
                             %(row[0][:2], row[1])
                    if found:
                        self.textBrowser2.append(output)
            else:
                if(input.ljust(50) == row[1]):
                    found = True
                    output = '''County: %s\nState: %s\n''' \
                             % (row[1], row[0][:2])
                    if found:
                        self.textBrowser2.append(output)

        if not found:
            self.textBrowser2.append("Data Not Found...")





class VaccineComplete(QDialog):
    def __init__(self):
        super(VaccineComplete, self).__init__()
        loadUi("./GUI/vaccineComplete.ui", self)
        self.backbutton10.clicked.connect(self.vaccineCompleteBack)
        self.searchbutton3.clicked.connect(self.dataSearch3)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 180)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 150)
        self.loadVaccineCompleteData()

    def vaccineCompleteBack(self):
        self.lineEdit3_1.clear()
        self.textBrowser3.clear()
        widget.setCurrentIndex(0)

    def loadVaccineCompleteData(self):
        con = psycopg2.connect(
            host=hostname,
            database=dbname,
            user=username,
            password=pwd,
            port=port_id)

        cur = con.cursor()
        cur.execute('''SELECT "Date", "FIPS", "Complete", "Complete_18Plus", "Complete_65Plus"
                    FROM "Vaccinations" 
                    WHERE "FIPS" = 4
                    OR "FIPS" = 4013
                    ORDER BY "Date" ASC, "FIPS" ASC ''')

        tablerow = 0
        results = cur.fetchall()
        self.tableWidget.setRowCount(640)

        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            tablerow += 1


    def dataSearch3(self):
        self.textBrowser3.clear()

        con = psycopg2.connect(
            host=hostname,
            database=dbname,
            user=username,
            password=pwd,
            port=port_id)

        cur = con.cursor()
        cur.execute('''SELECT "Date", "FIPS", "Complete", "Complete_18Plus", "Complete_65Plus"
                    FROM "Vaccinations"
                    WHERE "FIPS" = 4
                    OR "FIPS" = 4013
                    ORDER BY "Date" ASC, "FIPS" ASC ''')
        results = cur.fetchall()


        dateInput = self.lineEdit3_1.text()

        found = False

        for row in results:
            if dateInput == str(row[0]):
                found = True
                output = "Date: %s\nFIPS(Area): %s\nTotal Complete: %s\nComplete Over 18: %s\nComplete Over 65: %s\n"\
                        % (row[0], row[1], row[2], row[3], row[4])
                if found:
                    self.textBrowser3.append(output)

        if not found:
            self.textBrowser3.append("Data Not Found...")






class VaccBrandComplete(QDialog):
    def __init__(self):
        super(VaccBrandComplete, self).__init__()
        loadUi("./GUI/vaccBrandComplete.ui", self)
        self.backbutton11.clicked.connect(self.vaccBrandCompleteBack)
        self.searchbutton4.clicked.connect(self.dataSearch4)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 180)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 150)
        self.tableWidget.setColumnWidth(5, 150)
        self.tableWidget.setColumnWidth(6, 150)
        self.loadVaccBrandCompleteData()

    def vaccBrandCompleteBack(self):
        self.lineEdit4.clear()
        self.textBrowser4.clear()
        widget.setCurrentIndex(0)

    def loadVaccBrandCompleteData(self):
        con = psycopg2.connect(
            host=hostname,
            database=dbname,
            user=username,
            password=pwd,
            port=port_id)

        cur = con.cursor()
        cur.execute('''SELECT "Date", "FIPS", "Dist_Total", "Dist_Janssen", "Dist_Moderna", "Dist_Pfizer", "Given_Total"
                    FROM "State_Vacc_Dist" 
                    WHERE "FIPS" = 4
                    ORDER BY "Date" ASC, "FIPS" ASC ''')

        tablerow = 0
        results = cur.fetchall()
        self.tableWidget.setRowCount(320)

        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            tablerow += 1


    def dataSearch4(self):
        self.textBrowser4.clear()

        con = psycopg2.connect(
            host=hostname,
            database=dbname,
            user=username,
            password=pwd,
            port=port_id)

        cur = con.cursor()
        cur.execute('''SELECT "Date", "FIPS", "Dist_Total", "Dist_Janssen", "Dist_Moderna", "Dist_Pfizer", "Given_Total"
                    FROM "State_Vacc_Dist" 
                    WHERE "FIPS" = 4
                    ORDER BY "Date" ASC, "FIPS" ASC ''')
        results = cur.fetchall()


        dateInput = self.lineEdit4.text()

        found = False

        for row in results:
            if dateInput == str(row[0]):
                found = True
                output = '''
Date: %s\nFIPS(States): %s\nTotal Complete: %s\nJanssen Complete: %s\nModerna Complete: %s
Pfizer Complete: %s\nTotal Given: %s\n'''\
                        % (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                if found:
                    self.textBrowser4.append(output)

        if not found:
            self.textBrowser4.append("Data Not Found...")


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
widget.addWidget(VaccineComplete())
widget.addWidget(VaccBrandComplete())

widget.setWindowTitle("CSE 412 Covid-19 Database")
widget.setFixedHeight(850)
widget.setFixedWidth(1120)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
