# coding=utf-8

class WidgetStyle(object):

    QTabWidget = """
        
    QTabWidget#right QTabBar::tab { 
        border-color: #DCDCDC; 
        border-width: 1px; 
        background:#DCDCDC; 
        color:black; 
        min-width:30ex; 
        min-height:10ex; 
    } 
    QTabWidget#right QTabBar::tab:!selected:hover{ 
        width:100px; 
        height:24px; 
        border:1px solid #FFE4C4; 
        background:#FFE4C4; 
    } 
    
    QTabWidget#right QTabBar::tab:selected{ 
        background:green; 
        color:white; 
    } 
    
    """


    My_QTabWidget = """
        
    QTabWidget#myself QTabBar::tab { 
        border-color: #DCDCDC; 
        border-width: 1px; 
        background:white; 
        color:black; 
        min-width:30ex; 
        min-height:0ex;         
        border-top-left-radius: 20px; 
        border-top-right-radius: 20px; 
        border-bottom-left-radius: 20px; 
        border-bottom-right-radius: 20px; 
    } 
    QTabWidget#myself QTabBar::tab:!selected:hover{ 
        width:100px; 
        height:24px; 
        border:1px solid #FFE4C4; 
        background:white; 
    } 
    
    QTabWidget#myself QTabBar::tab:selected{ 
        background:#B0E0E6; 
        color:black; 
    } 
    
    """


    TREE_WIDGET = """
    
        QTreeView{
            font-size:20px
        }
        QHeaderView::section{
            height:40px;
            font-size:15px;
            background:#7EC0EE;
            text-align:center;
            font:bold;
            border:1px solid white;
        }
        
    
    """




