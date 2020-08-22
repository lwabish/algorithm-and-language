package im.wbw.servlet.hello;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Set;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(urlPatterns = "/set-lang")
public class LangPrefServlet extends HttpServlet {
    private static final Set<String> LANGUAGES = Set.of("en", "zh");

    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String lang = req.getParameter("lang");
        if (LANGUAGES.contains(lang)) {
            Cookie cookie = new Cookie("lang", lang);
            cookie.setPath("/");
            cookie.setMaxAge(86400);
            resp.addCookie(cookie);
        }
        resp.sendRedirect("/home");
    }
}