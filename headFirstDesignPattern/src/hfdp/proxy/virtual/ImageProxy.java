package hfdp.proxy.virtual;

import javax.swing.*;
import java.awt.*;
import java.net.URL;

/**
 * 代理类和被代理类实现同样的接口，包装一层逻辑
 *
 * @author Lwabish
 */
public class ImageProxy implements Icon {

    ImageIcon imageIcon;
    URL url;
    Thread retrievalThread;
    boolean retrieving = false;

    public ImageProxy(URL url) {
        this.url = url;
    }


    @Override
    public void paintIcon(Component c, Graphics g, int x, int y) {
        if (imageIcon != null) {
            imageIcon.paintIcon(c, g, x, y);
        } else {
            g.drawString("loading cd image", x + 300, y + 190);
            if (!retrieving) {
                retrieving = true;
                retrievalThread = new Thread(() -> {
                    try {
                        imageIcon = new ImageIcon(url, "CD COVER");
                        c.repaint();
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                });
                retrievalThread.start();
            }
        }
    }

    @Override
    public int getIconWidth() {
        if (imageIcon != null) {
            return imageIcon.getIconWidth();
        } else {
            return 800;
        }
    }

    @Override
    public int getIconHeight() {
        if (imageIcon != null) {
            return imageIcon.getIconHeight();
        } else {
            return 600;
        }
    }
}
