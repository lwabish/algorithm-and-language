package hfdp.template;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * @author Lwabish
 */
public class CoffeeWithHook extends CaffeineBeverageWithHook {
    @Override
    void brew() {
        System.out.println("coffee filter");
    }

    @Override
    void addCondiments() {
        System.out.println("adding sugar and milk");
    }

    @Override
    public boolean needCondiments() {
        String ans = getUserInput();
        String yes = "y";
        return ans.toLowerCase().startsWith(yes);
    }

    private String getUserInput() {
        String answer = null;
        System.out.println("add condiments(y/n)???");
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        try {
            answer = in.readLine();
        } catch (IOException ioe) {
            System.err.println("IO error");
        }
        if (answer == null) {
            return "no";
        }
        return answer;
    }
}
