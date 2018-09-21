# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTableWidgetItem,QMessageBox,QComboBox
import traceback

class Table_Util(object):

    @classmethod
    def insert_single_data(cls,table,data):
        """
        表格单条数据插入
        :param table:
        :param data:
        :return:
        """
        table_name = table.objectName()
        try:
            rowPosition = table.rowCount()
            table.insertRow(rowPosition)
            operation = QComboBox(parent=table)
            if table_name == "navi_table":
                operation.addItem("单击")
                operation.addItem("元素")
            elif table_name == "flip_table":
                operation.addItem("点击翻页")
                operation.addItem("规则翻页")
            else:
                operation.addItem("文本")
                operation.addItem("正则")
                operation.addItem("函数")
                operation.addItem("文本标签")
            operation.setCurrentText(data.get("operation",""))
            table.setCellWidget(rowPosition,0,operation)
            table.setItem(rowPosition,1,QTableWidgetItem(data.get("text","")))
            table.setItem(rowPosition,2,QTableWidgetItem(data.get("xpath","")))
            if table_name == "navi_table":
                table.setItem(rowPosition,3,QTableWidgetItem(data.get("placeurl","")))
            elif table_name == "flip_table":
                table.setItem(rowPosition,3,QTableWidgetItem(data.get("begin","")))
                table.setItem(rowPosition,4,QTableWidgetItem(data.get("end","")))
            elif table_name == "field_table":
                table.setItem(rowPosition,3,QTableWidgetItem(data.get("field","")))
                table.setItem(rowPosition,4,QTableWidgetItem(data.get("reg","")))
                table.setItem(rowPosition,5,QTableWidgetItem(data.get("func","")))
            else:
                pass
        except Exception as a:
            QMessageBox.warning (table,
                                    "错误信息",
                                    "插入数据失败{}".format(traceback.format_exc()))

    @classmethod
    def clean_all_data(cls,table):
        """
        清除表格
        :param table:
        :return:
        """
        for row in range(table.rowCount()):
            table.removeRow(0)

    @classmethod
    def clean_table(cls,prev):
        table_list = [prev.navi_table,prev.flip_table,prev.field_table]
        target_table = list(filter(lambda x: not x.isHidden(), table_list))[0]
        Table_Util.clean_all_data(target_table)

    @classmethod
    def get_navi_table(cls,table):
        """
        获取列表表格数据
        :param table:
        :return:
        """
        rows = table.rowCount()
        data_list = []
        for index in range(rows):
            row_data = {}
            row_data['operation'] = table.cellWidget(index,0).currentText()
            row_data['text'] = table.item(index,1).text()
            row_data['xpath'] = table.item(index,2).text()
            row_data['placeurl'] = table.item(index,3).text()
            data_list.append(row_data)
        return data_list


    @classmethod
    def get_flip_table(cls,table):
        """
        获取翻页表格数据
        :param table:
        :return:
        """
        rows = table.rowCount()
        data_list = []
        for index in range(rows):
            row_data = {}
            row_data['operation'] = table.cellWidget(index,0).currentText()
            row_data['text'] = table.item(index,1).text()
            row_data['xpath'] = table.item(index,2).text()
            row_data['begin'] = table.item(index,3).text()
            row_data['end'] = table.item(index,4).text()
            data_list.append(row_data)
        return data_list


    @classmethod
    def get_field_table(cls,table):
        """
        获取翻页表格数据
        :param table:
        :return:
        """
        rows = table.rowCount()
        data_list = []
        for index in range(rows):
            row_data = {}
            row_data['operation'] = table.cellWidget(index,0).currentText()
            row_data['text'] = table.item(index,1).text()
            row_data['xpath'] = table.item(index,2).text()
            row_data['field'] = table.item(index,3).text()
            row_data['reg'] = table.item(index,4).text()
            row_data['func'] = table.item(index,5).text()
            data_list.append(row_data)
        return data_list