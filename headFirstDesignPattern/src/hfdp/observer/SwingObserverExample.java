package hfdp.observer;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 * @author wubowen
 */
public class SwingObserverExample {
    JFrame frame;

    public void go() {
        frame = new JFrame();

        JButton button = new JButton("holy shit?");
        button.addActionListener(new AngelListener());
        button.addActionListener(new DevilListener());
        frame.getContentPane().add(BorderLayout.CENTER, button);

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(BorderLayout.CENTER, button);
        frame.setSize(300,300);
        frame.setVisible(true);
    }

    static class AngelListener implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {
            System.out.println("angel");
        }
    }

    static class DevilListener implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {
            System.out.println("devil");
        }
    }

    public static void main(String[] args) {
        SwingObserverExample example = new SwingObserverExample();
        example.go();
    }
}
