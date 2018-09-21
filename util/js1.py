# -*- coding: utf-8 -*-

class MyJs(object):

    INIT_EVENT = '''
    
    var objs = document.getElementsByTagName('*');
    function initEvent()
    {
        for(var i = 0; i < objs.length; i++) {
            (function(i){
                objs[i].onmouseover = function(ev){
                    var oEvent = ev || event;
                    oEvent.cancelBubble = true;
                    oEvent.stopPropagation();
                    oEvent.target.style.borderWidth = '2px';
                    oEvent.target.style.borderStyle = 'outset';
                    oEvent.target.style.borderColor = 'red';
                    objs[i].addEventListener("mouseout",clearStyle,true);
                    
                };
                
                objs[i].onclick = function(ev){
                    var oEvent = ev || event;
                    //js阻止事件冒泡
                    oEvent.cancelBubble = true;
                    oEvent.stopPropagation();
                    if(objs[i].getAttribute("clickable")==null){
                        oEvent.target.setAttribute("target","_blank");
                        removeAlloutEvent();
                        oEvent.target.style.borderWidth = '2px';
                        oEvent.target.style.borderStyle = 'outset';
                        oEvent.target.style.borderColor = 'blue';
                        oEvent.target.setAttribute("clickable",true);
                        resultToQt(getInfo(oEvent.target));
                    }else{
                        oEvent.target.removeAttribute("target");
                    }
                };
                
                objs[i].addEventListener("mouseout",clearStyle,true);
            })(i)
        }
        
    }
    
    
    //去除所有元素的悬停事件
    function removeAlloutEvent(){
        for(var i = 0; i < objs.length; i++) {
            objs[i].removeEventListener("mouseout",clearStyle,true);
        }
    }
    
    //去除样式
    function clearStyle(eve)
    {
        eve.cancelBubble = true;
        eve.stopPropagation();
        eve.target.style.borderStyle = 'none';
        eve.target.removeAttribute("clickable");
    }
    
    
    function getInfo(element){
        var info = {};
        info.xpath = readXPath(element);
        info.text = element.innerText;
        info.operation = "单击";
        info.begin = "1"
        info.end = "1"
        info.reg = ""
        info.func = ""
        info.field = ""
        return JSON.stringify(info);
    }
    
    
    //从页面返回数据到qt
    function resultToQt(value){
        if(window.bridge != null){
            window.bridge.strValue = value
        }
    
    }
    
    
    //获取元素xpath
    function readXPath(element) {
        if (element.id !== "") {//判断id属性，如果这个元素有id，则显 示//*[@id="xPath"]  形式内容
            return '//*[@id=\"'+ element.id +'\"]';
        }
        //这里需要需要主要字符串转译问题，可参考js 动态生成html时字符串和变量转译（注意引号的作用）
        if (element == document.body) {//递归到body处，结束递归
            return '/html/' + element.tagName.toLowerCase();
        }
        var ix = 1,//在nodelist中的位置，且每次点击初始化
             siblings = element.parentNode.childNodes;//同级的子元素
    
        for (var i = 0, l = siblings.length; i < l; i++) {
            var sibling = siblings[i];
            //如果这个元素是siblings数组中的元素，则执行递归操作
            if (sibling == element) {
                return arguments.callee(element.parentNode) + '/' + element.tagName.toLowerCase() + '[' + (ix) + ']';
                //如果不符合，判断是否是element元素，并且是否是相同元素，如果是相同的就开始累加
            } else if (sibling.nodeType == 1 && sibling.tagName == element.tagName) {
                ix++;
            }
        }
    };
    
    
    
    initEvent();
    
    
    new QWebChannel(qt.webChannelTransport, function (channel) {
    
        window.bridge = channel.objects.bridge;
    })
    
    
    
   
    '''



