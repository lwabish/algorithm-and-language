public class JavaSwitch {
    public static void main(String[] args) {
        // 经典语法，漏了break很严重
        String n = "a";
        switch (n) {
            case "a":
                System.out.println("1");
                break;
            case "b":
            case "c":
                System.out.println("o");
                break;
            default:
                break;
        }
        // java 12+ switch表达式
        String fruit = "apple";
        int opt = switch (fruit) {
            case "apple" -> 1;
            case "pear" -> {
                int x = 3;
                yield x;
            }
            default -> 0;
        };

    }
}