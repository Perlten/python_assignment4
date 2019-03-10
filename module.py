import pandas as pd
import matplotlib.pyplot as plt
import zipfile
import urllib.request
url = "http://api.worldbank.org/v2/en/indicator/SI.POV.DDAY?downloadformat=csv"


def getData():
    urllib.request.urlretrieve(url, "data.zip")
    zip_ref = zipfile.ZipFile("./data.zip", 'r')
    zip_ref.extractall()
    zip_ref.close()

    data = pd.read_csv(
        "API_SI.POV.DDAY_DS2_en_csv_v2_10474275.csv", skiprows=4)
    contries_names = data.loc[:, "Country Name"].to_dict()
    return data, contries_names


def createDataFramePlot(values, index, label=None, plt_type="line",
                        style="", x_label="", y_label="", title="", fill=False):
    plt.figure()
    for values in values:
        #Creates a pandas Series
        se = pd.Series(values, index=index)
        if fill:
            se = se.ffill()
        ax = se.plot(style=style, kind=plt_type,
                     title=title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        # set x ticks to the same size as index
        ax.set_xticks(range(len(index)))
        ax.set_xticklabels(index, rotation=90)
        if label:
            ax.legend(label)
    plt.show()


# ----------------------------------------------------------------------------------------
# CODE BELOW IS THE SAME AS IN JUPYTER NOTEBOOK!  

data, contries_names = getData()

# # Part 1
c_data = data.loc[(data["Country Name"].isin(
    ["Argentina", "United States", "Venezuela, RB", "Denmark"]))]
c_data = c_data.iloc[:, 4:]
label = [contries_names[x] for x in c_data.index]
createDataFramePlot(c_data.values, c_data.columns, label, style="o-")


# Part 2
# year = "2000"
# c_data = data.sort_values(by=[year], ascending=False).head(10)
# c_data = c_data.loc[:, year]
# index = [contries_names[x] for x in c_data.index]
# createDataFramePlot([c_data.values], index, x_label="Year", plt_type="bar",
#                     y_label="Poverty Rate", title="Poverty Rate in {}".format(year))


# # Part 3

# central_american_countries = ["Belize",
#                               "Costa Rica",
#                               "El Salvador",
#                               "Guatemala",
#                               "Honduras",
#                               "Nicaragua",
#                               "Panama"]

# c_data = data.loc[(data["Country Name"].isin(central_american_countries))]
# c_data = c_data.iloc[:, 4:]
# label = [contries_names[x] for x in c_data.index]
# createDataFramePlot(c_data.values[:,:-1], c_data.columns[:-1], label, style="o-")


# Part 4

# Get top 5 highest poverty count by a given year and show development plot

# year = "1995"
# c_data = data.sort_values(by=[year], ascending=False).head(5)
# c_data = c_data.iloc[:, 4:]
# label = [contries_names[x] for x in c_data.index]
# createDataFramePlot(c_data.values[:,:-1], c_data.columns[:-1], label, style="o-")
