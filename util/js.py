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
                    if(oEvent.target.getAttribute("myselect")==null){
                        oEvent.target.style.borderStyle = 'outset';
                    }
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
                        oEvent.target.style.borderStyle = 'dotted';
                        oEvent.target.style.borderColor = 'red';
                        oEvent.target.setAttribute("clickable",true);
                        //resultToQt(getInfo(oEvent.target));
                        var myinput = document.getElementById('rule_info');
                        xpath = readXPath(oEvent.target);
                        myinput.value = js_xpath(get_all_xpath(xpath));
                        //myinput.value = getInfo(oEvent.target);
                        document.getElementById("myform_spider").submit();
                        
                        
                    }else{
                        //oEvent.target.removeAttribute("target");
                    }
                };
                //objs[i].addEventListener("mouseout",clearStyle,true);
            })(i)
        }
        
    }
    
    
    function js_xpath(xpath) {
        var xresult = document.evaluate(xpath, document, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null);
        var xnodes = [];
        for(i=0,length=xresult.snapshotLength;i<length;i++){
            thisElement = xresult.snapshotItem(i);
            thisElement.style.borderWidth = '2px';
            thisElement.style.borderStyle = 'dotted';
            thisElement.style.borderColor = 'red';
            thisElement.setAttribute("myselect",true);
            xnodes.push(getInfo(thisElement));
        }
        return JSON.stringify(xnodes);
        
    }
    
    
    function get_all_xpath(xpath){
        xpath = xpath.replace(/\\[\\d\\]/g,'');
        return xpath;
    }
    
    
    

    
    function getTitle(){
        var title = "";
        try{
            title = document.title;
        }catch(err){
            title = "链接"
        }
        return title;
    }
    
    
    function appendForm(){
        newform = document.createElement("form");
        newform.setAttribute('name','myform_spider');
        newform.setAttribute('accept-charset','UTF-8');
        newform.setAttribute('id','myform_spider');
        newform.setAttribute('action','http://localhost:9997/internet');
        newform.setAttribute('method','post');
        newform.setAttribute('style','display: none;');
        newform.setAttribute('target','spider_iframe');
        document.getElementsByTagName("body")[0].appendChild(newform)
        
        var myinput = document.createElement('input');
        myinput.type = 'hidden';
        myinput.id = 'rule_info';
        myinput.name = 'rule_info';
        myinput.value = '';
        document.myform_spider.appendChild(myinput);
        
        var spider_iframe = document.createElement('iframe');
        spider_iframe.setAttribute('name','spider_iframe');
        spider_iframe.setAttribute('style','display: none;');
        spider_iframe.setAttribute('id','spider_iframe');
        document.getElementsByTagName("body")[0].appendChild(spider_iframe)
        
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
        
        if(eve.target.getAttribute("myselect")==null){
            eve.cancelBubble = true;
            eve.stopPropagation();
            eve.target.style.borderStyle = 'none';
            //eve.target.removeAttribute("clickable");
        }
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
        return info;
        //return JSON.stringify(info);
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
    
    setTimeout(appendForm(),1000);
    
    
    new QWebChannel(qt.webChannelTransport, function (channel) {
    
        window.bridge = channel.objects.bridge;
    })
    
   
    '''



