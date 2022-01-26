from pathlib import Path
import glob
import openpyxl
from random import *


class Global_range():

    def __init__(self):

        self.quantity_alter = 0
        self.kit_alter = {}
        self.allowed_alter = []
        self.quantity_ranger = 0
        self.kit_ranger = []
        self.final_range_bord = []
        self.final_range_cond = []

    def setKitAlter(self):
        self.kit_alter = self.read_xl()
        self.allowed_alter = [i for i in range(self.quantity_alter)]

    def read_xl(self):
        xlsx_file = Path('data_kourse.xlsx')
        wb_obj = openpyxl.load_workbook(xlsx_file)
        sheet = wb_obj.active
        range_alter = sheet[1:self.quantity_alter]
        dct_alter = dict()
        i = 0
        for row in sheet.iter_rows(min_row=1, min_col=1, max_row=self.quantity_alter, max_col=1):
            dct_alter[i] = row[0].value
            i += 1

        return dct_alter

    def create_ranger(self, ranger):
        temp = []
        for i in ranger:
            temp.append(int(i))
        self.allowed_alter = [i for i in range(self.quantity_alter)]
        self.kit_ranger.append(temp)

    def destroy_ranger(self):
        self.kit_ranger = []

    def toUnif(self):
        lns = len(self.final_range_bord)

        for i in range(self.quantity_ranger):
            if(len(self.kit_ranger[i]) >= lns):
                continue
            for j in range(lns):
                if(j not in self.kit_ranger[i]):
                    indx = self.final_range_bord.index(j)
                    rn = random()
                    if(rn < 0.25):
                        if(indx-1 < 0):
                            self.kit_ranger[i].insert(0, j)
                        else:
                            self.kit_ranger[i].insert(indx-1, j)
                    elif(rn >= 0.25 and rn < 0.75):
                        self.kit_ranger[i].insert(indx, j)
                    else:
                        if(indx+1 >= lns):
                            self.kit_ranger[i].insert(indx, j)
                        else:
                            self.kit_ranger[i].insert(indx+1, j)
        print(self.kit_ranger)

    def toGlobalRangerCondorse(self):
        comparison_mat = [[[0 for i in range(self.quantity_alter)]for j in range(self.quantity_alter)]for i in range(self.quantity_ranger)]
        quantity_point = [0 for i in range(self.quantity_alter)]
        final_range_cond = []
        for k in range(self.quantity_ranger):
            for i in range(self.quantity_alter):
                if (i not in self.kit_ranger[k]):
                    continue
                for j in range(self.quantity_alter):
                    if(j not in self.kit_ranger[k]):
                        continue
                    if(self.kit_ranger[k].index(i) < self.kit_ranger[k].index(j)):
                        comparison_mat[k][i][j] = 1
                    elif(self.kit_ranger[k].index(i) > self.kit_ranger[k].index(j)):
                        comparison_mat[k][i][j] = -1

        for k in range(self.quantity_ranger):
            for i in range(self.quantity_alter):
                for j in range(self.quantity_alter):
                    quantity_point[i] += comparison_mat[k][i][j]

        for i in range(self.quantity_alter):
            final_range_cond.append(quantity_point.index(max(quantity_point)))
            quantity_point[quantity_point.index(max(quantity_point))] = (-self.quantity_alter*self.quantity_ranger)-1

        return final_range_cond

    def toGlobalRangerBord(self):
        final_range_bord = []
        quantity_point = [0 for i in range(self.quantity_alter)]

        for i in range(self.quantity_ranger):
            for j in range(len(self.kit_ranger[i])):
                quantity_point[self.kit_ranger[i][j]] += len(self.kit_ranger[i])-j

        for i in range(self.quantity_alter):
            final_range_bord.append(quantity_point.index(max(quantity_point)))
            quantity_point[quantity_point.index(max(quantity_point))] = -1

        return final_range_bord
