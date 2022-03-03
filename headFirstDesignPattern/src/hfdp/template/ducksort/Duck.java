package hfdp.template.ducksort;

/**
 * @author Lwabish
 */
public class Duck implements Comparable<Duck> {
    String name;
    int weight;

    public Duck(String n, int w) {
        this.name = n;
        this.weight = w;
    }

    @Override
    public String toString() {
        return "Duck{" +
                "name='" + name + '\'' +
                ", weight=" + weight +
                '}';
    }

    @Override
    public int compareTo(Duck d) {
        return Integer.compare(this.weight, d.weight);
    }

}
