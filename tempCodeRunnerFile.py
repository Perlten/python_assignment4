# Part 2
year = "2000"
c_data = data.sort_values(by=[year], ascending=False).head(10)
c_data = c_data.loc[:, year]
index = [contries_names[x] for x in c_data.index]
createDataFramePlot([c_data.values], index, x_label="Year", plt_type="bar",
                    y_label="Poverty Rate", title="Poverty Rate in {}".format(year))

