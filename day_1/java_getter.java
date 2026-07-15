class Person{
    private String name = "mani";
    String getName(){
        return name;
    } 
}
public class java_getter {
    public static void main(String[] args) {
        Person p1 = new Person();
        String name = p1.getName();
        System.out.print(name);

    }
}
