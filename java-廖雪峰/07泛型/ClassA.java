import java.util.Arrays;

public class ClassA {
    public static void main(String[] args) {
        Person[] persons = new Person[] { new Person("bob", 60), new Person("jammy", 70), new Person("amy", 80), };
        Arrays.sort(persons);
        System.out.println(Arrays.toString(persons));
    }
}

// Comparable是一个泛型接口
class Person implements Comparable<Person> {
    String name;
    int score;

    Person(String name, int score) {
        this.name = name;
        this.score = score;
    }

    public String toString() {
        return this.name + "," + this.score;
    }

    // 实现了comparable的方法，所有才能sort
    public int compareTo(Person other) {
        return this.name.compareTo(other.name);
    }

}
