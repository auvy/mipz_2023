// 1.	Рішення задач узагальнення
class Animal
{
   private: int m_age;

   public: Animal() {}

   public: Animal (int age)
   {
      m_age = age;
   }
   
   int GetAge() { return m_age; }
};

class Dog : public Animal
{
   // idk what to put here
};

class Cat : public Animal
{
   // idk what to put here
};