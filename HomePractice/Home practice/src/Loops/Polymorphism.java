package Loops;

public class Polymorphism {
    public static void main(String[] args) {
        Animal[] animal = new Animal[3];
        animal[0] = new Cat();
        animal[1] = new Dog();
        animal[2] = new Cat();
        for (Animal ani : animal) {
            System.out.println(ani.makeSound());
        }


    }
}
