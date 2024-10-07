package Loops;
import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class AnimalTest {

    @Test
    public void testDogMakesSound() {
        Dog dog = new Dog();
        String sound = dog.makeSound();
        assertEquals("Dog barks.",sound);

    }
    @Test
    public void testCatMakesSound() {
        Cat cat = new Cat();
        String sound = cat.makeSound();
        assertEquals("Cat meows.",sound);
    }
    @Test
    public void testAnimalMakesSound() {
        Animal animal = new Animal();
        String sound = animal.makeSound();
        assertEquals("Animal makes sound.",sound);
    }
}
