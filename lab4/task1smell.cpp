// 1.	Рішення задач узагальнення
class Animal
{
   public: Animal() {}
};

class Dog : public Animal
{
   // однаковий конструктор класів, треба підйом
   public: Dog(int age) : Animal()
   {
      m_age = age;
   }

   // однаковий метод класів, треба підйом
   int GetAge() { return m_age; }

   // однакове поле класів, треба підйом
   private: int m_age;
};

class Cat : public Animal
{
   // однаковий конструктор класів, треба підйом
   public: Cat (int age) : Animal()
   {
      m_age = age;
   }

   // однаковий метод класів, треба підйом
   int GetAge() { return m_age; }
   
   // однакове поле класів, треба підйом
   private: int m_age;
};