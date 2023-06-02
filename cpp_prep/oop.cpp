#include <iostream>
#include <string>

using namespace std;

enum Gender { male = 1, female = 2 };

class Animal {
   private:
    Gender gender;

   protected:
    float speed;

   public:
    string name;
    float weight;
    void makeSound() { cout << "animal sound\n"; }

    Gender getGender() { return gender; }
    Animal(string name, float weight, Gender gender)
        : name(name), weight(weight), gender(gender){};

    static int compareWeight(Animal a, Animal b) {
        if (a.weight < b.weight) {
            return -1;
        } else if (a.weight > b.weight) {
            return 1;
        } else {
            return 0;
        }
    }
};

class Bird : public Animal {
   public:
    float wingspan;
    void makeSound() { cout << "tweet!\n"; }
    Bird(string name, float weight, Gender gender, float wingspan)
        : Animal(name, weight, gender), wingspan(wingspan){};

    static Bird parrot() { return Bird("parrot", 0.5, (Gender)(rand() % 2 + 1), 34.0); }
    static int compareWingspan(Bird a, Bird b) {
        if (a.wingspan < b.wingspan) {
            return -1;
        } else if (a.wingspan > b.wingspan) {
            return 1;
        } else {
            return 0;
        }
    }
};

class Hen : public Bird {
   public:
    Hen(string name, float weight, float wingspan)
        : Bird(name, weight, female, wingspan) {}

    Bird layEgg(float babyWeight, float babyWingspan) {
        return Bird(name, babyWeight, (Gender)(rand() % 2 + 1), babyWingspan);
    }
};

int main() {
    Animal dog("dog", 15.0, male);
    dog.makeSound();
    cout << dog.name << endl;
    Bird parrot("parrot", 0.5, female, 34.0);
    cout << parrot.name << endl;
    cout << parrot.wingspan << endl;
    parrot.makeSound();
    cout << Animal::compareWeight(dog, parrot) << endl;
    Bird parrot2 = Bird::parrot();
    cout << Bird::compareWingspan(parrot, parrot2) << endl;
}